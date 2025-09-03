import pyglet

window = pyglet.window.Window(width=800, height=600, caption='Pyglet Example')

@window.event
def on_draw():
    window.clear()

pyglet.app.run()
