import os
import sys
import subprocess
import pystray
from PIL import Image
from threading import Thread
import path_identify as pif


def run_example_script():
    global tcp_connect_process
    tcp_connect_process = subprocess.Popen(["python", "tcp_connect.py"])


def exit_action(icon, item):
    tcp_connect_process.terminate()
    icon.stop()
    sys.exit(0)


def poweroff_action(icon, item):
    pif.ss.poweroff();

def poweron_action(icon, item):
    pif.ss.poweron();

def create_tray_icon():
    icon_path = r"C:\Users\ZF\Pictures\icon\boji1.png"  # 您的图标文件路径
    image = Image.open(icon_path)

    icon = pystray.Icon("name", image, "Running tcp_connect.py")
    icon.menu = (
        pystray.MenuItem("PowerOff", poweroff_action),
        pystray.MenuItem("PowerOn", poweron_action),
        pystray.MenuItem("Exit", exit_action),
    )
    icon.run()


if __name__ == "__main__":
    example_thread = Thread(target=run_example_script)
    example_thread.start()

    create_tray_icon()
