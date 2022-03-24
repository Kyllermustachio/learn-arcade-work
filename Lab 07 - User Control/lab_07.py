""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5
laser_sound = arcade.load_sound("laser.wav")
edge_sound = arcade.load_sound("kick-bass-808-drums-loop-6-11282.mp3")


def draw_sun():
    # Drawing a sun
    arcade.draw_circle_filled(20, 580, 60, (230, 224, 69))

    # Drawing sun rays
    arcade.draw_line(20, 580, 105, 530, (230, 224, 69), 3)
    arcade.draw_line(20, 580, 120, 590, (230, 224, 69), 3)
    arcade.draw_line(20, 580, 50, 490, (230, 224, 69), 3)


def draw_ground():
    # Drawing a rectangle for the ground
    arcade.draw_lrtb_rectangle_filled(0, 800, 300, 0, (9, 122, 26))


def draw_building():
    # Drawing building front
    arcade.draw_rectangle_filled(300, 300, 250, 200, (196, 196, 181))

    # Drawing roof
    arcade.draw_triangle_filled(148, 400, 450, 400, 300, 500, (105, 73, 25))

    # Drawing door
    arcade.draw_rectangle_filled(300, 235, 50, 70, (156, 131, 104))
    arcade.draw_circle_filled(315, 230, 5, (207, 164, 56))


def draw_windows(x, y):
    # Drawing windows
    arcade.draw_rectangle_filled(x, y, 40, 50, (85, 184, 217))
    arcade.draw_rectangle_outline(x, y, 40, 50, (156, 131, 104), 5)


def draw_clouds(x, y):
    arcade.draw_ellipse_filled(x, y, 80, 60, (237, 234, 230))
    arcade.draw_ellipse_filled(x + 20, y + 20, 80, 60, (237, 234, 230))
    arcade.draw_ellipse_filled(x - 20, y + 20, 80, 60, (237, 234, 230))
    arcade.draw_ellipse_filled(x + 40, y + 10, 80, 60, (237, 234, 230))


class Cloud:
    def __init__(self, x, y, change_x, change_y, width, height):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height

    def draw_moving_cloud(self):
        arcade.draw_ellipse_filled(self.x, self.y, self.width, self.height, (237, 234, 230))
        arcade.draw_ellipse_filled(self.x + 20, self.y + 20, self.width, self.height, (237, 234, 230))
        arcade.draw_ellipse_filled(self.x - 20, self.y + 20, self.width, self.height, (237, 234, 230))
        arcade.draw_ellipse_filled(self.x + 40, self.y + 10, self.width, self.height, (237, 234, 230))

    def update(self):
        # Move the cloud
        self.y += self.change_y
        self.x += self.change_x

        # See if the cloud hit the edge of the screen. If so, change direction
        if self.x < self.width:
            self.x = self.width
            arcade.play_sound(edge_sound)

        if self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width
            arcade.play_sound(edge_sound)

        if self.y < self.height:
            self.y = self.height
            arcade.play_sound(edge_sound)

        if self.y > SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height
            arcade.play_sound(edge_sound)


class Circle:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        # Set the background color
        arcade.set_background_color((88, 169, 209))

        self.circle = Circle(50, 50, 15, arcade.color.WHITE_SMOKE)
        self.cloud = Cloud(600, 400, 0, 0, 80, 60)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.circle.position_x = x
        self.circle.position_y = y

    def on_draw(self):
        arcade.start_render()

        draw_ground()

        draw_sun()

        draw_building()

        draw_windows(220, 260)
        draw_windows(220, 350)
        draw_windows(375, 260)
        draw_windows(375, 350)

        draw_clouds(200, 500)
        draw_clouds(400, 520)

        self.circle.draw()
        self.cloud.draw_moving_cloud()

        # Finish drawing
        arcade.finish_render()

    def update(self, delta_time):
        self.cloud.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.cloud.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.cloud.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.cloud.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.cloud.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.cloud.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.cloud.change_y = 0

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """

        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(laser_sound)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(laser_sound)


def main():
    window = MyGame()
    arcade.run()


main()
