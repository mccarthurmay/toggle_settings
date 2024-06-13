import subprocess

def toggle_hdr(enable):
    if enable:
        command = "Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\VideoSettings' -Name 'EnableHDR' -Value 1"
    else:
        command = "Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\VideoSettings' -Name 'EnableHDR' -Value 0
    
    subprocess.run(command, shell = True)


command = "Restart-Service -Name 'DisplayEnhancementService'"

def hertz(enable):
    if enable:
        command = ""
    else:
        command = ""
    subprocess.run(command, shell = True)

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

def education():
    #HDR off
    #60HZ
    #turn down quality in battery
    #whisper fan
    #turn on target mode in asus settings

def quality():
    #HDR on
    #120HZ
    #turn up quality in battery
    #standard fan

def performance():
    #HDR off
    #60HZ
    #turn down quality in battery
    #performance fan