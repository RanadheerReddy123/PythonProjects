import pywhatkit
wno = input("Whatsapp Number: ")
msg = input("Message: ")
hr = int(input("Hour(24 hour format): "))
mnt = int(input("Minutes: "))
pywhatkit.sendwhatmsg('+91' +wno, msg, hr, mnt)