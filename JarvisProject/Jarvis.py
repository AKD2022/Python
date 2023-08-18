# Basic Format
import os
name = input("What is your name?\n")
name = name.upper()

if (name != "ARNESH"):
    greet = "AudioFiles/Hello.wav"
    os.system("afplay " + greet)
elif (name == "ARNESH"):
    greetA = "AudioFiles/HelloArnesh.wav"
    os.system("afplay " + greetA)
#

# Trying to use microphone for input
import pyaudio
import wave
import time
import speech_recognition as sr
from pydub import AudioSegment
from os import path
# Remove Audio
def removeAudio():
    time.sleep(5)
    os.remove("output.wav") 

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK)

print("recording started")

frames = []
seconds = 3
for i in range(0, int(RATE / CHUNK * seconds)):
    data = stream.read(CHUNK)
    frames.append(data)

print("recording finished")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open("output.wav", 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

greet = "output.wav"
os.system("afplay " + greet)

AUDIO_FILE = "output.wav"
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        print("Transcription: " + r.recognize_google(audio))


removeAudio()




