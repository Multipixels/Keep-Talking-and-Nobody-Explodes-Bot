import speech_recognition as sr
import pyttsx3
import threading
import pyaudio
import pocketsphinx
from time import sleep
import os

isActive = False
isTalking = False
doNotStartSpeak = False

# def listen():
#     global isActive

#     while isActive:
#         print("test")
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             print("Say something!")
#             audio = r.listen(source)

#             try:
#                 # for testing purposes, we're just using the default API key
#                 # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#                 # instead of `r.recognize_google(audio)`
#                 print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
#             except sr.UnknownValueError:
#                 print("Google Speech Recognition could not understand audio")
#             except sr.RequestError as e:
#                 print("Could not request results from Google Speech Recognition service; {0}".format(e))

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

    import window
    window.inputText("wadopakwdp")

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

# this is called from the background thread
# def callback(recognizer, audio):
#     # received audio data, now we'll recognize it using Google Speech Recognition
#     # try:
#     #     # for testing purposes, we're just using the default API key
#     #     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#     #     # instead of `r.recognize_google(audio)`
#     #     print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))
#     # except sr.UnknownValueError:
#     #     print("Google Speech Recognition could not understand audio")
#     # except sr.RequestError as e:
#     #     print("Could not request results from Google Speech Recognition service; {0}".format(e))

    

#     try:
#         print("Sphinx thinks you said " + r.recognize_sphinx(audio))
#     except sr.UnknownValueError:
#         print("Sphinx could not understand audio")
#     except sr.RequestError as e:
#         print("Sphinx error; {0}".format(e))

# r = sr.Recognizer()
# m = sr.Microphone()

# MODELDIR = r"C:\Users\RIC\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pocketsphinx\model"

# print(pocketsphinx.__file__)

# config = pocketsphinx.Decoder.default_config()
# config.set_string('-hmm', os.path.join(MODELDIR, r'en-us'))
# config.set_string('-lm', os.path.join(MODELDIR, r'en-us.lm.bin'))
# config.set_string('-dict', os.path.join(MODELDIR, r'cmudict-en-us.dict'))
# decoder = pocketsphinx.Decoder(config)
# decoder.set_jsgf_file('grammar', "testing.gram")
# decoder.set_search('grammar')

# # with m as source:
# #     r.adjust_for_ambient_noise(source)

# # stop_listening = r.listen_in_background(m, callback)
# # stop_listening(wait_for_stop=False)

# p = pyaudio.PyAudio()
# stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
# stream.start_stream()

# in_speech_bf = False
# decoder.start_utt()
# while True:
#     buf = stream.read(1024)
#     if buf:
#         decoder.process_raw(buf, False, False)
#         if decoder.get_in_speech() != in_speech_bf:
#             in_speech_bf = decoder.get_in_speech()
#             if not in_speech_bf:
#                 decoder.end_utt()

#                 # Print hypothesis and switch search to another mode
#                 print('Result:')

#                 # if decoder.get_search() == 'keyword':
#                 #      decoder.set_search('lm')
#                 # else:
#                 #      decoder.set_search('keyword')

#                 # decoder.start_utt()
#     else:
#         break
# decoder.end_utt()