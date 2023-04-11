# 导入pyttsx3库
import pyttsx3

def speak_shdlh():
    # 创建一个pyttsx3引擎对象
    engine = pyttsx3.init()

    # 设置使用的语音合成引擎为中文
    engine.setProperty('voice', 'zh')

    # 获取当前使用的语音合成引擎的可用音色列表
    voices = engine.getProperty('voices')

    # 设置要使用的音色（这里假设我们使用列表中的第一个音色，您可以自行选择其他音色）
    engine.setProperty('voice', voices[0].id)

    # 获取当前语音合成的速度
    rate = engine.getProperty('rate')

    # 设置新的语音合成速度（这里将速度增加50%，您可以自行设置其他数值）
    engine.setProperty('rate', rate * 0.7)

    # 要转换为语音的文本
    text = "上山打老虎！老虎打不到，打到小松鼠！"

    # 使用引擎对象将文本转换为语音
    engine.say(text)

    # 播放语音
    engine.runAndWait()