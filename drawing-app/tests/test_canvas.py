from src.server.canvas import Canvas


def test_cursor_location():
    c = Canvas()
    # verify the default cursor location
    assert c.get_cursor() == (15, 15)
    c.set_cursor(10, 10)
    assert c.get_cursor() == (10, 10)


def test_set_direction():
    c = Canvas()
    assert c.get_direction() == 0

    c.change_direction(1)
    assert c.get_direction() == 1

    c.change_direction(-1)
    assert c.get_direction() == 0

    c.change_direction(-1)
    assert c.get_direction() == 7

    c.change_direction(8)
    assert c.get_direction() == 7


def test_steps_and_direction():
    c = Canvas()
    assert c.get_cursor() == (15, 15)
    assert c.get_direction() == 0
    c.step(1)
    assert c.get_cursor() == (14, 15)

    # verify the cursor stays in the boundary
    c.step(15)
    assert c.get_cursor() == (0, 15)

    # verify the cursor stays in the boundary
    c.change_direction(2)
    c.step(20)
    assert c.get_cursor() == (0, 29)

    c.change_direction(3)
    c.step(2)
    assert c.get_cursor() == (2, 27)

    c.change_direction(-1)
    c.step(2)
    assert c.get_cursor() == (4, 27)


def test_mode_effect():
    c = Canvas()
    # verify the default mode
    assert c.mode == 1
    # hover modes, doesn't change the canvas
    # the canvas is blank everywhere.
    c.set_mode(0)
    assert c.get_cursor() == (15, 15)
    assert c.get_direction() == 0
    c.step(1)
    assert c.get_cell(15, 15) == ' '

    # draw mode, check * symbol
    c.set_mode(1)
    assert c.get_cursor() == (14, 15)
    c.step(1)
    assert c.get_cell(14, 15) == '*'

    # eraser mode, check * symbols are cleared
    c.set_mode(2)
    c.change_direction(4)
    # going down
    assert c.get_direction() == 4
    c.step(2)
    assert c.get_cell(13, 15) == ' '
    assert c.get_cell(14, 15) == ' '
    assert c.get_cursor() == (15, 15)

    c.set_mode(1)
    c.change_direction(-4)
    # going up
    assert c.get_direction() == 0
    c.step(2)
    assert c.get_cell(15, 15) == '*'
    assert c.get_cell(14, 15) == '*'
    assert c.get_cursor() == (13, 15)

    # hover mode, check cells are unchanged
    c.set_mode(0)
    c.change_direction(4)
    # going down
    assert c.get_direction() == 4
    c.step(2)
    assert c.get_cell(13, 15) == ' '
    assert c.get_cell(14, 15) == '*'
    assert c.get_cursor() == (15, 15)
