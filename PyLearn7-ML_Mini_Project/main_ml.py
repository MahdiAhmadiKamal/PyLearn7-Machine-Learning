import tensorflow as tf
import pandas as pd
import arcade
from apple import Apple
from snake import Snake


width = 800
height = 400
title = "Super Snake ML 🐍"


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(width, height, title, resizable=True)
        arcade.set_background_color(arcade.color.KHAKI)

        self.snake = Snake(width, height)
        self.apple = Apple(width, height)
        self.score = 0
        self.model = tf.keras.models.load_model('snake_ml_model.h5')
        self.condition = ""
    

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()
        
        arcade.draw_text(f"score: {self.score}", self.width-100, 15, arcade.color.BLACK, 15)

        if self.condition == "Game Over":
            arcade.start_render()
            arcade.draw_text("Game Over",self.width//3.2, self.height/2, arcade.color.BLACK, 45)
            
        arcade.finish_render()
        
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
                'bl':None}
                
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

        data = pd.DataFrame(data, index=[1])
        data.fillna(0, inplace=True)
        data = data.values
        
        output = self.model.predict(data) 
        direction = output.argmax()
        if direction == 0:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif direction == 1:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif direction == 2:
            self.snake.change_x = 0
            self.snake.change_y = -1   
        elif direction == 3:
            self.snake.change_x = -1
            self.snake.change_y = 0       

        self.snake.on_update()
        self.apple.on_update()

        if self.snake.center_x > self.width or self.snake.center_x<0:
            self.condition = "Game Over"
            
        if self.snake.center_y > self.height or self.snake.center_y<0:
            self.condition = "Game Over"

        if arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat()
            self.apple = Apple(width, height)
            self.score += 1

       
if __name__ == "__main__":
    window = MyGame()
    arcade.run()
