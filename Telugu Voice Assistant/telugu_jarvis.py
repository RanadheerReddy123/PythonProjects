import speech_recognition as sr
listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Listening......")
        audio = listener.listen(source)
        text = listener.recognize_google(audio)
        print(text)
except:
    print("Check your Mic")
