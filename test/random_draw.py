# coding=utf8

import pgzrun
import random

WIDTH=1200
HEIGHT=800
R=100
def draw():
    screen.fill('white')
    for x in range(R, WIDTH, 2*R):
        for y in range(R, HEIGHT, 2*R):
            for r in range(1, R, 10):
                _R = random.randint(0, 255)
                _G = random.randint(0, 255)
                _B = random.randint(0, 255)
                screen.draw.filled_circle((x, y), R-r, (_R, _G, _B))
    
def on_mouse_down():
    draw()

pgzrun.go()