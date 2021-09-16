from abc import ABC, abstractmethod


class Pawn(ABC):
    def __init__(self, color):
        self.color = color
        self._moved = False

    @property
    def moved(self):
        return self._moved

    @property
    def is_long (self):
        return False

    @property
    def directions(self):
        return []

    @moved.setter
    def moved(self, moved):
        self._moved = moved


class WhitePawn(Pawn):
    def __init__(self):
        super().__init__('white')

    @property
    def name(self):
        return 'Pawn'

    def directions(self):
        if self.moved:
            return [[1, 1], [1, -1], [1, 0]]
        else:
            return [[1, 1], [1, -1], [1, 0], [2, 0]]


class BlackPawn(Pawn):
    def __init__(self):
        super().__init__('black')

    @property
    def name(self):
        return 'Pawn'

    def directions(self):
        if self.moved:
            return [[-1, 1], [-1, -1], [-1, 0]]
        else:
            return [[-1, 1], [-1, -1], [-1, 0], [-2, 0]]


class King(Pawn):
    @property
    def name(self):
        return 'King'

    def directions(self):
        if self.moved:
            return [[-1, 1], [-1, -1], [-1, 0], [1, 1], [1, -1], [1, 0], [0, 1], [0, -1]]
        else:
            return [[-1, 1], [-1, -1], [-1, 0], [1, 1], [1, -1], [1, 0], [0, 1], [0, -1], [0, 2], [0, -2]]


class Queen(Pawn):
    @property
    def name(self):
        return 'Queen'

    def is_long(self):
        return True

    def directions(self):
        return [[-1, 1], [-1, -1], [-1, 0], [1, 1], [1, -1], [1, 0], [0, 1], [0, -1]]


class Rook(Pawn):
    @property
    def name(self):
        return 'Rook'

    def is_long(self):
        return True

    def directions(self):
        return [[-1, 0], [1, 0], [0, 1], [0, -1]]


class Bishop(Pawn):
    @property
    def name(self):
        return 'Bishop'

    def is_long(self):
        return True

    def directions(self):
        return [[-1, 1], [-1, -1], [1, 1], [1, -1]]


class Knight(Pawn):
    @property
    def name(self):
        return 'Knight'

    def directions(self):
        return [[-1, 2], [-1, -2], [-2, 1], [1, 2], [1, -2], [2, 1], [-2, -1], [2, -1]]
