import pyglet
from pyglet import shapes
from pyglet import clock
from pyglet.window import mouse

background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)

turn = 1

def change_turn():
    global turn
    turn = turn ^ 1
    
    return turn

def background_draw():
    mybatch = pyglet.graphics.Batch()

    width = 2    
    color = (200, 200, 200)

    vertical_lines = []
    horizontal_lines = []

    for i in range(11):
        # Vertical Line
        vco_x1 = 80 + (64*i);       vco_x2 = 80 + (64*i)
        vco_y1 = 580;               vco_y2 = 60
        
        # Hotizontal Line
        hco_x1 = 80;                hco_x2 = 720
        hco_y1 = 60 + (52*i);       hco_y2 = 60 + (52*i)
        
        # creating a line
        horizontal_lines.append(shapes.Line(vco_x1, vco_y1, vco_x2, vco_y2, width, color = color, batch = mybatch, group=background)) 
        horizontal_lines[-1].opacity = 222

        horizontal_lines.append(shapes.Line(hco_x1, hco_y1, hco_x2, hco_y2, width, color = color, batch = mybatch, group=background)) 
        horizontal_lines[-1].opacity = 222
     
    mybatch.draw()


def token_draw(char :str, board_posx :int, board_posy :int):
    label1 = pyglet.text.Label(char,
                              font_name='Noto Sans',
                              font_size=24,
                              x=80+32+(64*board_posx), y=60+28+(52*board_posy),
                              anchor_x='center', anchor_y='center', group=foreground)
    label1.draw()

def turn_redraw(turnlabel, turn ):
    if (turn == 0):
        char = 'O'
    elif (turn == 1):
        char = 'X'

    turnlabel.text = char


window = pyglet.window.Window(800, 600, "10x10 Tic Tac Toe")
pyglet.gl.glClearColor(0.1,0.1,0.14,1)

main_label = pyglet.text.Label('TURN: ',
                          font_name='Noto Sans',
                          font_size=16,
                          x=(window.width//2 -32), y=24,
                          anchor_x='center', anchor_y='center', group=background)
                          
label2 = pyglet.text.Label('O',
                              font_name='Noto Sans',
                              font_size=16,
                              x=(window.width//2 + 8), y=24,
                              anchor_x='center', anchor_y='center', group=foreground)

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

pyglet.app.run()
