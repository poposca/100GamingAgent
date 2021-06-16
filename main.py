import pyglet
from pyglet.window import mouse
from drawings import *
from math import floor
from random import *
import time

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

#---Utils---
#-------------------------------------------
def calculate_cells(x,y):
    new_x = x - globals.board_start_x
    new_y = y - globals.board_start_y

    j = floor(new_x / globals.cell_size_x)
    i = floor(new_y / globals.cell_size_y)
    
    return i,j

#-------------------------------------------
# Nota: Inicializar un diccionario vacio (state : reward_array), tipo json
# Cargar un archivo que contenga los estados del tablero despues de la exploracion
# En caso de no existir el archivo, generar uno mediante la exploracion.
#-------------------------------------------
# # append a hash state
# def addState(self, state):
#     self.states.append(state)

# # at the end of game, backpropagate and update states value
# def feedReward(self, reward):
#     for st in reversed(self.states):
#         if self.states_value.get(st) is None:
#             self.states_value[st] = 0
#         self.states_value[st] += self.lr * (self.decay_gamma * reward - self.states_value[st])
#         reward = self.states_value[st]


def NPC_turn():

    if globals.cont == 1:
        i,j = 0,0
        while globals.board[i][j] != -1:
            x = randint(globals.board_start_x,globals.board_end_x)
            y = randint(globals.board_start_y,globals.board_end_y)
            i,j = calculate_cells(x,y)
        
        if (globals.board[i][j] == -1):
            token_activate(globals.tokens[globals.turn], j, i)
            globals.board[i][j] = globals.turn
            change_turn()
            turn_redraw(label2)
            globals.cont -=1


#---EVENTOS---
#--------------------------------------------
@window.event
def on_draw():
    window.clear()
    background_draw()
    cells_redraw()
    time.sleep(1) # ------------------------ delay
    cells_redraw2()
    main_label.draw()
    label2.draw()



@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        if (globals.board_start_x<x<globals.board_end_x) and (globals.board_start_y<y<globals.board_end_y):
            i,j = calculate_cells(x,y)
            if (globals.board[i][j] == -1):
                token_activate(globals.tokens[globals.turn], j, i)
                globals.board[i][j] = globals.turn
                change_turn()
                turn_redraw(label2)
                globals.cont += 1   # To change turns btw NPC and PLayer
                NPC_turn()
                
        #print(globals.board)

#    @window.event
           
#--------------------------------------------

pyglet.app.run()
