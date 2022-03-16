import pyttsx3
import threading
import pyaudio
from vosk import Model, KaldiRecognizer, SetLogLevel
from time import sleep
import json
import moduleManager

isActive = False
isTalking = False
doNotStartSpeak = False

def toggleActive():
    global isActive
    global doNotStartSpeak

    if doNotStartSpeak == False:
        if isActive == False:
            isActive = True
            x = threading.Thread(target=speak, args=("I am active.",), daemon=True)
            x.start()


        elif isActive == True:
            isActive = False
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
    model = Model(r"vosk-model-en-us-0.22")
    recognizer = KaldiRecognizer(model, 16000)

    from window import inputText
    inputText("Ready to listen!")

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
                        if output['text'] != "" and output['text'] != " " and output['text'] != "the":
                            inputText(output['text']) 
                        if output['text'] != "" and output['text'] != "the":
                            x = threading.Thread(target=speak, args=(moduleManager.redirectInformation(output['text'])[1],))
                            x.start()
                        
        if stream.is_active():
            stream.stop_stream()
        sleep(0.1)


#SetLogLevel(-1)

z = threading.Thread(target=listening, daemon=True)
z.start()