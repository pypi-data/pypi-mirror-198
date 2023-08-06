import openai
import pyaudio
import wave
import tempfile

__all__ = ("get_response", "speech_to_text", "api_key")

api_key = None


def median(values: list[int]):
    return sorted(values)[int(len(values) / 2)]


def convert_chunk_to_ints(chunk: bytearray):
    res = [int(a) + 255 * int(b) for a, b in zip(chunk[::2], chunk[1::2])]
    res = [x if x < 2 ** 15 else 2 ** 16 - x for x in res]
    return res


def record_to_tempfile():
    """
    :returns: Path to the created file.
    """
    # Parameters
    freq = 44100
    # A buffer size that is pretty close to 1024, but still divisible by the
    # total number of samples
    buffer_size = 1024
    # Hard cap on the input size
    max_duration = 30000  # milliseconds
    probe_duration = 2000  # milliseconds
    threshold = 0.5

    # Set up input stream and output file
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=freq, input=True,
                    frames_per_buffer=buffer_size)
    _, tmpfile = tempfile.mkstemp(suffix=".wav")
    output_file = wave.open(tmpfile, "wb")
    output_file.setnchannels(1)
    output_file.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    output_file.setframerate(freq)

    def cleanup():
        # Cleanup
        output_file.close()
        stream.stop_stream()
        stream.close()
        p.terminate()

    chunks_per_probe = int(freq * probe_duration / 1000 / buffer_size)
    max_probes = (max_duration) / probe_duration
    med = 0
    i = 0
    while True:
        probe = bytearray()
        for _ in range(0, chunks_per_probe):
            chunk = stream.read(buffer_size)
            output_file.writeframes(chunk)
            probe += chunk
        int_probe = convert_chunk_to_ints(probe)
        _med = median(list(map(abs, int_probe)))
        # The remaining probes must keep raising the threshold. This is
        # protection against an infinite loop in case the initial probe was too
        # quiet.
        med = max(_med, med)
        if i > max_probes:
            cleanup()
            raise Exception("Maximum duration exceeded")
        if _med <= threshold * med:
            break

    return tmpfile


def get_response(prompt: str) -> str:
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def speech_to_text() -> str:
    file_path = record_to_tempfile()
    with open(file_path, "rb") as file:
        openai.api_key = api_key
        response = openai.Audio.transcribe("whisper-1", file)
    return response.text
