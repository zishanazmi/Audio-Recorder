import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 44100

duration = int(input("Enter the duration to record the audio: "))


recording = sd.rec(int(duration * freq),
				samplerate=freq, channels=2)
				
print("Recording...")

sd.wait()

wv.write("recording1.wav", recording, freq, sampwidth=2)