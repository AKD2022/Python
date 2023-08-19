# Trying to use microphone for input
import os
import pyaudio
import wave
import time
import speech_recognition as sr
from pydub import AudioSegment
from os import path
from gtts import gTTS

# Creating Functions 

# Remove Audio(s)
def removeAudio():
    os.remove("output.wav") 

def removeAudio2():
    os.remove("output2.wav")

# Convert Audio to Text 
def convertAudioToText():
    r = sr.Recognizer()
    AUDIOFILE = "output.wav"
    r = sr.Recognizer()
    with sr.AudioFile(AUDIOFILE) as source:
            audio = r.record(source)                  
            return(r.recognize_google(audio))
    
# Convert Text to Audio 
def convertTextToAudio():
     language = 'en'
     myobj = gTTS(text=mytext, lang=language, slow=False)
     myobj.save("output2.wav")
     os.system("afplay output2.wav")

# Record Audio Function
def recordAudio():
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


    frames = []
    seconds = 3
    for i in range(0, int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)


    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open("output.wav", 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))    
    wf.close()  

# Play Audio
def playAudio():
    r = sr.Recognizer()
    play = "output.wav"
    os.system("afplay " + play)

# Basic Format
print("What is your name? (Say it)")
recordAudio() 
name = convertAudioToText()
print("I heard: " + str(name) + " was that correct?")
removeAudio()

recordAudio()
response = convertAudioToText()
response.lower()

if ('y' in response):
    print("Ok, great! Syncing now!")
    time.sleep(1)
    print("...")
    time.sleep(3)
    print("Syncing Complete")
elif ('n' in response):
    name = input("Alright, type in your name: ")
    print("Ok, great! Syncing now!")
    time.sleep(1)
    print("...")
    time.sleep(3)
    print("Syncing Complete")

mytext = ("Great! Hello " + name + ", my name is AK, and I am your personal voice assistant")
convertTextToAudio()
removeAudio()
removeAudio2()