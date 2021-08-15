# coding=utf8

import pgzrun

def draw():
    screen.fill('white')
    color = 'black'
    for r in range(256, 0, -1):
        screen.draw.filled_circle((400, 300), r, (256-r, 0, 0))

pgzrun.go()