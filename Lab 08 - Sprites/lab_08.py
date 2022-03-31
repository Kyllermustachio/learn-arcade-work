""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.2
SPRITE_SCALING_BACKGROUND = 1
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50
coin_sound = arcade.load_sound("toggle_002.ogg")
error_sound = arcade.load_sound("error_006.ogg")


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Bomb(arcade.Sprite):

    def reset_pos(self):

        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the coin
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()


class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites Lab 08")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.bomb_list = None
        self.background_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        self.background_sprite = None

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bomb_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        self.background_sprite = arcade.Sprite("backgroundColorDesert.png", SPRITE_SCALING_BACKGROUND)
        self.background_sprite.center_x = 400
        self.background_sprite.center_y = 200
        self.background_list.append(self.background_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin("coin_01.png", SPRITE_SCALING_COIN)
            bomb = Bomb("explosion3.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)

            bomb.center_x = random.randrange(SCREEN_WIDTH)
            bomb.center_y = random.randrange(SCREEN_HEIGHT)
            """bomb.change_x = random.randrange(-3, 2)
            bomb.change_y = random.randrange(-3, 2)"""

            # Add the coin to the lists
            self.coin_list.append(coin)
            self.bomb_list.append(bomb)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.background_list.draw()
        self.bomb_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 14)

        if len(self.coin_list) <= 0:
            arcade.draw_text("GAME OVER", 200, 300, arcade.color.BLACK, 40)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        if len(self.coin_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y
        else:
            self.set_mouse_visible(True)
            self.player_sprite.center_x = 810
            self.player_sprite.center_y = 610

    def update(self, delta_time):

        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this example though.)
        self.coin_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(coin_sound)
            self.score += 1

        self.bomb_list.update()

        # Generate a list of all sprites that collided with the player.
        bomb_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bomb_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for bomb in bomb_hit_list:
            bomb.reset_pos()
            bomb.remove_from_sprite_lists()
            arcade.play_sound(error_sound)
            self.score -= 1

        if len(self.coin_list) <= 0:
            Bomb.center_y = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
