class Canvas(object):
    def __init__(self):
        self.rows = 30
        self.cols = 30
        self.x = 15
        self.y = 15
        # 0: up, 1: up right, 2: right, 3: down right, 4: down
        # 5: down left, 6: left, 7: up left
        self.direction = 0
        self.canvas = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        # 0: hover, 1: draw, 2: eraser
        self.mode = 1

    def change_direction(self, n):
        self.direction = (self.direction + n) % 8

    def set_mode(self, mode):
        self.mode = mode

    def set_cursor(self, x, y):
        self.x = x
        self.y = y

    def clear(self):
        self.canvas = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]

    def step(self, n):
        for i in range(n):
            self.step_one()

    def step_one(self):
        if self.mode == 1:
            self.canvas[self.x][self.y] = '*'

        if self.mode == 2:
            self.canvas[self.x][self.y] = ' '

        # advance the cursor one step according to the direction
        # up one step
        if self.direction == 0 or self.direction == 1 or self.direction == 7:
            self.x -= 1

        # right one step
        if self.direction == 1 or self.direction == 2 or self.direction == 3:
            self.y += 1

        # down one step
        if self.direction == 3 or self.direction == 4 or self.direction == 5:
            self.x += 1

        # left one step
        if self.direction == 5 or self.direction == 6 or self.direction == 7:
            self.y -= 1

        # make sure the cursor doesn't go beyond the boundary
        if self.x < 0:
            self.x = 0

        if self.x >= self.rows:
            self.x = self.rows - 1

        if self.y < 0:
            self.y = 0

        if self.y >= self.cols:
            self.y = self.cols - 1

    def get_cursor(self):
        return self.x, self.y

    def get_direction(self):
        return self.direction

    def get_cell(self, x, y):
        return self.canvas[x][y]

    def render(self):
        output = []
        first = [u'\u2550' for _ in range(self.cols + 2)]
        first[0] = u'\u2554'
        first[self.cols + 1] = u'\u2557'
        output.append(''.join(first))

        for i in range(self.rows):
            row = [' ' for i in range(self.cols + 2)]
            row[0] = u'\u2551'
            row[1:self.cols + 1] = self.canvas[i]
            row[self.cols + 1] = u'\u2551'
            output.append(''.join(row))

        end = [u'\u2550' for _ in range(self.cols + 2)]
        end[0] = u'\u255A'
        end[self.cols + 1] = u'\u255D'
        output.append(''.join(end))
        return output


