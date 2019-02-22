#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys; sys.path.append('.\\modules\\')
import Tkinter as tk

def insert_point():
    var = e.get()
    t.insert('insert',var)

def insert_end():
    var = e.get()
    t.insert('end',var)

def hit_me():
    global on_hit
    if on_hit == False:     # 从 False 状态变成 True 状态
        on_hit = True
        var.set('you hit me')   # 设置标签的文字为 'you hit me'
    else:       # 从 True 状态变成 False 状态
        on_hit = False
        var.set('') # 设置 文字为空

on_hit = False  # 默认初始状态为 False

window = tk.Tk()
window.title('my window')

##窗口尺寸
window.geometry('400x400')

var = tk.StringVar()    # 这时文字变量储存器
l = tk.Label(window,
    textvariable=var,   # 使用 textvariable 替换 text, 因为这个可以变化
    font=('Arial', 12), width=40, height=15)
l.pack()

b = tk.Button(window,
    text='hit me',      # 显示在按钮上的文字
    width=15, height=2,
    command=hit_me)     # 点击按钮式执行的命令
b.pack()    # 按钮位置

b1 = tk.Button(window,text="insert point",width=15,height=2,command=insert_point)
b1.pack()

b2 = tk.Button(window,text="insert end",command=insert_end)
b2.pack()

e = tk.Entry(window,show='*')
e.pack()

t = tk.Text(window,height=2)
t.pack()

##显示出来
window.mainloop()
