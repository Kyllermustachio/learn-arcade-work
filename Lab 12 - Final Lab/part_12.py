"""
Scroll around a large screen.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""


import random
import arcade
from pyglet.math import Vec2

SPRITE_SCALING = 0.5

DEFAULT_SCREEN_WIDTH = 1000
DEFAULT_SCREEN_HEIGHT = 800
SCREEN_TITLE = "Pirate Battle Food Struggle"

NUMBER_OF_COINS = 50
coin_sound = arcade.load_sound("toggle_002.ogg")
explosion_sound = arcade.load_sound("synthetic_explosion_1.flac")
cannon_sound = arcade.load_sound("boom4.wav")
crash_sound = arcade.load_sound("pain_jack_02.wav")
background_music = arcade.load_sound("Blackmoor Tides.mp3")

BULLET_SPEED = 5

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 3


def Main():

    class Ship(arcade.Sprite):

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

            if self.right > 2000:
                self.change_x *= -1

            if self.bottom < 0:
                self.change_y *= -1

            if self.top > 2000:
                self.change_y *= -1

    class Player(arcade.Sprite):

        def __init__(self):
            super().__init__()

            self.scale = 0.8
            self.textures = []

            # Load a left facing texture and a right facing texture.
            # flipped_horizontally=True will mirror the image we load.
            texture = arcade.load_texture("dinghyLargeDown.png")
            self.textures.append(texture)
            texture = arcade.load_texture("dinghyLargeUp.png")
            self.textures.append(texture)
            texture = arcade.load_texture("dinghyLargeLeft.png")
            self.textures.append(texture)
            texture = arcade.load_texture("dinghyLargeRight.png")
            self.textures.append(texture)

            # By default, face right.
            self.texture = texture

        def update(self):
            self.center_x += self.change_x
            self.center_y += self.change_y

            # Figure out if we should face left or right
            if self.change_x < 0:
                self.texture = self.textures[2]
            elif self.change_x > 0:
                self.texture = self.textures[3]
            if self.change_y < 0:
                self.texture = self.textures[0]
            elif self.change_y > 0:
                self.texture = self.textures[1]

    class MyGame(arcade.Window):
        """ Main application class. """

        def __init__(self, width, height, title):
            """
            Initializer
            """
            super().__init__(width, height, title, resizable=True)

            # Sprite lists
            self.player_list = None
            self.wall_list = None
            self.coin_list = None
            self.bullet_list = None
            self.enemy_ship_list = None

            # Set up the player
            self.player_sprite = None
            self.score = 0

            # Physics engine so we don't run into walls.
            self.physics_engine = None
            self.physics_engine2 = None

            # Track the current state of what key is pressed
            self.left_pressed = False
            self.right_pressed = False
            self.up_pressed = False
            self.down_pressed = False

            # Create the cameras. One for the GUI, one for the sprites.

            # We scroll the 'sprite world' but not the GUI.

            self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

            self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        def setup(self):
            arcade.play_sound(background_music)
            """ Set up the game and initialize the variables. """

            # Sprite lists
            self.player_list = arcade.SpriteList()
            self.wall_list = arcade.SpriteList()
            self.coin_list = arcade.SpriteList()
            self.bullet_list = arcade.SpriteList()
            self.enemy_ship_list = arcade.SpriteList()

            # Set up the player
            self.player_sprite = Player()
            self.player_sprite.center_x = 256
            self.player_sprite.center_y = 512
            self.player_list.append(self.player_sprite)

            # --- Place walls with a list
            coordinate_list = [[0, 0], [0, 50], [0, 100], [0, 150], [0, 200], [0, 250], [0, 300], [0, 350], [0, 400],
                               [0, 450], [0, 500], [0, 550], [0, 600], [0, 650], [0, 700], [0, 750], [0, 800], [0, 850],
                               [0, 900], [0, 950], [0, 1000], [0, 1050], [0, 1100], [0, 1150], [0, 1200], [0, 1250],
                               [0, 1300], [0, 1350], [0, 1400], [0, 1450], [0, 1500], [0, 1550], [0, 1600], [0, 1650],
                               [0, 1700], [0, 1750], [0, 1800], [0, 1850], [0, 1900], [0, 1950], [0, 2000]]

            # Loop through coordinates
            for coordinate in coordinate_list:
                wall = arcade.Sprite("ship (1).png", SPRITE_SCALING)
                wall.center_x = coordinate[0]
                wall.center_y = coordinate[1]
                self.wall_list.append(wall)

            coordinate_list = [[50, -50], [100, -50], [150, -50], [200, -50], [250, -50], [300, -50], [350, -50],
                               [400, -50], [450, -50], [500, -50], [550, -50], [600, -50], [650, -50], [700, -50],
                               [750, -50], [800, -50], [850, -50], [900, -50], [950, -50], [1000, -50], [1050, -50],
                               [1100, -50], [1150, -50], [1200, -50], [1250, -50], [1300, -50], [1350, -50],
                               [1400, -50], [1450, -50], [1500, -50], [1550, -50], [1600, -50], [1650, -50],
                               [1700, -50], [1750, -50], [1800, -50], [1850, -50], [1900, -50], [1950, -50],
                               [2000, -50]]

            # Loop through coordinates
            for coordinate in coordinate_list:
                wall = arcade.Sprite("ship (2).png", SPRITE_SCALING)
                wall.center_x = coordinate[0]
                wall.center_y = coordinate[1]
                self.wall_list.append(wall)

            coordinate_list = [[2050, 0], [2050, 50], [2050, 100], [2050, 150], [2050, 200], [2050, 250], [2050, 300],
                               [2050, 350], [2050, 400], [2050, 450], [2050, 500], [2050, 550], [2050, 600],
                               [2050, 650], [2050, 700], [2050, 750], [2050, 800], [2050, 850], [2050, 900],
                               [2050, 950], [2050, 1000], [2050, 1050], [2050, 1100], [2050, 1150], [2050, 1200],
                               [2050, 1250], [2050, 1300], [2050, 1350], [2050, 1400], [2050, 1450], [2050, 1500],
                               [2050, 1550], [2050, 1600], [2050, 1650], [2050, 1700], [2050, 1750], [2050, 1800],
                               [2050, 1850], [2050, 1900], [2050, 1950], [2050, 2000]]

            # Loop through coordinates
            for coordinate in coordinate_list:
                wall = arcade.Sprite("ship (1).png", SPRITE_SCALING)
                wall.center_x = coordinate[0]
                wall.center_y = coordinate[1]
                self.wall_list.append(wall)

            coordinate_list = [[50, 2050], [100, 2050], [150, 2050], [200, 2050], [250, 2050], [300, 2050], [350, 2050],
                               [400, 2050], [450, 2050], [500, 2050], [550, 2050], [600, 2050], [650, 2050],
                               [700, 2050], [750, 2050], [800, 2050], [850, 2050], [900, 2050], [950, 2050],
                               [1000, 2050], [1050, 2050], [1100, 2050], [1150, 2050], [1200, 2050], [1250, 2050],
                               [1300, 2050], [1350, 2050], [1400, 2050], [1450, 2050], [1500, 2050], [1550, 2050],
                               [1600, 2050], [1650, 2050], [1700, 2050], [1750, 2050], [1800, 2050], [1850, 2050],
                               [1900, 2050], [1950, 2050], [2000, 2050]]

            # Loop through coordinates
            for coordinate in coordinate_list:
                wall = arcade.Sprite("ship (2).png", SPRITE_SCALING)
                wall.center_x = coordinate[0]
                wall.center_y = coordinate[1]
                self.wall_list.append(wall)

            for i in range(150):
                # Create the coin instance
                # Coin image from kenney.nl
                enemy_ship = Ship("ship (3).png", SPRITE_SCALING)

                # Position the coin
                enemy_ship.center_x = random.randrange(2000)
                enemy_ship.center_y = random.randrange(2000)
                enemy_ship.change_x = random.randrange(0, 4)
                enemy_ship.change_y = random.randrange(0, 4)

                # Add the coin to the lists
                self.enemy_ship_list.append(enemy_ship)

            """
            # Place boxes inside a loop
            for x in range(50, 2000, 100):
                for y in range(50, 2000, 304):
                    if random.randrange(10) > 0:
                        enemy = arcade.Sprite("ship (3).png", SPRITE_SCALING)
                        enemy.center_x = x
                        enemy.center_y = y
                        self.enemy_ship_list.append(enemy)
            """

            # -- Randomly place coins where there are no walls
            # Create the coins
            for i in range(NUMBER_OF_COINS):

                # Create the coin instance
                # Coin image from kenney.nl
                coin = arcade.Sprite("fish.png", scale=0.2)

                # --- IMPORTANT PART ---

                # Boolean variable if we successfully placed the coin
                coin_placed_successfully = False

                # Keep trying until success
                while not coin_placed_successfully:
                    # Position the coin
                    coin.center_x = random.randrange(2000)
                    coin.center_y = random.randrange(2000)

                    # See if the coin is hitting a wall
                    wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                    # See if the coin is hitting another coin
                    coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                    if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                        # It is!
                        coin_placed_successfully = True

                # Add the coin to the lists
                self.coin_list.append(coin)

                # --- END OF IMPORTANT PART ---

            """
            # -- Set up several columns of walls
            for x in range(200, 1650, 210):
                for y in range(0, 1600, 64):
                    # Randomly skip a box so the player can find a way through
                    if random.randrange(5) > 0:
                        wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
                        wall.center_x = x
                        wall.center_y = y
                        self.wall_list.append(wall)"""

            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
            # self.physics_engine2 = arcade.PhysicsEngineSimple(self.player_sprite, self.enemy_ship_list)

            # Set the background color
            arcade.set_background_color(arcade.color.OCEAN_BOAT_BLUE)

        def on_draw(self):
            """ Render the screen. """

            # This command has to happen before we start drawing
            self.clear()

            # Select the camera we'll use to draw all our sprites
            self.camera_sprites.use()

            # Draw all the sprites.
            self.wall_list.draw()
            self.player_list.draw()
            self.coin_list.draw()
            self.bullet_list.draw()
            self.enemy_ship_list.draw()

            # Select the (unscrolled) camera for our GUI
            self.camera_gui.use()

            # Draw the GUI
            arcade.draw_rectangle_filled(self.width // 2, 20, self.width, 40, arcade.color.ALMOND)
            text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
                   f"{self.camera_sprites.position[1]:5.1f}, " f"Score: {self.score})"
            arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

            arcade.draw_text("Use arrow keys to move,", 10, 80, arcade.color.BLACK, 20)
            arcade.draw_text("and click the mouse to fire.", 10, 50, arcade.color.BLACK, 20)

            if self.score < 0:
                arcade.draw_text("GAME OVER YOU LOSE :(", 200, 300, arcade.color.BLACK, 40)
            elif len(self.coin_list) <= 0:
                if len(self.enemy_ship_list) <= 0:
                    arcade.draw_text("GAME OVER YOU WIN!!!!!!", 200, 300, arcade.color.BLACK, 40)

        def on_key_press(self, key, modifiers):
            """Called whenever a key is pressed. """
            if self.score >= 0:
                if key == arcade.key.UP:
                    self.up_pressed = True
                elif key == arcade.key.DOWN:
                    self.down_pressed = True
                elif key == arcade.key.LEFT:
                    self.left_pressed = True
                elif key == arcade.key.RIGHT:
                    self.right_pressed = True
            elif self.score < 0:
                if key == arcade.key.UP:
                    self.up_pressed = False
                elif key == arcade.key.DOWN:
                    self.down_pressed = False
                elif key == arcade.key.LEFT:
                    self.left_pressed = False
                elif key == arcade.key.RIGHT:
                    self.right_pressed = False

        def on_key_release(self, key, modifiers):
            """Called when the user releases a key. """

            if key == arcade.key.UP:
                self.up_pressed = False
            elif key == arcade.key.DOWN:
                self.down_pressed = False
            elif key == arcade.key.LEFT:
                self.left_pressed = False
            elif key == arcade.key.RIGHT:
                self.right_pressed = False

        def on_mouse_press(self, x, y, button, modifiers):
            if self.score >= 0:
                arcade.play_sound(cannon_sound)

                # Create a bullet
                bullet = arcade.Sprite("explosion3.png", SPRITE_SCALING, angle=90)

                bullet.center_x = self.player_sprite.center_x
                bullet.center_y = self.player_sprite.center_y
                print(Player().textures[0])
                if self.player_sprite.texture == self.player_sprite.textures[0]:
                    bullet.change_y = -10
                elif self.player_sprite.texture == self.player_sprite.textures[1]:
                    bullet.change_y = 10
                elif self.player_sprite.texture == self.player_sprite.textures[2]:
                    bullet.change_x = -10
                elif self.player_sprite.texture == self.player_sprite.textures[3]:
                    bullet.change_x = 10

                # Add the bullet to the appropriate list
                self.bullet_list.append(bullet)
            else:
                print("Can't do that.")

        def on_update(self, delta_time):
            """ Movement and game logic """

            # Call updates on all sprites (The sprites don't do much in this example though.)
            self.coin_list.update()
            self.bullet_list.update()
            self.enemy_ship_list.update()

            # Generate a list of all sprites that collided with the player.
            coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

            # Loop through each colliding sprite, remove it, and add to the score.
            for coin in coins_hit_list:
                coin.remove_from_sprite_lists()
                arcade.play_sound(coin_sound)
                self.score += 1

            for bullet in self.bullet_list:
                # Generate a list of all sprites that collided with the player.
                ship_hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_ship_list)

                if len(ship_hit_list) > 0:
                    bullet.remove_from_sprite_lists()

                # Loop through each colliding sprite, remove it, and add to the score.
                for ship in ship_hit_list:
                    ship.remove_from_sprite_lists()
                    arcade.play_sound(explosion_sound)
                    self.score += 1

                if bullet.bottom > 2000:
                    bullet.remove_from_sprite_lists()
                elif bullet.bottom < -2000:
                    bullet.remove_from_sprite_lists()

            for ship in self.enemy_ship_list:
                # Generate a list of all sprites that collided with the player.
                ship_hit_list = arcade.check_for_collision_with_list(ship, self.bullet_list)

                if len(ship_hit_list) > 0:
                    ship.remove_from_sprite_lists()

            # Crashed ship
            player_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_ship_list)
            for ship in player_hit_list:
                arcade.play_sound(crash_sound)
                ship.remove_from_sprite_lists()
                self.score -= 1

            # Calculate speed based on the keys pressed
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0

            if self.up_pressed and not self.down_pressed:
                self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
            elif self.down_pressed and not self.up_pressed:
                self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
            if self.left_pressed and not self.right_pressed:
                self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
            elif self.right_pressed and not self.left_pressed:
                self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

            if self.score < 0:
                Ship.change_x = 0
                Ship.change_y = 0

            # Call updates on all sprites (The sprites don't do much in this
            # example though.)
            self.physics_engine.update()
            # self.physics_engine2.update()

            # Scroll the screen to the player
            self.scroll_to_player()
            self.player_list.update()

        def scroll_to_player(self):
            """
            Scroll the window to the player.
            if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
            Anything between 0 and 1 will have the camera move to the location with a smoother pan.
            """
            position = Vec2(self.player_sprite.center_x - self.width / 2, self.player_sprite.center_y - self.height / 2)
            self.camera_sprites.move_to(position, CAMERA_SPEED)

        def on_resize(self, width, height):

            """
            Resize window
            Handle the user grabbing the edge and resizing the window.
            """

            self.camera_sprites.resize(int(width), int(height))

            self.camera_gui.resize(int(width), int(height))

    def main():
        """ Main function """
        window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
        window.setup()
        arcade.run()

    if __name__ == "__main__":
        main()


Main()
