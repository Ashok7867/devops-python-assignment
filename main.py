from pydub import AudioSegment
from pydub.playback import play


# Load audio file
audio_file = AudioSegment.from_file("example.mp3")


# Play audio
play(audio_file)
