import os
import sys
import time
import subprocess
from threading import Thread
from PIL import Image
import pystray
import requests

icon_path = os.path.join(sys._MEIPASS, "icon", "fhb.ico")
icon_image = Image.open(icon_path)


def exit_action(icon, item):
    icon.stop()

def poweroff_action(icon, item):

    response = requests.get('http://192.168.15.221:8000/poweroff')

def poweron_action(icon, item):
    response = requests.get('http://192.168.15.221:8000/poweron')

def ssdlh_action(icon, item):
    response = requests.get('http://192.168.15.221:8000/12345')

# 创建系统托盘图标和上下文菜单
icon = pystray.Icon("wifi_connect", icon_image, "Let's Control!")
menu = (
    pystray.MenuItem("Power_Off", poweroff_action),
    pystray.MenuItem("Power_On", poweron_action),
    pystray.MenuItem("一二三四五", ssdlh_action),
    pystray.MenuItem("Exit", exit_action),
)
icon.menu = menu

icon.run()