# coding=utf8

import pgzrun

def draw():
    screen.fill('white')
    color = 'black'
    for r in range(100, 10, -10):
        screen.draw.filled_circle((400, 300), r, color)
        color = 'white' if color == "black" else "black"

pgzrun.go()