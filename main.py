import subprocess
import win32gui
import win32con
import pyautogui as pag
import time
import cv2
import numpy as np

#open Settings
def OpenSettings():
    pag.press('win') 
    time.sleep(1)
    pag.typewrite('settings') 
    time.sleep(1)
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
    pag.moveTo(2603, 790, 0.5)
    pag.click()
    time.sleep(2)

    screenshot = pag.screenshot(region=(1800, 460, 1900, 800))

    #convert image to HSV
    image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2HSV)

    #blue color range
    lower_blue = np.array([90, 100, 100])  
    upper_blue= np.array([170, 255, 255])

    mask = cv2.inRange(image, lower_blue, upper_blue) #identifies pixels within blue color range

    toggled_on = cv2.countNonZero(mask) > 0 #check if blue color exists (white pixels in mask indicate blue)
    
    if enable:  #HDR on, want to enable
        if toggled_on: 
            pass
        else:   #HDR off, want to enable
            pag.moveTo(2600,922)
            time.sleep(1)
            pag.click()
    else:   #HDR on, want to disable
        if toggled_on:
            time.sleep(1)
            pag.click()



def hertz(enable):
    #navigate to hertz
    pag.moveTo(300,315,0.25)
    pag.click()
    pag.typewrite('display')
    pag.moveTo(304,375, 0.5)
    pag.click()
    pag.moveTo(1370,1675, 0.75)
    pag.click()
    pag.moveTo(2582,1130, 0.5)
    pag.click()
    if enable:
        pag.press('up')
    else:
        pag.press('down')
    pag.press('enter')
    time.sleep(3)
    pag.press('tab')
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