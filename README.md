# README

（1.0版本）

## 文件列表_20230407

    C:\Users\ZF\PycharmProjects\pythonProject\air_IRcontrol 的目录
    
    2023/04/11  16:32    <DIR>          .idea
    2023/04/03  16:43    <DIR>          Arduino_代码
    2023/04/11  16:32    <DIR>          For_control_computer
    2023/03/26  00:04               188 indicator_control.py
    2019/08/01  20:55            46,413 NirCmd.chm
    2019/08/01  20:53           119,296 nircmd.exe
    2019/08/01  20:53           117,248 nircmdc.exe
    2023/04/03  17:04               813 path_identify.py
    2023/04/11  16:32                 0 README.md
    2023/04/03  23:50             1,058 run_tcp.py
    2023/04/03  23:58               186 run_tcp.vbs
    2023/03/26  00:26               322 send_serial.py
    2023/04/04  00:00             2,579 Tcp_connect.lnk
    2023/04/11  16:30             1,221 tcp_connect.py
    2023/04/04  01:32               961 txt2voice.py
    2023/04/04  01:33    <DIR>          __pycache__
                  12 个文件        290,285 字节

### python文件

目录包含以下6个python文件：

    2023/03/26  00:04               188 indicator_control.py
    2023/04/03  17:04               813 path_identify.py
    2023/04/03  23:50             1,058 run_tcp.py
    2023/03/26  00:26               322 send_serial.py
    2023/04/11  16:30             1,221 tcp_connect.py
    2023/04/04  01:32               961 txt2voice.py

#### 1. indicator_control

用于控制显示器的息屏等，注意不是关闭显示器。

#### 2. path_identify

用于解析每个网址附带的请求应该分别对应什么指令。

    def path_switch(path):
        if(path=='/poweron'):
            print('try poweron')
            ss.poweron()
            print('poweron has finished!')

其中`ss`是调用了`send_serial`函数来实现红外信号的发射。

项目里一般`import path_identify as pif`。

#### 3. run_tcp

用于运行`tcp_connect`，同时在右下角生成一个系统小图标。

小图标可以右键关闭和选择相关指令，当前是直接调用`path_identify`来进行控制的，如：

```
def poweron_action(icon, item):
    pif.ss.poweron();
```

#### 4. send_serial

用于给Arduino发送串口信号，来控制发射目标红外信号。

#### 5. tcp_connect

核心的文件，用于获取网页请求。

```
#http://192.168.15.221:8000/command
```

获取请求后在`path_identify`处理请求。

#### 6. txt2voice

调用`pyttsx3`实现简单的文本转语音功能。



### 其他文件

    2019/08/01  20:55            46,413 NirCmd.chm
    2019/08/01  20:53           119,296 nircmd.exe
    2019/08/01  20:53           117,248 nircmdc.exe
    2023/04/11  16:53             2,679 README.md
    2023/04/03  23:58               186 run_tcp.vbs
    2023/04/04  00:00             2,579 Tcp_connect.lnk
    2023/04/11  16:32    <DIR>          For_control_computer

#### 1. NirCmd.chm & nircmd.exe & nircmdc.exe

用于控制显示器的息屏等。

#### 2. README.md

正是本文。

#### 3. run_tcp.vbs

用来快速运行`run_tcp.py`，并可以生成快捷方式，将快捷方式放到开机自启栏。

#### 4.Tcp_connect.lnk

生成的快捷方式。

#### 5. For_control_computer

这是一个文件夹，以下是文件夹里的内容：

    2023/04/04  01:40    <DIR>          build
    2023/04/04  01:40    <DIR>          dist
    2023/04/04  01:36               924 Let's.spec
    2023/04/04  01:59               957 Let_control.py
    2023/04/04  01:40               917 Let_control.spec
                   3 个文件          2,798 字节

作用是：可以部署在别的电脑上，通过系统小托盘来控制空调等。

和`run_tcp`生成小图标的方法相同，只是指令的执行从直接调用`path_identify`函数，变成了发送网址请求。

这意味着需要主控电脑，运行着`tcp_connect`代码。

dist目录下包含了`Let_control.exe`，这是利用以下代码生成的：

    pyinstaller --onefile --noconsole --add-data "C:\Users\ZF\Pictures\icon\fhb.ico;icon" Let_control.py

`Let_control.exe`可以直接复制到其他电脑上运行。

