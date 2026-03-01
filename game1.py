import pyxel

class Player:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.w, self.h = 5, 5
        self.speed = 2

    def update(self):
        next_x, next_y = self.x, self.y
        if pyxel.btn(pyxel.KEY_LEFT or pyxel.KEY_A): next_x -= self.speed
        if pyxel.btn(pyxel.KEY_RIGHT or pyxel.KEY_D): next_x += self.speed
        if pyxel.btn(pyxel.KEY_UP or pyxel.KEY_W): next_y -= self.speed
        if pyxel.btn(pyxel.KEY_DOWN or pyxel.KEY_S): next_y += self.speed
        #if pyxel.btn(pyxel.KEY_):

#def __init__(self):
#    pyxel.init(128, 128, title = "Sample Game")
#    pyxel.load("game1.pyxres")
    