import arcade
from snake import Snake
from apple import Apple


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=600, title="Super Snake V.1.0 🐍")
        arcade.set_background_color(arcade.color.KHAKI)

        self.snake = Snake(self)
        self.food = Apple(self)
        self.condition = ""
            
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
        self.snake.move()

        if self.snake.center_x>self.width or self.snake.center_x<0:
            self.condition = "Game Over"
            
        if self.snake.center_y>self.height or self.snake.center_y<0:
            self.condition = "Game Over"

      
        if arcade.check_for_collision(self.snake, self.food):
            self.snake.eat(self.food)

            if self.snake.score <= 0:
                self.condition = "Game Over"
            
            self.food = Apple(self)

        for part in self.snake.body:
            if self.snake.center_x == part["x"] and self.snake.center_y == part["y"]:
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


