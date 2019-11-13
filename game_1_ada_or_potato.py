import arcade

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Ada or Potato"
GAME_SPEED = 1 / 60
TIMER_MAXIMUM = 100

ada = arcade.load_texture("images/ada.png")
potato = arcade.Sprite("potato.png")


class AdaPotato(arcade.Window):
    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.score = 0

        # location
        self.center_x = WINDOW_WIDTH / 2
        self.center_y = WINDOW_HEIGHT / 2

        # sprites
        self.sprite_list = None
        self.potato = potato
        self.ada = ada

        self.texture = None
        self.timer = 0

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)

        self.sprite_list.append(self.ada)
        self.sprite_list.append(self.potato)

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        self.texture = self.sprite_list()
        for self.texture
        if self.texture == self.ada:
            self.texture == self.potato
        else:
            self.texture == self.ada

    def on_mouse_press(self, x, y, button):
        """ Going to determine when the mouse presses potato or ada
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            if self.texture == self.ada:
                self.score += 1
            if self.texture == self.potato:
                self.score -= 1

    def update_timer(self):
        if self.timer < TIMER_MAXIMUM:
            self.timer += 1
        else:
            self.timer = 0


def main():
    window = AdaPotato()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
