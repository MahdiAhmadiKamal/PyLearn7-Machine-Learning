import arcade
import pandas as pd
from apple import Apple
from snake import Snake


width = 800
height = 400
title = "Super Snake V.1.0 🐍"

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(width, height, title, resizable=True)
        arcade.set_background_color(arcade.color.KHAKI)

        self.snake = Snake(width, height)
        self.apple = Apple(width, height)
        self.score = 0
        self.dataset = []

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(f"score: {self.score}", self.width-100, 15, arcade.color.BLACK, 15)
        self.snake.draw()
        self.apple.draw()
        
    def on_update(self, delta_time):

        data = {'wu':None,
                'wr':None,
                'wd':None,
                'wl':None,
                'au':None,
                'ar':None,
                'ad':None,
                'al':None,
                'bu':None,
                'br':None,
                'bd':None,
                'bl':None,
                'direction':None}
        
        if self.snake.center_y > self.apple.center_y:
            self.snake.change_x = 0
            self.snake.change_y = -1
            data['direction'] = 2
        elif self.snake.center_y < self.apple.center_y:   
            self.snake.change_x = 0
            self.snake.change_y = 1 
            data['direction'] = 0
        elif self.snake.center_x > self.apple.center_x:   
            self.snake.change_x = -1
            self.snake.change_y = 0 
            data['direction'] = 3
        elif self.snake.center_x < self.apple.center_x:   
            self.snake.change_x = 1
            self.snake.change_y = 0 
            data['direction'] = 1

        if self.snake.center_x == self.apple.center_x and self.snake.center_y < self.apple.center_y:
            data['au'] = 1  
            data['ar'] = 0 
            data['ad'] = 0
            data['al'] = 0
        elif self.snake.center_x == self.apple.center_x and self.snake.center_y > self.apple.center_y:    
            data['au'] = 0
            data['ar'] = 0
            data['ad'] = 1
            data['al'] = 0
        elif self.snake.center_x < self.apple.center_x and self.snake.center_y == self.apple.center_y:
            data['au'] = 0
            data['ar'] = 1
            data['ad'] = 0
            data['al'] = 0
        elif self.snake.center_x > self.apple.center_x and self.snake.center_y == self.apple.center_y:    
            data['au'] = 0
            data['ar'] = 0
            data['ad'] = 0
            data['al'] = 1

        data['wu'] = height - self.snake.center_y 
        data['wr'] = width - self.snake.center_x  
        data['wd'] = self.snake.center_y
        data['wl'] = self.snake.center_x


        for part in self.snake.body:
            if self.snake.center_x == part['center_x'] and self.snake.center_y < part['center_y']:
                data['bu'] = 1
                data['br'] = 0
                data['bd'] = 0
                data['bl'] = 0
            elif self.snake.center_x == part['center_x'] and self.snake.center_y > part['center_y']:
                data['bu'] = 0
                data['br'] = 0
                data['bd'] = 1
                data['bl'] = 0   
            elif self.snake.center_x < part['center_x'] and self.snake.center_y == part['center_y']:
                data['bu'] = 0
                data['br'] = 1
                data['bd'] = 0
                data['bl'] = 0   
            elif self.snake.center_x > part['center_x'] and self.snake.center_y == part['center_y']:
                data['bu'] = 0
                data['br'] = 0
                data['bd'] = 0
                data['bl'] = 1  

        self.dataset.append(data)
        self.snake.on_update(delta_time)
        self.apple.on_update()

        if arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat()
            self.apple = Apple(width, height)
            self.score += 1

    def on_key_release(self, symbol, modifiers: int):
        if symbol == arcade.key.Q:
            df = pd.DataFrame(self.dataset)
            df.to_csv('dataset.csv', index=False)
            arcade.close_window()
            exit(0)
             
       
if __name__ == "__main__":
    window = MyGame()
    arcade.run()
