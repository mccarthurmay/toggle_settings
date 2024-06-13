import subprocess
import win32gui
import win32con
import pyautogui as pag
import time

#open Settings
pag.press('win') 
pag.typewrite('settings') 
pag.press('enter')
hwnd = win32gui.FindWindow(None, "Settings")
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
try:
    win32gui.SetForegroundWindow(hwnd)
except:
    pass
pag.click()
time.sleep(2)

def hdr(enable):
    #navigate to HDR
    pag.moveTo(300, 315, 0.5)
    pag.click()
    pag.typewrite('HDR')
    time.sleep(2)
    pag.press('enter')

    #toggle HDR
    pag.moveTo(2603, 790, 0.5)
    pag.click()
    time.sleep(1)
    pag.click()



def hertz(enable):
    #navigate to hertz
    pag.moveTo(300,315,0.5)
    pag.click()
    pag.typewrite('display')
    time.sleep(1)
    pag.press('enter')

    
        


def battery(enable):  
    if enable:
        command = ""
    else:
        command = ""
    subprocess.run(command, shell = True)

def fan(enable):
    if enable:
        command = ""
    else:
        command = ""
    subprocess.run(command, shell = True)

def target_mode(enable):
    if enable:
        command = ""
    else:
        command = ""
    subprocess.run(command, shell = True)

def video():
    #HDR on
    #120HZ
    #turn up quality in battery
    #whisper fan
    pass

def education():
    #HDR off
    #60HZ
    #turn down quality in battery
    #whisper fan
    #turn on target mode in asus settings
    pass

def quality():
    #HDR on
    #120HZ
    #turn up quality in battery
    #standard fan
    pass

def performance():
    #HDR off
    #60HZ
    #turn down quality in battery
    #performance fan
    pass    