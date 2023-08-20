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
    AUDIOFILE = "output.wav"
    r = sr.Recognizer()
    with sr.AudioFile(AUDIOFILE) as source:
            audio = r.record(source)                  
            return(r.recognize_google(audio))

# Convert Text to Audio
def convertTextToAudio():
    myobj = gTTS(text=speech, lang='en', slow=False)
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
speech = "What is your name?"
print(speech)
# Converting Text to Audio
convertTextToAudio()

# Record Name
recordAudio() 
name = convertAudioToText()

# Print Name
speech = "I heard: " + str(name) + ", was that correct?"
print(speech)
# Converting to Audio
convertTextToAudio()




recordAudio()
response = convertAudioToText()
response.lower()

if ('y' in response):
    speech = "Syncing now!"
    print(speech)
    convertTextToAudio()
    time.sleep(1)
    print("...")
    time.sleep(3)
    speech = "Syncing Complete"
    print(speech)
    convertTextToAudio()

elif ('n' in response):
    speech = "Alright, type in your name"     
    convertTextToAudio()
    name = input("Name: ")

    speech = "Syncing Now!"
    print(speech)
    convertTextToAudio()
    time.sleep(1)
    print("...")
    time.sleep(3)
    speech = "Syncing Complete"
    print(speech)
    convertTextToAudio()


speech = "Great! Hello, " + name + ", my name is AK, and I am your personal voice assistant"
print(speech)
convertTextToAudio()


removeAudio()
removeAudio2()