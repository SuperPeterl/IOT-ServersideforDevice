import os
import requests
import time
def process_request():
    response = requests.get('http://localhost:8000/listen')
    res = [int(x) for x in response.text.split(',')]
    for o in res:
        if o == 1:
            # Execute the command to turn off the computer
            #os.system('shutdown /s /t 5')
            print("Computer is shutting down...")
        else:
            print("noting")


while True :
    try :
        time.sleep(5)
        process_request()
    except:
        print("error")