import arcade
from snake import Snake
from apple import Apple


width = 800
height = 400
title = "Super Snake V.1.0 🐍"

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.KHAKI)

        self.snake = Snake(width, height)
        self.apple = Apple(width, height)
        self.score = 0
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

    def on_update(self, delta_time: float):
        
        self.snake.on_update(delta_time)
        self.apple.on_update()

        if self.snake.center_x>self.width or self.snake.center_x<0:
            self.condition = "Game Over"
            
        if self.snake.center_y>self.height or self.snake.center_y<0:
            self.condition = "Game Over"

        
        if arcade.check_for_collision(self.snake, self.apple):
            
            self.snake.eat()
            self.apple = Apple(width, height)
            self.score += 1

            if self.score <= 0:
                self.condition = "Game Over"


        for part in self.snake.body:
            if self.snake.center_x == part["center_x"] and self.snake.center_y == part["center_y"]:
                self.condition = "Game Over"
        
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0


if __name__ == "__main__":
    game = Game()
    arcade.run()


