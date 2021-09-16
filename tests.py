from game import *
import unittest


class TestGame(unittest.TestCase):
    def test_3_row_board(self):
        game = Chess()
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)

    def test_change_pawn(self):
        game = Chess()
        game.board_state = [
            [None, game.white_knight, game.white_bishop, game.white_queen, game.white_king, game.white_bishop2, game.white_knight2, game.white_rook2],
            [game.black_a_pawn, game.white_b_pawn, game.white_c_pawn, game.white_d_pawn, game.white_e_pawn, game.white_f_pawn, game.white_g_pawn, game.white_h_pawn],
            [None for i in range(8)],
            [None for i in range(8)],
            [None for i in range(8)],
            [None for i in range(8)],
            [None, game.black_b_pawn, game.black_c_pawn, game.black_d_pawn, game.black_e_pawn,
             game.black_f_pawn, game.black_g_pawn, game.black_h_pawn],
            [game.black_rook, game.black_knight, game.black_bishop, game.black_queen, game.black_king,
             game.black_bishop2, game.black_knight2, game.black_rook2],
        ]
        game.black_a_pawn.moved = True
        game.transition_to(game.black_turn, False)

        move = Move('A2', 'B1')
        game.request(move)
        check_board = [[0, -9, 4, 9, 100, 4, 3, 5],
                       [0, 1, 1, 1, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, -1, -1, -1, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)

    def test_threefold_repetition(self):
        game = Chess()
        move = Move('G1', 'F3')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 0, 5],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0, 3, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('G8', 'F6')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 0, 5],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0, 3, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, -3, 0, 0],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, 0, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('F3', 'G1')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, -3, 0, 0],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, 0, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('F6', 'G8')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('G1', 'F3')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 0, 5],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0, 3, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('G8', 'F6')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 0, 5],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0, 3, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, -3, 0, 0],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, 0, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('F3', 'G1')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, -3, 0, 0],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, 0, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('F6', 'G8')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('G1', 'F3')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)

    def test_move_in_game_en_passant(self):
        game = Chess()
        move = Move('E2', 'E4')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('D7', 'D5')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, -1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, 0, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('E4', 'E5')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, -1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, 0, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('D5', 'D4')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, -1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, 0, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('E5', 'D6')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, -1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, 0, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)

    def test_moving_capture_en_passant_castle(self):
        game = Chess()
        move = Move('E2', 'E4')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('D7', 'D5')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, -1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, 0, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('E4', 'F5')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, -1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, 0, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('E4', 'D5')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, 0, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('C7', 'C5')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, -1, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, 0, 0, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('D5', 'C6')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0, 0, 0],
                       [-1, -1, 0, 0, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('B8', 'C6')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, -3, 0, 0, 0, 0, 0],
                       [-1, -1, 0, 0, -1, -1, -1, -1],
                       [-5, 0, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('F1', 'E2')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 0, 3, 5],
                       [1, 1, 1, 1, 4, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, -3, 0, 0, 0, 0, 0],
                       [-1, -1, 0, 0, -1, -1, -1, -1],
                       [-5, 0, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('C8', 'D7')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 0, 3, 5],
                       [1, 1, 1, 1, 4, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, -3, 0, 0, 0, 0, 0],
                       [-1, -1, 0, -4, -1, -1, -1, -1],
                       [-5, 0, 0, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('G1', 'F3')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 0, 0, 5],
                       [1, 1, 1, 1, 4, 1, 1, 1],
                       [0, 0, 0, 0, 0, 3, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, -3, 0, 0, 0, 0, 0],
                       [-1, -1, 0, -4, -1, -1, -1, -1],
                       [-5, 0, 0, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('D8', 'C7')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 0, 0, 5],
                       [1, 1, 1, 1, 4, 1, 1, 1],
                       [0, 0, 0, 0, 0, 3, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, -3, 0, 0, 0, 0, 0],
                       [-1, -1, -9, -4, -1, -1, -1, -1],
                       [-5, 0, 0, 0, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('E1', 'G1')
        game.request(move)
        check_board = [[5, 3, 4, 9, 0, 5, 100, 0],
                       [1, 1, 1, 1, 4, 1, 1, 1],
                       [0, 0, 0, 0, 0, 3, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, -3, 0, 0, 0, 0, 0],
                       [-1, -1, -9, -4, -1, -1, -1, -1],
                       [-5, 0, 0, 0, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('E8', 'C8')
        game.request(move)
        check_board = [[5, 3, 4, 9, 0, 5, 100, 0],
                       [1, 1, 1, 1, 4, 1, 1, 1],
                       [0, 0, 0, 0, 0, 3, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, -3, 0, 0, 0, 0, 0],
                       [-1, -1, -9, -4, -1, -1, -1, -1],
                       [0, 0, -100, -5, 0, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('E2', 'D3')
        game.request(move)
        check_board = [[5, 3, 4, 9, 0, 5, 100, 0],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 4, 0, 3, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, -3, 0, 0, 0, 0, 0],
                       [-1, -1, -9, -4, -1, -1, -1, -1],
                       [0, 0, -100, -5, 0, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('C7', 'H2')
        game.request(move)
        check_board = [[5, 3, 4, 9, 0, 5, 100, 0],
                       [1, 1, 1, 1, 0, 1, 1, -9],
                       [0, 0, 0, 4, 0, 3, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, -3, 0, 0, 0, 0, 0],
                       [-1, -1, 0, -4, -1, -1, -1, -1],
                       [0, 0, -100, -5, 0, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('G1', 'H1')
        game.request(move)
        check_board = [[5, 3, 4, 9, 0, 5, 100, 0],
                       [1, 1, 1, 1, 0, 1, 1, -9],
                       [0, 0, 0, 4, 0, 3, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, -3, 0, 0, 0, 0, 0],
                       [-1, -1, 0, -4, -1, -1, -1, -1],
                       [0, 0, -100, -5, 0, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('G1', 'H2')
        game.request(move)
        check_board = [[5, 3, 4, 9, 0, 5, 0, 0],
                       [1, 1, 1, 1, 0, 1, 1, 100],
                       [0, 0, 0, 4, 0, 3, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, -3, 0, 0, 0, 0, 0],
                       [-1, -1, 0, -4, -1, -1, -1, -1],
                       [0, 0, -100, -5, 0, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)

        game.reset()
        game.board_state = [
            [game.white_rook, None, None, None, game.white_king,
             None, None, game.white_rook2],
            [game.white_a_pawn]+[None for i in range(7)],
            [None for i in range(8)],
            [None for i in range(8)],
            [None for i in range(8)],
            [None for i in range(8)],
            [None for i in range(8)],
            [game.black_rook, game.black_knight, game.black_bishop, game.black_queen, game.black_king,
             game.black_bishop2, game.black_knight2, game.black_rook2],
        ]
        move = Move('A2', 'A4')
        game.request(move)
        check_board = [[5, 0, 0, 0, 100, 0, 0, 5],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)

        move = Move('D8', 'E7')
        game.request(move)
        check_board = [[5, 0, 0, 0, 100, 0, 0, 5],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, -9, 0, 0, 0],
                       [-5, -3, -4, 0, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)

        move = Move('E1', 'G1')
        game.request(move)
        check_board = [[5, 0, 0, 0, 100, 0, 0, 5],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, -9, 0, 0, 0],
                       [-5, -3, -4, 0, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)

        move = Move('E1', 'F1')
        game.request(move)
        check_board = [[5, 0, 0, 0, 0, 100, 0, 5],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, -9, 0, 0, 0],
                       [-5, -3, -4, 0, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)

        game.reset()
        game.board_state = [
            [game.white_rook, None, None, None, game.white_king,
             None, None, game.white_rook2],
            [game.white_a_pawn] + [None for i in range(7)],
            [None for i in range(8)],
            [None for i in range(8)],
            [None for i in range(8)],
            [None for i in range(8)],
            [None for i in range(8)],
            [game.black_rook, game.black_knight, game.black_bishop, game.black_queen, game.black_king,
             game.black_bishop2, game.black_knight2, game.black_rook2],
        ]
        move = Move('A2', 'A4')
        game.request(move)
        check_board = [[5, 0, 0, 0, 100, 0, 0, 5],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)

        move = Move('D8', 'F6')
        game.request(move)
        check_board = [[5, 0, 0, 0, 100, 0, 0, 5],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, -9, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-5, -3, -4, 0, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)

        move = Move('E1', 'G1')
        game.request(move)
        check_board = [[5, 0, 0, 0, 100, 0, 0, 5],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, -9, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-5, -3, -4, 0, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)

    def test_scholar_mate(self):
        game = Chess()
        move = Move('E2', 'E4')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)

        move = Move('E7', 'E5')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, -1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, -1, 0, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('E4', 'E5')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, -1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, -1, 0, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('D1', 'F3')
        game.request(move)
        check_board = [[5, 3, 4, 0, 100, 4, 3, 5],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 9, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, -1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, -1, 0, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('A7', 'A5')
        game.request(move)
        check_board = [[5, 3, 4, 0, 100, 4, 3, 5],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 9, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0],
                       [-1, 0, 0, 0, -1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, -1, -1, -1, 0, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('F1', 'C4')
        game.request(move)
        check_board = [[5, 3, 4, 0, 100, 0, 3, 5],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 9, 0, 0],
                       [0, 0, 4, 0, 1, 0, 0, 0],
                       [-1, 0, 0, 0, -1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, -1, -1, -1, 0, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('H7', 'H5')
        game.request(move)
        check_board = [[5, 3, 4, 0, 100, 0, 3, 5],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 9, 0, 0],
                       [0, 0, 4, 0, 1, 0, 0, 0],
                       [-1, 0, 0, 0, -1, 0, 0, -1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, -1, -1, -1, 0, -1, -1, 0],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('F3', 'F7')
        game.request(move)
        check_board = [[5, 3, 4, 0, 100, 0, 3, 5],
                       [1, 1, 1, 1, 0, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 4, 0, 1, 0, 0, 0],
                       [-1, 0, 0, 0, -1, 0, 0, -1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, -1, -1, -1, 0, 9, -1, 0],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        print('End' in str(game._state))
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('F3', 'F7')
        game.request(move)
        check_board = [[5, 3, 4, 9, 100, 4, 3, 5],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, -1, -1, -1, -1, -1, -1, -1],
                       [-5, -3, -4, -9, -100, -4, -3, -5]]
        self.assertEqual(game.transposition_board(), check_board)

    def test_move(self):
        move = Move('A1', 'B2')
        self.assertEqual(move.x, [0, 0])
        self.assertEqual(move.y, [1, 1])
