import pyaudio
import wave
from pydub import AudioSegment
from pydub.playback import play

'''
    The channels parameter in the PyAudio code specifies the number of audio channels to be used for recording or playback.
    In this specific code, channels=1 is used, which means it's set to record audio in mono.

    Here's what this means:

    Mono (1 channel): When channels is set to 1, you are recording audio in mono. Mono audio has a single channel,
    which means it captures sound as a single audio stream. It's commonly used for voice recordings, podcasts, and many other
    applications where stereo audio (with multiple channels) is not required. In mono audio, the same sound is played through
    both left and right speakers or headphones, and there is no spatial separation between the audio sources.

    Stereo (2 channels): If you were to set channels to 2, you would be recording audio in stereo.
    Stereo audio has two separate channels: one for the left ear and one for the right ear. This allows for spatial
    separation of audio sources and is used in applications like music production, movies, and video games to create
    a sense of direction and depth in the audio.

    The choice of mono or stereo recording depends on the specific use case. For many tasks like voice recording,
    mono is sufficient and conserves storage space, while stereo is used for situations where spatial audio separation is important.
    In this code, it's set to mono (channels=1) because it's a common choice
    for simple audio recording tasks like capturing voice recordings from a microphone.

    Mono Audio:

    Mono audio has a single channel, meaning it captures or plays back sound as a single, combined audio stream.
    In mono audio, all audio sources are mixed together, and there is no spatial separation between them.
    This means that if you're recording in mono, all sound sources, regardless of their physical direction, are combined
    into one audio track.
    Mono is typically used for tasks where spatial separation is not important or necessary. For example, voice recording,
    phone calls, podcasts, and many audio conferences are often recorded and played back in mono.
    Stereo Audio:

    Stereo audio has two separate channels: one for the left ear and one for the right ear
    (commonly referred to as the left and right channels).
    Stereo audio allows for spatial separation and directionality.
    Different audio sources can be assigned to the left and right channels, creating a sense of direction and space.
    For example, in a stereo recording, you can perceive that one sound source is on your left and another is on your right.
    Stereo is commonly used in music production, movies, video games, and other forms of multimedia where the spatial
    placement of audio sources is important for creating an immersive and realistic experience.
'''

def record_and_save_audio(file_name, duration_seconds):
    p = pyaudio.PyAudio()

    format = pyaudio.paInt16  # 16-bit integer format
    channels = 1  # Mono audio
    rate = 44100  # Sampling rate (samples per second)
    frames_per_buffer = 1024  # Number of frames per buffer

    stream = p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=frames_per_buffer)
    print("Recording...")
    frames = []

    try:
        for _ in range(0, int(rate / frames_per_buffer * duration_seconds)):
            data = stream.read(frames_per_buffer)
            frames.append(data)
    except KeyboardInterrupt: # # Ctrl + C
        pass

    print("Recording stopped.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    sound_file = wave.open("output.wav", "wb")
    sound_file.setnchannels(1)


    # p.get_sample_size(pyaudio.paInt16) to get the sample size in bytes for
    # the specified audio format (pyaudio.paInt16).
    #
    # The sample width represents the size of each audio sample in bytes.


    sound_file.setsampwidth(p.get_sample_size(pyaudio.paInt16))

    # The framerate determines how many audio samples are recorded or played back per second.
    #
    # 44,100 Hz is a common sampling rate used for CD-quality audio, and it's
    # often used in various audio recording and playback scenarios.

    sound_file.setframerate(44100)

    # b'' creates an empty bytes object.
    sound_file.writeframes(b''.join(frames))
    sound_file.close()

    print(f"Audio saved to {file_name}")

record_and_save_audio("output.wav", 11)


def play_audio_from_file(file_name):
    try:
        audio = AudioSegment.from_file(file_name)
        play(audio)
    except Exception as e:
        print(f"Error playing audio: {e}")

play_audio_from_file("output.wav")
