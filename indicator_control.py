import os
import time

def indicator_off():
    os.system("nircmd.exe monitor off")
    time.sleep(1)

def indicator_on():
    os.system("nircmd.exe monitor on")
    time.sleep(1)