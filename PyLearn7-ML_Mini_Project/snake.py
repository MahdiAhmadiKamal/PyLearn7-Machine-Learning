import arcade

class Snake(arcade.Sprite):

    def __init__(self, width, height):
        super().__init__()

        self.speed = 8
        self.center_x = width // 2
        self.center_y = height // 2
        self.change_x = 0
        self.change_y = 0
        self.width = 16
        self.height = 16

        self.color1 = arcade.color.DARK_GREEN
        self.color2 = arcade.color.ORANGE

        self.body = []
        self.body_size = 0

    def draw(self):
            arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
            for part in self.body:
                if self.body.index(part)%2==0:
                    arcade.draw_rectangle_filled(part['center_x'], part['center_y'], self.width, self.height, self.color1)
                elif self.body.index(part)%2!=0:
                    arcade.draw_rectangle_filled(part['center_x'], part['center_y'], self.width, self.height, self.color2)

    def eat(self):
            self.body_size += 1

    def on_update(self, delta_time: float = 1/60):

        self.body.append({'center_x': self.center_x, 'center_y': self.center_y})
        if len(self.body) > self.body_size:
            self.body.pop(0)

        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y