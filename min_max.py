from game import Chess, Move
from time import time
game = Chess()


def get_score(new_game, game):
    score = 0
    board_state = new_game.transposition_board()
    for row in range(8):
        for col in range(8):
           score += board_state[row][col]
    if 'White' in str(game._state):
        score += len(game.available_moves) * 0.01
        score -= len(new_game.available_moves) * 0.01
    else:
        score -= len(game.available_moves) * 0.01
        score += len(new_game.available_moves) * 0.01

    return score


def min_max_player(game, depth):
    best_score = None
    best_score_move = None

    moves = game.available_moves
    amount_of_moves = len(moves)
    if 'End' in str(game._state):
        return 0, None
    for move in moves:
        new_game = game.copy()
        c_move = Move()
        c_move.x = move[0]
        c_move.y = move[1]
        new_game.request(c_move)
        if 'End' in str(game._state):
            return (10000, move) if game._state.win =='white' else (-10000, move)
        else:
            if ((time() - start_time) * amount_of_moves)**(depth+2) > 20 and depth % 2 == 0:
                score = get_score(new_game, game)
            else:
                score, _ = min_max_player(new_game, depth+1)
            if 'White' in str(game._state):
                if best_score is None or score > best_score:
                    best_score = score
                    best_score_move = move
            else:
                if best_score is None or score < best_score:
                    best_score = score
                    best_score_move = move
    return best_score, best_score_move


# game.request(Move('B1','C3'))
# game.request(Move('E7','E5'))
# game.request(Move('D2','D4'))
# game.request(Move('B8','C6'))
# game.request(Move('D4','E5'))
# game.request(Move('C6','E5'))
# game.request(Move('C1','D2'))
# game.request(Move('A8','B8'))
# game.request(Move('A1','C1'))
# game.request(Move('D7','D6'))
# game.request(Move('C3','D5'))
# game.request(Move('G7','G6'))
# game.request(Move('D2','A5'))
# game.request(Move('A8','B8'))
# game.request(Move('D1','D2'))
# game.request(Move('A7','A6'))
# game.request(Move('D2','E3'))
# game.request(Move('F7','F6'))
# game.request(Move('C1','D1'))
# game.request(Move('H7','H5'))
# game.request(Move('D1','D4'))
# game.request(Move('H8','H7'))
# game.request(Move('D4','C4'))
# game.request(Move('B7','B6'))
# game.request(Move('A5','B4'))
# game.request(Move('A6','A5'))
# game.request(Move('B4','D2'))
# game.request(Move('F6','F5'))
# game.request(Move('E1','D1'))
# game.request(Move('A5','A4'))
# game.request(Move('G1','F3'))
# game.request(Move('F8','G7'))
# game.request(Move('F3','E5'))
# game.request(Move('G8','E7'))
# game.request(Move('E5','G6'))
# game.request(Move('G7','B2'))
# game.request(Move('E5','G6'))
# game.request(Move('G7','B2'))
# game.request(Move('D2','E1'))
# game.request(Move('A8','A7'))
# game.request(Move('F2','F3'))
# game.request(Move('C8','A6'))
# game.request(Move('C4','A4'))
# game.request(Move('D8','D7'))
# game.request(Move('A4','A6'))
# game.request(Move('A7','A6'))
# game.request(Move('G6','E7'))
# game.request(Move('A6','A3'))
# game.request(Move('D5','C7'))
# game.request(Move('D7','C7'))
# game.request(Move('C2','C3'))
# game.request(Move('H7','E7'))
# game.request(Move('E3','D4'))
# game.request(Move('E7','H7'))
# game.request(Move('D4','E3'))
# game.request(Move('E8','F7'))
# game.request(Move('E3','D4'))
# game.request(Move('A3','A5'))
# game.request(Move('E1','H4'))
# game.request(Move('H7','G7'))
game.request(Move('D4','F6'))
game.request(Move('F7','E8'))

start_time = time()
depth = 1
move = min_max_player(game, depth)
print(time() - start_time)
