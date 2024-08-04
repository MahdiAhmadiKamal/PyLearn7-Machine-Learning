import random
import arcade

class Apple(arcade.Sprite):
    def __init__(self, width, height):
        super().__init__("pics/apple.png")

        self.center_x = random.randint(1, width) //8 * 8  # x becomes a multiple of 8
        self.center_y = random.randint(1, height) //8 * 8 # y becomes a multiple of 8
        self.change_x = 0
        self.change_y = 0
        self.width = 16
        self.height = 16
