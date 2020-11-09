from src.server.command import *


def test_steps_cmd_parsing():
    s = "steps 1"
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, StepCmd)
    assert cmd.n == 1

    s = "steps 1.0"
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, InvalidCmd)

    s = "steps -1"
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, InvalidCmd)

    s = "stepss -1"
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, InvalidCmd)


def test_change_direction_cmd_parsing():
    s = "left 2"
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, ChangeDirectionCmd)
    assert cmd.n == -2

    s = "right 3"
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, ChangeDirectionCmd)
    assert cmd.n == 3

    s = "left"
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, ChangeDirectionCmd)
    assert cmd.n == -1

    s = "right"
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, ChangeDirectionCmd)
    assert cmd.n == 1

    s = "left 1.0"
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, InvalidCmd)

    s = "right 1.0"
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, InvalidCmd)

    s = "lefts 1"
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, InvalidCmd)

    s = "rights 1"
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, InvalidCmd)

    s = "left -1"
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, InvalidCmd)

    s = "right -1"
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, InvalidCmd)


def test_change_mode_cmd_parsing():
    s = "hover"
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, ChangeModeCmd)
    assert cmd.n == 0

    s = "draw"
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, ChangeModeCmd)
    assert cmd.n == 1

    s = "eraser"
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, ChangeModeCmd)
    assert cmd.n == 2

    s = "hovers"
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, InvalidCmd)

    s = "draws"
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, InvalidCmd)

    s = "erasers"
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, InvalidCmd)


def test_coord_cmd_parsing():
    s = 'coord'
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, CoordCmd)

    s = 'coords'
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, InvalidCmd)


def test_render_cmd_parsing():
    s = 'render'
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, RenderCmd)

    s = 'renders'
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, InvalidCmd)


def test_clear_cmd_parsing():
    s = 'clear'
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, ClearCmd)

    s = 'clears'
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, InvalidCmd)


def test_quit_cmd_parsing():
    s = 'quit'
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, QuitCmd)

    s = 'quits'
    cmd = Cmd.parse_cmd(s)
    assert isinstance(cmd, InvalidCmd)
