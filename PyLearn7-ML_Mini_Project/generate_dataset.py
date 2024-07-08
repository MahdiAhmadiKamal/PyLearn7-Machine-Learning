import arcade
import pandas as pd
from snake import Snake
from apple import Apple


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=600, title="Super Snake V.1.0 🐍")
        arcade.set_background_color(arcade.color.KHAKI)

        self.snake = Snake(self)
        self.food = Apple(self)
        self.condition = ""
        self.dataset = []
            
    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.food.draw()
        
        arcade.draw_text(f"score: {self.snake.score}", self.width-100, 15, arcade.color.BLACK, 15)

        if self.condition == "Game Over":
            arcade.start_render()
            arcade.draw_text("Game Over",self.width/5, self.height/2, arcade.color.BLACK, 45)
            
        arcade.finish_render()

    def on_update(self, delta_time: float):

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
                'bl': None,}
        
        # Data Collection: The distance between the snake and the apple
        if self.snake.center_x == self.food.center_x and self.snake.center_y < self.food.center_y:
            data['au'] = 1
            data['ar'] = 0
            data['ad'] = 0
            data['al'] = 0
        elif self.snake.center_x == self.food.center_x and self.snake.center_y > self.food.center_y:
            data['au'] = 0
            data['ar'] = 0
            data['ad'] = 1
            data['al'] = 0
        elif self.snake.center_x < self.food.center_x and self.snake.center_y == self.food.center_y:
            data['au'] = 0
            data['ar'] = 1
            data['ad'] = 0
            data['al'] = 0
        elif self.snake.center_x > self.food.center_x and self.snake.center_y == self.food.center_y:
            data['au'] = 0
            data['ar'] = 0
            data['ad'] = 0
            data['al'] = 1
        else:
            data['au'] = 0
            data['ar'] = 0
            data['ad'] = 0
            data['al'] = 0

        # Data Collection: The distance between the snake and the walls
        data['wu'] = self.height - self.snake.center_y
        data['wr'] = self.width - self.snake.center_x
        data['wd'] = self.snake.center_y
        data['wl'] = self.snake.center_x

        # Data Collection: The distance between the snake and its body
        for part in self.snake.body:
            if self.snake.center_x == part['x'] and self.snake.center_y < part['y']:
                data['bu'] = 1
                data['br'] = 0
                data['bd'] = 0
                data['bl'] = 0
            elif self.snake.center_x == part['x'] and self.snake.center_y > part['y']:
                data['bu'] = 0
                data['br'] = 0
                data['bd'] = 1
                data['bl'] = 0
            elif self.snake.center_x < part['x'] and self.snake.center_y == part['y']:
                data['bu'] = 0
                data['br'] = 1
                data['bd'] = 0
                data['bl'] = 0
            elif self.snake.center_x > part['x'] and self.snake.center_y == part['y']:
                data['bu'] = 0
                data['br'] = 0
                data['bd'] = 0
                data['bl'] = 1
            else:
                data['bu'] = 0
                data['br'] = 0
                data['bd'] = 0
                data['bl'] = 0
                
        self.dataset.append(data)

        self.snake.move_ai(self.food)

        if self.snake.center_x > self.width or self.snake.center_x<0:
            self.condition = "Game Over"
            
        if self.snake.center_y > self.height or self.snake.center_y<0:
            self.condition = "Game Over"

        if arcade.check_for_collision(self.snake, self.food):
            self.snake.eat(self.food)

            if self.snake.score <= 0:
                self.condition = "Game Over"
            
            self.food = Apple(self)

        # for part in self.snake.body:
        #     if self.snake.center_x == part["x"] and self.snake.center_y == part["y"]:
        #         self.condition = "Game Over"
        
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.Q:
            df = pd.DataFrame(self.dataset)
            df.to_csv('dateset.csv', index=False)


if __name__ == "__main__":
    game = Game()
    arcade.run()


