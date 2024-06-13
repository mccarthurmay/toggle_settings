import subprocess

def run_command(command):
    subprocess.run(command, shell=True)


def toggle_hdr(enable):
    if enable:
        command = r"powershell -Command Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\MonitorDataStore\SDC416D0_19_07E5_72' -Name 'AdvancedColorEnabled' -Value 1"
        print('1')
        run_command(command)
        nircmd_path = r'C:\Users\mccar\OneDrive\Desktop\toggle_settings\nircmd\nircmd.exe'
        run_command(f'{nircmd_path} monitor off')
        run_command(f'{nircmd_path} monitor on')
    else:
        command = r"powershell -Command Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\MonitorDataStore\SDC416D0_19_07E5_72' -Name 'AdvancedColorEnabled' -Value 0"
        run_command(command)       
        nircmd_path = r'C:\Users\mccar\OneDrive\Desktop\toggle_settings\nircmd\nircmd.exe'
        run_command(f'{nircmd_path} monitor off')
        run_command(f'{nircmd_path} monitor on')    

toggle_hdr(False)



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