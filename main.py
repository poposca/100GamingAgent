import pyglet
from pyglet.window import mouse
from drawings import *

import globals
globals.init()

def change_turn():
    globals.turn =  globals.turn ^ 1
    return globals.turn

#Definición de Ventana: Tamaño, nombres y color de fondo
#--------------------------------------------
window = pyglet.window.Window(800, 600, "10x10 Tic Tac Toe")
pyglet.gl.glClearColor(0.12,0.12,0.16,1)
#--------------------------------------------

#Objetos de texto para mostrar turno actual
#--------------------------------------------
main_label = pyglet.text.Label('TURN: ',
                          font_name='Noto Sans',
                          font_size=16,
                          x=(window.width//2 -32), y=24,
                          anchor_x='center', anchor_y='center', group=globals.background)
                          
label2 = pyglet.text.Label('O',
                              font_name='Noto Sans',
                              font_size=16,
                              x=(window.width//2 + 8), y=24,
                              anchor_x='center', anchor_y='center', group=globals.foreground)
#--------------------------------------------

#---EVENTOS---
#--------------------------------------------
@window.event
def on_draw():
    window.clear()
    background_draw()
    token_draw('X', 1, 1)
    token_draw('O', 3, 5)
    main_label.draw()
    label2.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        turn_redraw(label2, change_turn())
        if (globals.board_start_x<x<globals.board_end_x) and (globals.board_start_y<y<globals.board_end_y):
            print("Clicked inside the board")
            # i,j = calculate_cells(x,y)
#--------------------------------------------

pyglet.app.run()
