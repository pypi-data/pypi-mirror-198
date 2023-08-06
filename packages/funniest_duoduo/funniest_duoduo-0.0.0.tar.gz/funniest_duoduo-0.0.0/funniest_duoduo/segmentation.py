# -*- coding: utf-8 -*-

"""
@file    : day1.py
@author  : v_wieszheng
@Data    : 2023/2/9 10:48
@software: PyCharm
"""

import time
from pynput.keyboard import Key, Controller, Listener



# 聊天输入框复制聊天内容，然后按回车发送消息
import pyautogui as pyautogui
import pyperclip




import keyboard  # 监听键盘


class key(object):
    def __init__(self,filename):
        self.filename = filename
        super(key, self).__init__()

    def test_a(self):
        f = open(self.filename, encoding='utf-8')

        for line in f:
            pyperclip.copy(line.strip(''))
            pyautogui.hotkey("ctrl", "v")  # 按下组合键的方法，ctrl+v粘贴
            pyautogui.press("enter")  # 按下按键

    def testing(self):
        keyboard.add_hotkey('f1', self.test_a)
        keyboard.add_hotkey('ctrl+alt', print, args=('b'))
        keyboard.wait()


if __name__ == '__main__':
    # keyboard.add_hotkey('f1', test_a)
    # #按f1输出aaa
    # keyboard.add_hotkey('ctrl+alt', test, args=('b'))
    # #按ctrl+alt输出b
    # keyboard.wait()
    # #wait里也可以设置按键，说明当按到该键时结束
    key = key('txt.txt')
    key.testing()

