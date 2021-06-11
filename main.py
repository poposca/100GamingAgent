import pyglet
from pyglet import shapes

background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)


def background_draw():
    mybatch = pyglet.graphics.Batch()

    width = 2    
    color = (200, 200, 200)

    vertical_lines = []
    horizontal_lines = []

    for i in range(11):
        # Vertical Line
        vco_x1 = 80 + (64*i)
        vco_y1 = 580
        vco_x2 = 80 + (64*i)
        vco_y2 = 60
        # Hotizontal Line
        hco_x1 = 80
        hco_y1 = 60 + (52*i)
        hco_x2 = 720
        hco_y2 = 60 + (52*i)
         
        # creating a line
        horizontal_lines.append(shapes.Line(vco_x1, vco_y1, vco_x2, vco_y2, width, color = color, batch = mybatch, group=background)) 
        horizontal_lines[-1].opacity = 222

        horizontal_lines.append(shapes.Line(hco_x1, hco_y1, hco_x2, hco_y2, width, color = color, batch = mybatch, group=background)) 
        horizontal_lines[-1].opacity = 222
     
    mybatch.draw()


def tokens_draw():
    mybatch2 = pyglet.graphics.Batch()
    label1 = pyglet.text.Label('X',
                              font_name='Noto Sans',
                              font_size=24,
                              x=80+32+(64*(1-1)), y=60+28+(52*(1-1)),
                              anchor_x='center', anchor_y='center',
                              batch=mybatch2, group=foreground)
    label2 = pyglet.text.Label('O',
                                font_name='Noto Sans',
                                font_size=24,
                                x=80+32+(64*(3-1)), y=60+28+(52*(4-1)),
                                anchor_x='center', anchor_y='center',
                                batch=mybatch2, group=foreground)
    mybatch2.draw()


window = pyglet.window.Window(800, 600, "10x10 Tic Tac Toe")
pyglet.gl.glClearColor(0.1,0.1,0.14,1)

@window.event
def on_draw():
    window.clear()
    background_draw()
    tokens_draw()

pyglet.app.run()
