from math import sqrt
import numpy as np
import pandas as pd
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

    def move_generate_dataset(self, apple, data):
        self.body.append({'x': self.center_x, 'y': self.center_y})

        if len(self.body)> self.score:
            self.body.pop(0)


        if self.center_x < apple.center_x:
            self.center_x += 1 * self.speed
            data['direction'] = 1
        if self.center_y < apple.center_y:
            self.center_y += 1 * self.speed
            data['direction'] = 0
        if self.center_x > apple.center_x:
            self.center_x -= 1 * self.speed
            data['direction'] = 3
        if self.center_y > apple.center_y:
            self.center_y -= 1 * self.speed
            data['direction'] = 2

    def move_ml(self, apple, game):
        data = {'wu': None,
                'wr': None,
                'wd': None,
                'wl': None,
                'au': None,
                'ar': None,
                'ad': None,
                'al': None,
                'bu': None,
                'br': None,
                'bd': None,
                'bl': None}

        # The distance between the snake and the apple
        if self.center_x == apple.center_x and self.center_y < apple.center_y:
            data['au'] = 1
            data['ar'] = 0
            data['ad'] = 0
            data['al'] = 0
        elif self.center_x == apple.center_x and self.center_y > apple.center_y:
            data['au'] = 0
            data['ar'] = 0
            data['ad'] = 1
            data['al'] = 0
        elif self.center_x < apple.center_x and self.center_y == apple.center_y:
            data['au'] = 0
            data['ar'] = 1
            data['ad'] = 0
            data['al'] = 0
        elif self.center_x > apple.center_x and self.center_y == apple.center_y:
            data['au'] = 0
            data['ar'] = 0
            data['ad'] = 0
            data['al'] = 1

        # The distance between the snake and the walls
        data['wu'] = self.height - self.center_y
        data['wr'] = self.width - self.center_x
        data['wd'] = self.center_y
        data['wl'] = self.center_x

        # The distance between the snake and its body
        for part in self.body:
            if self.center_x == part['x'] and self.center_y < part['y']:
                data['bu'] = 1
                data['br'] = 0
                data['bd'] = 0
                data['bl'] = 0
            elif self.center_x == part['x'] and self.center_y > part['y']:
                data['bu'] = 0
                data['br'] = 0
                data['bd'] = 1
                data['bl'] = 0
            elif self.center_x < part['x'] and self.center_y == part['y']:
                data['bu'] = 0
                data['br'] = 1
                data['bd'] = 0
                data['bl'] = 0
            elif self.center_x > part['x'] and self.center_y == part['y']:
                data['bu'] = 0
                data['br'] = 0
                data['bd'] = 0
                data['bl'] = 1
                
        data = pd.DataFrame(data, index=[1])
        data.to_csv('d1.csv', index=False)
        data.fillna(0, inplace=True)

        data.to_csv('d2.csv', index=False)

        data = np.array(data)
        output = game.model.predict(data)
        direction = output.argmax()
        if direction == 0:
            self.change_x = 0
            self.change_y = 1
        elif direction == 1:
            self.change_x = 1
            self.change_y = 0
        elif direction == 2:
            self.change_x = 0
            self.change_y = -1
        elif direction == 3:
            self.change_x = -1
            self.change_y = 0

    def eat(self, food):
        self.score += food.score

        del food