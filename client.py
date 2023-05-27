import os
import requests
import time
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def process_request():
    response = requests.get('http://20.219.16.119:8000/listen')
    print(response.text)
    if response.text == '':
        return 
    res = [int(x) for x in response.text.split(',')]
    for o in res:
        if o == 1:
            shutdown()
        if o == 2:
            volumemanager(1)
        if o == 3:
            volumemanager(0)
        else:
            print("noting")

def shutdown():
    # Execute the command to turn off the computer
            l = list(range(5,-1,-1))
            for i in l:
                print(f'computer is shutting down in {i}')
                time.sleep(1)
            os.system('shutdown /s /t 0')
            print("Computer is shutting down...")

def volumemanager(do):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    vmin,vnor,vmax = volume.GetVolumeRange()
    vnow = volume.GetMasterVolumeLevel()
    volume.SetMasterVolumeLevel(vnow+5, None)
    print("volume.GetMasterVolumeLevel(): %s" % volume.GetMasterVolumeLevel())
    if do :
        if vnow+5 > 0:
            volume.SetMasterVolumeLevel(0, None)
        else:
            volume.SetMasterVolumeLevel(vnow+a, None)
    else :
        if vnow -5 < -65.25:
            volume.SetMasterVolumeLevel(-65.25, None)
        else:
            volume.SetMasterVolumeLevel(vnow-5, None)



print("start now")
while True :
    try :
        time.sleep(5)
        process_request()
        
    except Exception as e:
        print(e)