import pyautogui
import time
sleeptime = float(input('Please Enter Sleep time: '))
print('')
while sleeptime == 0 or sleeptime < 0.5:
    sleeptime = float(input('Please Enter Sleep time(more than or equal to 0.5): '))
    print('')
if sleeptime < 1:
    print('OK Sir, I will move your mouse after every', sleeptime*60, 'seconds')
elif sleeptime == 1:
    print('OK Sir, I will move your mouse after every', sleeptime, 'minute')
else:
    print('OK Sir, I will move your mouse after every', sleeptime, 'minutes')
while True:
    time.sleep(sleeptime*60)
    for i in range(50, 100):
        pyautogui.moveTo(250, i*5)