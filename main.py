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
    pag.click(300, 315)
    time.sleep(0.25)
    pag.typewrite('HDR')
    time.sleep(2)
    pag.press('enter')
    time.sleep(1)
    pag.press('enter')
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
            time.sleep(1)
            pag.click(2600,922)
    else:   #HDR on, want to disable
        if toggled_on:
            time.sleep(1)
            pag.click()




def hertz(enable):
    #navigate to hertz
    
    pag.click(300,315)
    time.sleep(0.25)
    pag.typewrite('display')
    time.sleep(1)
    pag.click(304,375)
    time.sleep(0.75)
    pag.click(1370,1675)
    time.sleep(0.5)
    pag.click(2582,1130)
    if enable:
        pag.press('up')
    else:
        pag.press('down')
    pag.press('enter')
    time.sleep(3)
    pag.press('tab')
    pag.press('enter')


def battery(level):  
    pag.click(300,315)
    pag.typewrite('battery')
    pag.press('enter')
    time.sleep(.5)
    pag.press('enter')
    time.sleep(1)
    pag.click(2500, 1060)

    if level == "power":
        pag.press('up')
        pag.press('up')
        pag.press('enter')

    elif level == "performance":
        pag.press('down')
        pag.press('down')
        pag.press('enter')
    else:
        pag.press('down')
        pag.press('down')
        pag.press('up')
        pag.press('enter')




def fan(level):
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
    OpenSettings()
    hdr(True)
    hertz(True)
    battery('power')
    #whisper fan
    pass

def education():
    OpenSettings()
    hdr(False)
    hertz(False)
    battery('power')
    #whisper fan
    #turn on target mode in asus settings (power)
    pass

def quality():
    OpenSettings()
    hdr(True)
    hertz(True)
    battery('balanced')
    #standard fan
    pass

def performance():
    OpenSettings()
    hdr(False)
    hertz(False)
    battery('performance')
    #performance fan 
    pass    


education()