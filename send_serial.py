import serial
import time

def poweron():
    # 打开串口，使用默认参数
    ser = serial.Serial('COM5', 9600, timeout=1)
    time.sleep(2)
    ser.write(b'a')
    time.sleep(1)

def poweroff():
    ser = serial.Serial('COM5', 9600, timeout=1)
    time.sleep(2)
    ser.write(b'b')
    time.sleep(1)