import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import datetime as dt
import pywhatkit as pk
listener = sr.Recognizer()
def speak(cmd):
    print("Speaking.........")
    print("")
    tts = gTTS(cmd, lang = "te")
    playsound('audio.mp3')
    os.remove('audio.mp3')
va_name = "త్రిష"
speak("నమస్కారం, నేను మీ త్రిష. మీకు ఏ విదంగా సహాయపడగలను. ")
def take_cmd(check):
    command = ""
    try:
        with sr.Microphone() as source:
            print("Listening......")
            audio = listener.listen(source)
            if check:
                command = listener.recognize_google(audio, language="te")
                if va_name in command:
                    command = command.replace("త్రిష ","")
                     print(command)
                     speak(command)
                else:
                    command = ""
            else:
                command = listener.recognize_google(audio, language="en-US")
    except:
        print("Check your Mic")

    return command
while True:
    final_cmd = take_cmd(True)
    if final_cmd!= "":
        if "టైం" in final_cmd:
            current_time = dt.datetime.now().strftime("%I:%M %p")
            speak(current_time)
        if "యూట్యూబ్" in final_cmd:
            speak("ఏ వీడియో ప్లే చెయ్యాలో చెప్పండి.")
            final_cmd = take_cmd(False)
            pk.playonyt(final_cmd)
            print(final_cmd)
            print("")
            speak("ఆనందించండి. అవసరమైతే మళ్ళీ కాల్ చేయ్యండి.")
            break
        if "గూగుల్" in final_cmd:
            speak("దేని గురించి సెర్చ్ చెయ్యాలో చెప్పండి.")
            final_cmd = take_cmd(False)
            print(final_cmd)
            print("")
            pk.search(final_cmd)
input("Press enter to close.")
