import pyxel

WALL_TILES = [(2, 0),(2, 1),(2, 2),(3, 0),(3, 1),(3, 2),(4, 0),(4, 1),(4, 2)]

class Player:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.w, self.h = 5, 5
        self.speed = 2
        self.dest = 0

    def update(self):
        next_x, next_y = self.x, self.y
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A): next_x -= self.speed; self.dest = 0
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D): next_x += self.speed; self.dest = 1
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W): next_y -= self.speed;self.dest = 2
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S): next_y += self.speed; self.dest = 3
        #if pyxel.btn(pyxel.KEY_):
        next_tile_x, next_tile_y = next_x // 8, next_y // 8
        tile = pyxel.tilemap(0).pget(next_tile_x, next_tile_y)

        if tile not in WALL_TILES:
            self.x, self.y = next_x, next_y

    def draw(self):
        muki = [(0, 72),(8, 64),(0, 64),(8, 72)]
        u, v = muki[self.dest]
        pyxel.blt(self.x, self.y, 0, u, v, 8, 8)

class Bullet:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.w, self.h = 5, 5
        self.speed = 5

    #def update(self):


class App:
    def __init__(self):
        pyxel.init(128, 128, title = "Sample Game")
        pyxel.load("game1.pyxres")
        self.player = Player(8, 8)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()
        
    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 20*8, 16*8)
        self.player.draw()

App()