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

# Drawing roof
arcade.draw_triangle_filled(148, 400, 450, 400, 300, 500, (105, 73, 25))

# Drawing door
arcade.draw_rectangle_filled(300, 235, 50, 70, (156, 131, 104))
arcade.draw_circle_filled(315, 230, 5, (207, 164, 56))

# Drawing windows
arcade.draw_rectangle_filled(220, 260, 40, 50, (85, 184, 217))
arcade.draw_rectangle_outline(220, 260, 40, 50, (156, 131, 104), 5)

arcade.draw_rectangle_filled(220, 350, 40, 50, (85, 184, 217))
arcade.draw_rectangle_outline(220, 350, 40, 50, (156, 131, 104), 5)

arcade.draw_rectangle_filled(375, 260, 40, 50, (85, 184, 217))
arcade.draw_rectangle_outline(375, 260, 40, 50, (156, 131, 104), 5)

arcade.draw_rectangle_filled(375, 350, 40, 50, (85, 184, 217))
arcade.draw_rectangle_outline(375, 350, 40, 50, (156, 131, 104), 5)

# Drawing clouds
arcade.draw_ellipse_filled(200, 500, 80, 60, (237, 234, 230))
arcade.draw_ellipse_filled(220, 520, 80, 60, (237, 234, 230))
arcade.draw_ellipse_filled(180, 520, 80, 60, (237, 234, 230))
arcade.draw_ellipse_filled(240, 510, 80, 60, (237, 234, 230))

arcade.draw_ellipse_filled(400, 520, 80, 60, (237, 234, 230))
arcade.draw_ellipse_filled(420, 540, 80, 60, (237, 234, 230))
arcade.draw_ellipse_filled(380, 540, 80, 60, (237, 234, 230))
arcade.draw_ellipse_filled(440, 530, 80, 60, (237, 234, 230))

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
