from gtts import gTTS
import os
import speech_recognition as sr
from time import ctime
import time
from search_fn import *

def speak(audioString):
    print(audioString)
    tts = gTTS(text = audioString , lang  = 'en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone(0) as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech Recognition using Google
    data = ""
    try:
        data = r.recognize_google(audio).lower()
        print("You said:- "+ data)
    except sr.UnknownValueError:
        print("Unable to recognize")
    except sr.RequestError as e:
        print("Could not request results")

    return data.lower()


def zizou(data):
    if "how are you" in data:
        speak("I am awesome")

    elif "what time is it" in data:
        speak(ctime())

    elif "google" in data:
        searchGoogle(data)

    elif "wikipedia" in data:
        searchWikipedia(data)
    elif "bye" in data:
        return 0



if __name__ == "__main__":
    time.sleep(2)
    speak("Hey Piyush!, Wassup?")
    while 1:
        data = recordAudio()
        if zizou(data) == 0:
            break
