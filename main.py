import pyglet
from pyglet.window import mouse

from drawings import *
from utils import *

import numpy as np

import globals
globals.init()

Q_init_val = 0.6
Q = {} # Dyctionary with the board state as key and arrays of reward as values

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
    cells_redraw()
    main_label.draw()
    label2.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        if (globals.board_start_x<x<globals.board_end_x) and (globals.board_start_y<y<globals.board_end_y):
            i,j = calculate_cells(x,y)
            if (is_legal_move(i, j)):
                token_activate(globals.tokens[globals.turn], j, i)
                globals.board[i][j] = globals.turn
                check_win(i,j)
                change_turn()
                turn_redraw(label2)
        #print(globals.board)
#--------------------------------------------

pyglet.app.run()
