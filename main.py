import pyglet
from pyglet.window import mouse
from pyglet import clock

from drawings import *
from utils import *

import numpy as np
from random import *
import time
import globals
globals.init()


Q_init_val = 0.6
# ---------- Q MATRIX - EXPLORATION {[board state]:reward]} ----------------
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

# ------------------ IF GAME OVER, RESET -------------------------
def Reset():
    globals.board = np.full((globals.n,globals.n), -1, dtype=int)
    globals.turn = 0
    globals.States = []
    globals.on_board_tokens = []
    globals.tokens_patch = pyglet.graphics.Batch()
    globals.tokens_patch2 = pyglet.graphics.Batch()
    #stop_game()


# ------------------- REWARD ROUTINE -----------------------------
# States = ['[-1,1,...,0,-1]','[-1,1,...,0,-1]']
# V(St) += alpha(V(St+1)-V(S))
def Reward(reward):
    States = reversed(globals.States)
    for state in States:
        if Q.get(state) is None:
            Q[state] = Q_init_val
        Q[state] = Q[state] + 0.2 * (globals.gamma * reward - Q[state])
        reward = Q[state]


# ------------------------------------------------------
# For NPC actions, we have two cases, 30% move 
# randomly and 70% by studying the enviroment
#------------------------- AI PLAYER --------------------------------

def NPC_move_AI():
    # ----------------- 30% actions ---------------------

    #if globals.cont == 1:
    if np.random.uniform(0,1) <= globals.exp_rate:
        i,j = randint(0,9),randint(0,9)
        while not (is_legal_move(i, j)):
            x = randint(globals.board_start_x,globals.board_end_x)
            y = randint(globals.board_start_y,globals.board_end_y)
            i,j = calculate_cells(x,y)
        print("PRIMERA PARTE   i: %d j: %d" %(i,j))

    # ------------------ 70% actions ---------------------
    else:
        Max_value = -999

        for m in range(globals.n):
            for n in range(globals.n):
                next_board = globals.board.copy() # to analyze if the next move is the best
                next_board[m][n] = globals.turn
                next_board_str =  str(next_board.reshape(-1))
                value = 0 if Q.get(next_board_str) is None else Q.get(next_board_str)
                
                #print("value: ",value)
                if is_legal_move(m,n) and value >= Max_value: 
                    Max_value = value
                    i,j = m,n
    
        print("SEGUNDA PARTE    i: %d j: %d" %(i,j))

    if (is_legal_move(i, j)):
        print(globals.turn,globals.tokens[globals.turn])
        token_activate(globals.tokens[globals.turn], j, i)
        globals.board[i][j] = globals.turn
        state = str(globals.board.reshape(-1))
        globals.States.append(state)
        result = check_win(i,j,Q)
        if result is not None:
            if result == 1: # "Won X"
                Reward(1)        
            elif result == 0: # "Won O"
                Reward(0)          
            else:             # "Draw"
                Reward(0.2)
            for key in Q:
                print( key ," : ",Q[key])    

            state = None
            return True
        else:
            return False
        #globals.cont -=1
        # board[i][j] += gamma * max ------ quizas aqui tmbn...

# -------------------------- BOT PLAYER -----------------------------------

def BOT_move():
    # ----------------- 30% actions ---------------------

    if np.random.uniform(0,1) <= globals.exp_rate:
        i,j = 0,0
        while not (is_legal_move(i, j)):
            x = randint(globals.board_start_x,globals.board_end_x)
            y = randint(globals.board_start_y,globals.board_end_y)
            i,j = calculate_cells(x,y)

    # ------------------ 70% actions ---------------------
    else:
        Max_value = -999
        
        for m in range(globals.n):
            for n in range(globals.n):
                next_board = globals.board.copy() # to analyze if the next move is the best
                next_board[m][n] = globals.turn
                next_board_str =  str(next_board.reshape(-1))
                value = 0 if Q.get(next_board_str) is None else Q.get(next_board_str)
                
                #print("value: ",value)
                if value >= Max_value: 
                    Max_value = value
                    i,j = m,n

    if (is_legal_move(i, j)):
        
        token_activate(globals.tokens[globals.turn], j, i)
        globals.board[i][j] = globals.turn
        state2 = str(globals.board.reshape(-1))
        globals.States2.append(state2)
        result = check_win(i,j,Q)
        if result is not None:
            if result == 1: # "Won X"
                Reward(1)       
                globals.States2 = []
            elif result == 0: # "Won O"
                Reward(0)          
                globals.States2 = []
            else:             # "Draw"
                Reward(0.5)
                globals.States2 = []
                
            Reset()
            state2 = None

        change_turn()
        
        turn_redraw(label2)

# --------------------------  AI VS BOT -------------------------------
def AI_BOT():
    NPC_move_AI() if globals.turn == 0 else BOT_move()    


# ------------------------- GRAFICO RESULTADO DE CADA GAME -------------------------
def callback_bot(dt):
    print("No lee el NPC")
    exit = NPC_move_AI()
    print("Leyó el NPC")    
    change_turn()
    turn_redraw(label2)
    print("------- Next Turn -----------")
    print(globals.turn)
    if(exit):
        Reset()
# -----------------------------------------------------------------------------

# ------------------------- GRAFICO RESULTADO DE CADA GAME -------------------------
# def AI_vs_BOT ():
#     gamebacth = pyglet.graphics.Batch()
#     AI_BOT()
#     gamebacth.draw()

#---EVENTOS---
#--------------------------------------------
@window.event
def on_draw():
    window.clear()
    background_draw()
    cells_redraw()
    cells_redraw2()
    main_label.draw()
    label2.draw()



# ----------------------- HUMAN TURN ------------------------------------

@window.event
#class GameEventHandler:
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        if (globals.board_start_x<x<globals.board_end_x) and (globals.board_start_y<y<globals.board_end_y) and (globals.turn==0):
            i,j = calculate_cells(x,y)
            if (is_legal_move(i, j)):
                token_activate(globals.tokens[globals.turn], j, i)
                globals.board[i][j] = globals.turn
                if check_win(i,j,Q) is not None:
                    for key in Q:
                        print( key ," : ",Q[key])    
                    Reset()
                else:
                    change_turn()
                    turn_redraw(label2)
                    print("------- Next Turn -----------")
                #print(globals.turn,globals.tokens[globals.turn])
                #print(globals.turn,globals.tokens[globals.turn])
                    clock.schedule_once(callback_bot, 0.5)  
                #window.clear() # NOSE COMO LIMPIAR LA PANTALLA PARA LA NUEVA PARTIDA
                #globals.cont += 1   # To change turns btw NPC and PLayer
                
        #print(globals.board)
#game_handler = GameEventHandler()

# def start_game():
#     window.push_handlers(game_handler)

# def stop_game():
#     window.pop_handlers()    
    #    @window.event
            
#--------------------------------------------

pyglet.app.run()
