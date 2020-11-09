from abc import ABC


class Cmd(ABC):
    def name(self):
        return NotImplemented

    @staticmethod
    def parse_cmd(cmd):
        if cmd.startswith('steps'):
            p = cmd.split(" ")
            if p[0] != "steps":
                return InvalidCmd()
            try:
                n = int(p[1])
                if n > 0:
                    return StepCmd(int(p[1]))
                else:
                    return InvalidCmd()
            except ValueError:
                return InvalidCmd()

        if cmd.startswith('left'):
            p = cmd.split(" ")
            if len(p) == 1:
                if p[0] != "left":
                    return InvalidCmd()
                else:
                    return ChangeDirectionCmd(-1)

            if len(p) > 2:
                return InvalidCmd()

            if p[0] != "left":
                return InvalidCmd()
            try:
                n = int(p[1])
                if n > 0:
                    return ChangeDirectionCmd(-n)
                else:
                    return InvalidCmd()
            except ValueError:
                return InvalidCmd()

        if cmd.startswith('right'):
            p = cmd.split(" ")
            if len(p) == 1:
                if p[0] != "right":
                    return InvalidCmd()
                else:
                    return ChangeDirectionCmd(1)

            if len(p) > 2:
                return InvalidCmd()

            if p[0] != "right":
                return InvalidCmd()
            try:
                n = int(p[1])
                if n > 0:
                    return ChangeDirectionCmd(n)
                else:
                    return InvalidCmd()
            except ValueError:
                return InvalidCmd()

        if cmd == 'hover':
            return ChangeModeCmd(0)

        if cmd == 'draw':
            return ChangeModeCmd(1)

        if cmd == 'eraser':
            return ChangeModeCmd(2)

        if cmd == "coord":
            return CoordCmd()

        if cmd == "render":
            return RenderCmd()

        if cmd == "clear":
            return ClearCmd()

        if cmd == "quit":
            return QuitCmd()

        return InvalidCmd()


class StepCmd(Cmd):
    def __init__(self, n):
        self.n = n

    def name(self):
        return "step"


class ChangeDirectionCmd(Cmd):
    def __init__(self, n):
        self.n = n

    def name(self):
        return "change_direction"


class ChangeModeCmd(Cmd):
    def __init__(self, n):
        self.n = n

    def name(self):
        return "change_mode"


class InvalidCmd(Cmd):
    def name(self):
        return "invalid"


class CoordCmd(Cmd):
    def name(self):
        return "coord"


class RenderCmd(Cmd):
    def name(self):
        return "render"


class ClearCmd(Cmd):
    def name(self):
        return "clear"


class QuitCmd(Cmd):
    def name(self):
        return "quit"
