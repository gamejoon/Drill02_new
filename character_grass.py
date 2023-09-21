from pico2d import *
import os
import math

open_canvas()

os.chdir("D:\\2DGP\\Drill04")

grass = load_image("grass.png")
character = load_image("character.png")

def run_circle():
    print("CIRCLE")
    
    # 일단 그림을 그려라
    
    cx, cy, r = 400, 300, 200

    for deg in range(0, 360, 5):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
    
        delay(0.01)

def run_rectangle():
    print("RECTANGLE")
    pass

while (True):
    run_circle()
    run_rectangle()
    