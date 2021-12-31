import pyttsx3
import threading
import pyaudio
from vosk import Model, KaldiRecognizer, SetLogLevel
from time import sleep
import json
import os

isActive = False
isTalking = False
doNotStartSpeak = False

def toggleActive():
    global isActive
    global doNotStartSpeak
    global stop_listening

    if doNotStartSpeak == False:
        if isActive == False:
            isActive = True
            # stop_listening = r.listen_in_background(m, callback)
            x = threading.Thread(target=speak, args=("I am active.",), daemon=True)
            x.start()


        elif isActive == True:
            isActive = False
            #stop_listening(wait_for_stop=False)
            x = threading.Thread(target=speak, args=("I am not active.",), daemon=True)
            x.start()

def speak(command):
    global isTalking
    global doNotStartSpeak
    doNotStartSpeak = True

    sleep(0.1)

    if isTalking == True:
        engine = pyttsx3.init()
        engine.stop()

        x = threading.Thread(target=speak, args=(command,), daemon=True)
        x.start()
        return
    elif isTalking == False:
        from window import ttsText
        ttsText(command)
        isTalking = True
        doNotStartSpeak = False

        engine = pyttsx3.init()

        engine.say(command)
        engine.runAndWait()
        print("Done")
        
        isTalking = False
        return

def listening():
    model = Model(r"vosk-model-en-us-0.22-lgraph")
    recognizer = KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

    while True:
        while isActive == True:
            stream.start_stream()

            while isActive == True:
                data = stream.read(4096, exception_on_overflow = False)

                if recognizer.AcceptWaveform(data):
                    output = json.loads(recognizer.Result())
                    print(output['text'])
                    if recognizer.Result() != "":
                        from window import inputText
                        inputText(output['text']) 
        
        if stream.is_active():
            stream.stop_stream()
        sleep(0.1)


SetLogLevel(-1)

#model = Model(r"C:\Users\RIC\Desktop\KTANEBot\Keep-Talking-and-Nobody-Explodes-Bot\vosk-model-en-us-0.22-lgraph")
z = threading.Thread(target=listening, daemon=True)
z.start()