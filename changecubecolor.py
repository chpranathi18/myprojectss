from ursina import *

app = Ursina()

cube = Entity(model='cube', color=color.white, scale=2)

colors = [color.red, color.green, color.blue, color.yellow, color.orange]
color_index = 0

def change_color():
    global color_index
    cube.color = colors[color_index]
    color_index = (color_index + 1) % len(colors)

def input(key):
    if key == 'left mouse down' and mouse.hovered_entity == cube:
        change_color()
    elif key == 'c':
        change_color()

app.run()