from figures.figure import Figure


class Pawn(Figure):
    def check_border(self, x, y, border):
        if x > 8 or x < 1 or y > 8 or y < 1:
            return False
        return True

    def check_other_figure(self, x, y):
        if self.x or self.y

    def _check_pawn_moves(self, x ,y):
        if y - self.y == 1 and self.x == x:
            return True
        return False

    def move(self, x, y):
        self.x = x
        self.y = y
