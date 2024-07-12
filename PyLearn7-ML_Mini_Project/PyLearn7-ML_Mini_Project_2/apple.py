import random
import arcade

class Apple(arcade.Sprite):
    def __init__(self,game):
        super().__init__("pics/apple.png")

        self.width = 32
        self.height = 32
        self.center_x = random.randint(16, game.width-16) // 8 * 8   #x becomes a multiple of 8
        self.center_y = random.randint(16, game.height-16) // 8 * 8  #y becomes a multiple of 8
        self.score = 1