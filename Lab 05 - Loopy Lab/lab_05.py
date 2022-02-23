import arcade


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    COLUMN_SPACING = 10
    ROW_SPACING = 10
    LEFT_MARGIN = 5
    BOTTOM_MARGIN = 5

    for row in range(30):
        for column in range(30):
            x = column * COLUMN_SPACING + LEFT_MARGIN  # Instead of zero, calculate the proper x location using 'column'
            y = row * ROW_SPACING + BOTTOM_MARGIN  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    # Below, replace "pass" with your code for the loop.
    # Use the modulus operator and an if statement to select the color
    # Don't loop from 30 to 60 to shift everything over, just add 300 to x.
    COLUMN_SPACING = 10
    ROW_SPACING = 10
    LEFT_MARGIN = 5
    BOTTOM_MARGIN = 5

    for row in range(30):
        for column in range(30):
            x = column * COLUMN_SPACING + LEFT_MARGIN + 300
            y = row * ROW_SPACING + BOTTOM_MARGIN
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

            if column % 2 == 1:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)


def draw_section_3():
    # Use the modulus operator and an if/else statement to select the color.
    # Don't use multiple 'if' statements.
    COLUMN_SPACING = 10
    ROW_SPACING = 10
    LEFT_MARGIN = 5
    BOTTOM_MARGIN = 5

    for row in range(30):
        for column in range(30):
            x = column * COLUMN_SPACING + LEFT_MARGIN + 600
            y = row * ROW_SPACING + BOTTOM_MARGIN
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

            if row % 2 == 1:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)


def draw_section_4():
    # Use the modulus operator and just one 'if' statement to select the color.
    COLUMN_SPACING = 10
    ROW_SPACING = 10
    LEFT_MARGIN = 5
    BOTTOM_MARGIN = 5

    for row in range(30):
        for column in range(30):
            x = column * COLUMN_SPACING + LEFT_MARGIN + 900
            y = row * ROW_SPACING + BOTTOM_MARGIN
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

            if column % 2 == 1:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            if row % 2 == 1:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)


def draw_section_5():
    # Do NOT use 'if' statements to complete 5-8. Manipulate the loops instead.
    COLUMN_SPACING = -10
    ROW_SPACING = 10
    LEFT_MARGIN = 305
    BOTTOM_MARGIN = 305

    for row in range(30):
        for column in range(30 - row + 1):
            x = column * COLUMN_SPACING + LEFT_MARGIN
            y = row * ROW_SPACING + BOTTOM_MARGIN
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_6():
    COLUMN_SPACING = 10
    ROW_SPACING = 10
    LEFT_MARGIN = 5
    BOTTOM_MARGIN = 305

    for row in range(30):
        for column in range(30 - row):
            x = column * COLUMN_SPACING + LEFT_MARGIN + 300
            y = row * ROW_SPACING + BOTTOM_MARGIN
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_7():
    COLUMN_SPACING = 10
    ROW_SPACING = 10
    LEFT_MARGIN = 5
    BOTTOM_MARGIN = 305

    for row in range(30):
        for column in range(row + 1):
            x = column * COLUMN_SPACING + LEFT_MARGIN + 600
            y = row * ROW_SPACING + BOTTOM_MARGIN
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_8():
    COLUMN_SPACING = -10
    ROW_SPACING = 10
    LEFT_MARGIN = 305
    BOTTOM_MARGIN = 305

    for row in range(30):
        for column in range(row + 2):
            x = column * COLUMN_SPACING + LEFT_MARGIN + 900
            y = row * ROW_SPACING + BOTTOM_MARGIN
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()
