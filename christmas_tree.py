# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 11:40:43 2022

@author: 啊元
"""# 创建画板
import turtle
screen = turtle.Screen()
screen.setup(800,600) #800是长，宽600
# 画红色圆
circle = turtle.Turtle()
circle.shape('circle')
circle.color('red')
circle.up()#笔画抬起，笔头移动，不划线
circle.goto(0,225)#笔画抬起，笔头移动，不划线
circle.stamp()
# 画绿色方块
square = turtle.Turtle()
square.shape('square')
square.color('green')
square.up()
square.goto(0,200)
square.stamp()
for j in range(1,4):
    for i in range(j*2+1):
        square.up()
        square.goto(-j*40+i*40,170-(j-1)*30)
        square.stamp()
circle.color('pink')
circle.up()
circle.goto(160,110)
circle.stamp()
circle.up()
circle.goto(-160,110)
circle.stamp()
for j in range(1,4):
    for i in range(j*2+1):
        square.up()
        square.goto(-j*40+i*40,80-(j-1)*30)
        square.stamp()
circle.color('orange')
circle.up()
circle.goto(160,20)
circle.stamp()
circle.up()
circle.goto(-160,20)
circle.stamp()
for j in range(1,4):
    for i in range(j*2+1):
        square.up()
        square.goto(-j*40+i*40,-10-(j-1)*30)
        square.stamp()
for i in range(9):
    square.up()
    square.goto(-4*40+i*40,-70)
    square.stamp()
circle.color('red')
circle.up()
circle.goto(200,-70)
circle.stamp()
circle.up()
circle.goto(-200,-70)
circle.stamp()
for i in range(5):
    for j in range(3):
        square.color('brown')
        square.up()
        square.goto(-j*40+40,-100-i*30)
        square.stamp()
# 暂停，点击后退出
turtle.exitonclick()
