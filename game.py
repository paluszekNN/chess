from pawns import *
import numpy as np
import copy


class Move:
    def __init__(self, x='A1', y='A1'):
        self.x = None
        self.y = None
        transform_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, '1': 0, '2': 1, '3': 2,
                            '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}
        if x[0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] and x[1] in ['1', '2', '3', '4', '5', '6', '7', '8']:
            self.x = [transform_to_num[x[1]], transform_to_num[x[0]]]
        else:
            print('Wrong move')
        if y[0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] and y[1] in ['1', '2', '3', '4', '5', '6', '7', '8']:
            self.y = [transform_to_num[y[1]], transform_to_num[y[0]]]
        else:
            print('Wrong move')


class Chess:
    def __init__(self):
        self.white_turn = WhiteMove()
        self.black_turn = BlackMove()

        self.white_king = King('white')
        self.black_king = King('black')
        self.black_a_pawn = BlackPawn()
        self.black_b_pawn = BlackPawn()
        self.black_c_pawn = BlackPawn()
        self.black_d_pawn = BlackPawn()
        self.black_e_pawn = BlackPawn()
        self.black_f_pawn = BlackPawn()
        self.black_g_pawn = BlackPawn()
        self.black_h_pawn = BlackPawn()
        self.white_a_pawn = WhitePawn()
        self.white_b_pawn = WhitePawn()
        self.white_c_pawn = WhitePawn()
        self.white_d_pawn = WhitePawn()
        self.white_e_pawn = WhitePawn()
        self.white_f_pawn = WhitePawn()
        self.white_g_pawn = WhitePawn()
        self.white_h_pawn = WhitePawn()
        self.white_knight = Knight('white')
        self.black_knight = Knight('black')
        self.white_knight2 = Knight('white')
        self.black_knight2 = Knight('black')
        self.white_rook = Rook('white')
        self.black_rook = Rook('black')
        self.white_rook2 = Rook('white')
        self.black_rook2 = Rook('black')
        self.white_bishop = Bishop('white')
        self.black_bishop = Bishop('black')
        self.white_bishop2 = Bishop('white')
        self.black_bishop2 = Bishop('black')
        self.white_queen = Queen('white')
        self.black_queen = Queen('black')

        self.board_state = [
            [self.white_rook, self.white_knight, self.white_bishop, self.white_queen, self.white_king,
             self.white_bishop2, self.white_knight2, self.white_rook2],
            [self.white_a_pawn, self.white_b_pawn, self.white_c_pawn, self.white_d_pawn, self.white_e_pawn,
             self.white_f_pawn, self.white_g_pawn, self.white_h_pawn],
            [None for i in range(8)],
            [None for i in range(8)],
            [None for i in range(8)],
            [None for i in range(8)],
            [self.black_a_pawn, self.black_b_pawn, self.black_c_pawn, self.black_d_pawn, self.black_e_pawn,
             self.black_f_pawn, self.black_g_pawn, self.black_h_pawn],
            [self.black_rook, self.black_knight, self.black_bishop, self.black_queen, self.black_king,
             self.black_bishop2, self.black_knight2, self.black_rook2],
        ]
        self.available_moves = []
        self.en_passant = []
        self.states = []
        self.transition_to(self.white_turn, False)
        self.change_pawns = 'queen'

    def reset(self):
        self.board_state = [
            [self.white_rook, self.white_knight, self.white_bishop, self.white_queen, self.white_king,
             self.white_bishop2, self.white_knight2, self.white_rook2],
            [self.white_a_pawn, self.white_b_pawn, self.white_c_pawn, self.white_d_pawn, self.white_e_pawn,
             self.white_f_pawn, self.white_g_pawn, self.white_h_pawn],
            [None for i in range(8)],
            [None for i in range(8)],
            [None for i in range(8)],
            [None for i in range(8)],
            [self.black_a_pawn, self.black_b_pawn, self.black_c_pawn, self.black_d_pawn, self.black_e_pawn,
             self.black_f_pawn, self.black_g_pawn, self.black_h_pawn],
            [self.black_rook, self.black_knight, self.black_bishop, self.black_queen, self.black_king,
             self.black_bishop2, self.black_knight2, self.black_rook2],
        ]
        for row in range(8):
            for col in range(8):
                if bool(self.board_state[row][col]):
                    self.board_state[row][col].moved = False
        self.states = []
        self.transition_to(self.white_turn, False)

    def copy(self):
        return copy.deepcopy(self)


    def is_threefold_repetition(self):
        count = 0
        for state in self.states:
            if state == self.available_moves:
                count += 1
        if count == 3:
            return True
        else:
            return False

    def transition_to(self, state, is_checking_check):
        self._state = state
        self._state.context = self
        if is_checking_check:
            pass
        else:
            if self._state.exising_of_moves():
                self.states.append(self.available_moves)
                if self.is_threefold_repetition():
                    self._state = EndGame(self)
            else:
                self._state = EndGame(self)

    def transposition_board(self):
        state = []
        for row in range(8):
            state.append([])
            for col in range(8):
                if not self.board_state[row][col]:
                    state[-1].append(0)
                elif type(self.board_state[row][col]).__name__ == 'WhitePawn':
                    state[-1].append(1)
                elif type(self.board_state[row][col]).__name__ == 'BlackPawn':
                    state[-1].append(-1)
                elif type(self.board_state[row][col]).__name__ == 'Rook':
                    state[-1].append(5 if self.board_state[row][col].color == 'white' else -5)
                elif type(self.board_state[row][col]).__name__ == 'Knight':
                    state[-1].append(3 if self.board_state[row][col].color == 'white' else -3)
                elif type(self.board_state[row][col]).__name__ == 'Bishop':
                    state[-1].append(4 if self.board_state[row][col].color == 'white' else -4)
                elif type(self.board_state[row][col]).__name__ == 'Queen':
                    state[-1].append(9 if self.board_state[row][col].color == 'white' else -9)
                elif type(self.board_state[row][col]).__name__ == 'King':
                    state[-1].append(100 if self.board_state[row][col].color == 'white' else -100)
        return state

    def possibility_of_en_passant(self, piece, move):
        if 'Pawn' in str(piece) and abs(move.x[0] - move.y[0]) == 2:
            return True
        else:
            return False

    def capture_en_passant(self, piece, move):
        if 'Pawn' in str(piece) and self.en_passant == move.y:
            return True
        else:
            return False

    def castle(self, piece, move):
        if 'King' in str(piece) and abs(move.y[1] - move.x[1]) == 2:
            return True
        else:
            return False

    def long_castle(self, move):
        if move.y[1] - move.x[1] < 0:
            return True
        else:
            return False

    def change_pawn(self, piece, move):
        if 'Pawn' in str(piece) and move.y[0] in [0, 7]:
            return True
        else:
            return False

    def request(self, move: Move):
        if self._state.move(move):
            new_en_passant = False
            piece = self.board_state[move.x[0]][move.x[1]]
            if self.possibility_of_en_passant(piece, move):
                self.en_passant = [move.x[0] + (move.y[0] - move.x[0]) // 2, move.x[1]]
                new_en_passant = True
            if self.capture_en_passant(piece, move):
                if move.y[0] == 5:
                    self.board_state[move.y[0] - 1][move.y[1]] = None
                else:
                    self.board_state[move.y[0] + 1][move.y[1]] = None
            if self.castle(piece, move):
                if self.long_castle(move):
                    self.board_state[move.y[0]][3] = self.board_state[move.y[0]][0]
                    self.board_state[move.y[0]][0] = None
                else:
                    self.board_state[move.y[0]][5] = self.board_state[move.y[0]][7]
                    self.board_state[move.y[0]][7] = None

            self.board_state[move.y[0]][move.y[1]] = self.board_state[move.x[0]][move.x[1]]
            self.board_state[move.x[0]][move.x[1]] = None
            self.board_state[move.y[0]][move.y[1]].moved = True

            if not new_en_passant:
                self.en_passant = []
            if self.change_pawn(piece, move):
                if self.change_pawns == 'knight':
                    self.board_state[move.y[0]][move.y[1]] = Knight(piece.color)
                elif self.change_pawns == 'rook':
                    self.board_state[move.y[0]][move.y[1]] = Rook(piece.color)
                elif self.change_pawns == 'bishop':
                    self.board_state[move.y[0]][move.y[1]] = Bishop(piece.color)
                else:
                    self.board_state[move.y[0]][move.y[1]] = Queen(piece.color)
            self.transition_to(self.white_turn if 'Black' in str(self._state) else self.black_turn, False)


class State(ABC):
    @property
    def context(self) -> Chess:
        return self._context

    @context.setter
    def context(self, context: Chess) -> None:
        self._context = context

    @abstractmethod
    def move(self, move: Move) -> bool:
        pass

    def color_of_piece(self, row, col):
        if self.context.board_state[row][col]:
            return self.context.board_state[row][col].color
        else:
            return 'None'

    def checking_checks(self, moves):
        moves_to_drop = []
        for move in moves:
            new_en_passant = False
            current_en_passant = self.context.en_passant[:]
            current_board_state = []
            for row in range(8):
                current_board_state.append(self.context.board_state[row][:])
            piece = self.context.board_state[move[0][0]][move[0][1]]
            if 'Pawn' in str(piece) and abs(move[0][0] - move[1][0]) == 2:
                self.context.en_passant = [move[0][0] + (move[1][0] - move[0][0]) // 2, move[0][1]]
                new_en_passant = True
            if 'Pawn' in str(piece) and self.context.en_passant == move[1]:
                if move[1][0] == 5:
                    self.context.board_state[move[1][0] - 1][move[1][1]] = None
                else:
                    self.context.board_state[move[1][0] + 1][move[1][1]] = None
            if 'King' in str(piece) and abs(move[1][1] - move[0][1]) == 2:
                if move[1][1] - move[0][1] < 0:
                    self.context.board_state[move[1][0]][3] = self.context.board_state[move[1][0]][0]
                    self.context.board_state[move[1][0]][0] = None
                else:
                    self.context.board_state[move[1][0]][5] = self.context.board_state[move[1][0]][7]
                    self.context.board_state[move[1][0]][7] = None

            self.context.board_state[move[1][0]][move[1][1]] = self.context.board_state[move[0][0]][move[0][1]]
            if move[1] != move[0]:
                self.context.board_state[move[0][0]][move[0][1]] = None
            if not new_en_passant:
                self.context.en_passant = []

            self.context.transition_to(
                self.context.white_turn if 'Black' in str(self.context._state) else self.context.black_turn, True)
            for move_2 in self.context._state.get_moves():
                if self.context.board_state[move_2[1][0]][move_2[1][1]] in [self.context.white_king,
                                                                            self.context.black_king]:
                    moves_to_drop.append(move)
                    break
            self.context.board_state = current_board_state
            self.context.en_passant = current_en_passant
            self.context.transition_to(
                self.context.white_turn if 'Black' in str(self.context._state) else self.context.black_turn, True)
        return moves_to_drop

    def is_short_range(self, row, col):
        if self.context.board_state[row][col].is_long:
            return False
        else:
            return True

    def is_on_board(self, row, col):
        if 8 > row >= 0 and 0 <= col < 8:
            return True
        else:
            return False

    def possibility_of_capture(self, row, col, move, color):
        if not bool(self.context.board_state[row + move[0]][col + move[1]]) or \
                                            self.context.board_state[row + move[0]][col + move[1]].color != color:
            return True
        else:
            return False

    def possibility_of_castle(self, move,row,col):
        if (move == [0, 2] and (bool(self.context.board_state[row][col + 1]) or
                             bool(self.context.board_state[row][col + 2]) or
                             'Rook' not in str(
                    self.context.board_state[row][7]) or
                             self.context.board_state[row][7].moved)) or \
        (move == [0, -2] and (
                bool(self.context.board_state[row][col - 1]) or
                bool(self.context.board_state[row][col - 2]) or
                bool(self.context.board_state[row][col - 3]) or
                'Rook' not in str(self.context.board_state[row][0]) or
                self.context.board_state[row][0].moved)
         ):
            return False
        else:
            return True

    def possibility_of_long_pawn_move(self, move, piece, row, col):
        if (move == [-2, 0] and bool(self.context.board_state[row - 1][col])) or \
        (move == [2, 0] and bool(self.context.board_state[row + 1][col])):
            return False
        else:
            return True

    def pawn_possibility_of_capture(self, move, row, col, color):
        if move in [[1, 1], [1, -1], [-1, 1], [-1, -1]] and \
                                                    (not bool(self.context.board_state[row + move[0]][col + move[1]]) or
                                                     self.context.board_state[row + move[0]][
                                                         col + move[1]].color == color) and \
                                                    self.context.en_passant != [row + move[0], col + move[1]]:
            return False
        else:
            return True

    def get_moves(self):
        self.context.available_moves = []
        moves = []
        color = 'white' if 'White' in str(self) else 'black'
        for row in range(8):
            for col in range(8):
                if self.context.board_state[row][col]:
                    piece = self.context.board_state[row][col]
                    if piece.color == color:
                        if self.is_short_range(row, col):
                            for move in piece.directions():
                                if self.is_on_board(row + move[0], col + move[1]):
                                    if self.possibility_of_capture(row, col, move, color):
                                        if 'King' in str(piece):
                                            if not self.possibility_of_castle(move, row, col):
                                                continue
                                        if 'Pawn' in str(piece):
                                            if not self.possibility_of_long_pawn_move(move, piece, row, col):
                                                continue
                                            if not self.pawn_possibility_of_capture(move, row, col, color):
                                                continue
                                            if bool(self.context.board_state[row + move[0]][col + move[1]]) and \
                                                    self.context.board_state[row+move[0]][col+move[1]].color != color and \
                                                    move in [[1, 0], [2, 0], [-1, 0], [-2, 0]]:
                                                continue
                                        moves.append([[row, col], [row + move[0], col + move[1]]])
                        else:
                            for move in piece.directions():
                                for step in range(1, 9):
                                    new_move = np.array(move) * step
                                    if self.is_on_board(row + new_move[0], col + new_move[1]):
                                        if not bool(self.context.board_state[row + new_move[0]][col + new_move[1]]):
                                            moves.append([[row, col], [row + new_move[0], col + new_move[1]]])
                                        else:
                                            if self.context.board_state[row + new_move[0]][
                                                col + new_move[1]].color != color:
                                                moves.append([[row, col], [row + new_move[0], col + new_move[1]]])
                                            break
                                    else:
                                        break
        return moves

    def exising_of_moves(self):
        moves = self.get_moves()
        for move in self.checking_checks(moves):
            moves.remove(move)
        for move in moves:
            if 'King' in str(self.context.board_state[move[0][0]][move[0][1]]) and abs(move[1][1]-move[0][1]) == 2:
                if move[1][1]-move[0][1] > 0:
                    if self.checking_checks([[[move[0][0],move[0][1]], [move[0][0],move[0][1]]],
                                             [[move[0][0],move[0][1]], [move[1][0],move[1][1]-1]]]):
                        moves.remove(move)
                else:
                    if self.checking_checks([[[move[0][0],move[0][1]], [move[0][0],move[0][1]]],
                                             [[move[0][0],move[0][1]], [move[1][0],move[1][1]+1]]]):
                        moves.remove(move)
        self.context.available_moves = moves
        if moves:
            return True
        else:
            return False


class WhiteMove(State):
    def move(self, move: Move):
        if self.color_of_piece(move.x[0], move.x[1]) == 'white' and [move.x, move.y] in self.context.available_moves:
            return True


class BlackMove(State):
    def move(self, move: Move):
        if self.color_of_piece(move.x[0], move.x[1]) == 'black' and [move.x, move.y] in self.context.available_moves:
            return True


class EndGame(State):
    def __init__(self, context):
        self.context = context
        self.win = None
        check_mate = self.check_mate()
        if check_mate[0]:
            print('win')
            self.win = check_mate[1]
        else:
            print('draw')

    def check_mate(self):
        for color in ['black', 'white']:
            for row in range(8):
                for col in range(8):
                    if self.context.board_state[row][col]:
                        piece = self.context.board_state[row][col]
                        if piece.color == color:
                            if self.is_short_range(row, col):
                                for move in piece.directions():
                                    if self.is_on_board(row + move[0], col + move[1]):
                                        if self.possibility_of_capture(row, col, move, color):
                                            if self.context.board_state[row + move[0]][col + move[1]] in \
                                                    [self.context.white_king, self.context.black_king]:
                                                return True, color
                            else:
                                for move in piece.directions():
                                    for step in range(1, 9):
                                        new_move = np.array(move) * step
                                        if self.is_on_board(row + new_move[0], col + new_move[1]):
                                            if not bool(self.context.board_state[row + new_move[0]][col + new_move[1]]):
                                                if self.context.board_state[row + move[0]][col + move[1]] in \
                                                        [self.context.white_king, self.context.black_king]:
                                                    return True, color
                                            else:
                                                if self.context.board_state[row + new_move[0]][
                                                    col + new_move[1]].color != color:
                                                    if self.context.board_state[row + move[0]][col + move[1]] in \
                                                            [self.context.white_king, self.context.black_king]:
                                                        return True, color
                                                break
                                        else:
                                            break
        return False, None

    def move(self, move=None) -> bool:
        if move:
            self.context.reset()
        return False


# if __name__ == '__main__':
#     game = Chess()
#     print(game.available_moves)
#     move = Move('E2', 'E4')
#     game.request(move)
#     print(game.en_passant)
#     move = Move('E7', 'E5')
#     game.request(move)
#     print(game.en_passant)
