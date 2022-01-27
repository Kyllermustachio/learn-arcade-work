# Import the "arcade" library
import arcade

# Open up a window.
arcade.open_window(600, 600, "Lab 2")

# Set the background color
arcade.set_background_color((88, 169, 209))

# Get ready to draw
arcade.start_render()

# Drawing a rectangle for the ground
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, (9, 122, 26))

# Drawing a sun
arcade.draw_circle_filled(20, 580, 60, (230, 224, 69))

# Drawing sun rays
arcade.draw_line(20, 580, 105, 530, (230, 224, 69), 3)
arcade.draw_line(20, 580, 120, 590, (230, 224, 69), 3)
arcade.draw_line(20, 580, 50, 490, (230, 224, 69), 3)

# Drawing building front
arcade.draw_rectangle_filled(300, 300, 250, 200, (196, 196, 181))

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
