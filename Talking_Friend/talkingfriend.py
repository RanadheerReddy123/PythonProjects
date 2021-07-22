import pyttsx3
vtf = pyttsx3.init()
rate = vtf.getProperty("rate")
vtf.setProperty("rate", 140)
def vtf_speak(text):
    print("Speaking..........")
    vtf.say(text)
    vtf.runAndWait()
txt = "Hello RR-Web Developers, Subscriber"
vtf_speak(txt)
while txt!= 'bye':
    txt = input("What should I say: ")
    txt = txt.lower()
    if txt!= 'bye':
        vtf_speak(txt)
    else:
        vtf_speak("See you again, this was nice talking to you")
    
