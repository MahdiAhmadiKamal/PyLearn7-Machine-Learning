from math import sqrt
import arcade


class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 32
        self.height = 32
        self.center_x = game.width//2
        self.center_y = game.height//2
        self.color = arcade.color.DARK_GREEN
        self.color2 = arcade.color.ORANGE
        self.change_x = 0
        self.change_y = 0
        self.speed = 8
        self.score = 0
        self.body = []

    def draw(self):
            arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
        
            for part in self.body:
                if self.body.index(part)%2==0:
                    arcade.draw_rectangle_filled(part['x'], part['y'], self.width, self.height, self.color)
                elif self.body.index(part)%2!=0:
                    arcade.draw_rectangle_filled(part['x'], part['y'], self.width, self.height, self.color2)
            
    def move(self):
        self.body.append({'x': self.center_x, 'y': self.center_y})

        if len(self.body)> self.score:
            self.body.pop(0)

        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
        

    def move_ai(self, apple):
        self.body.append({'x': self.center_x, 'y': self.center_y})

        if len(self.body)> self.score:
            self.body.pop(0)


        if self.center_x < apple.center_x:
            self.center_x += 1 * self.speed
        if self.center_y < apple.center_y:
            self.center_y += 1 * self.speed
        if self.center_x > apple.center_x:
            self.center_x -= 1 * self.speed
        if self.center_y > apple.center_y:
            self.center_y -= 1 * self.speed

    def eat(self, food):
        self.score += food.score

        del food