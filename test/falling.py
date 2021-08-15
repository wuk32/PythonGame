# coding=utf8

import pgzrun

y = 100
speed = 3
def draw():
    screen.fill('white')
    screen.draw.filled_circle((400, y), 30, 'red')

def update():
    global y, speed
    y = y + speed
    if y >= 570 or y <= 30:
        speed = -speed

pgzrun.go()