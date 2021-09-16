from flask import Flask, render_template, request
from game import Chess, Move

app = Flask(__name__)

game = Chess()
square = None
square2 = None


@app.route('/', methods=["POST", 'GET'])
def home():
    global square, square2, game
    if request.method == 'POST':
        if 'new' in request.form.to_dict().keys():
            game.reset()
            if square:
                return render_template('board.html', content=[game, Move(square).x])
            else:
                return render_template('board.html', content=[game, square])
        elif 'position' in request.form.to_dict().keys():
            if not square:
                square = chr(int(request.form['position'][0]) + 65) + str(int(request.form['position'][1]) + 1)
            else:
                square2 = chr(int(request.form['position'][0]) + 65) + str(int(request.form['position'][1]) + 1)
                move = Move(square, square2)
                game.request(move)
                square = None
            if square:
                return render_template('board.html', content=[game, Move(square).x])
            else:
                return render_template('board.html', content=[game, square])
        else:
            game.change_pawns = request.form['change']
            if square:
                return render_template('board.html', content=[game, Move(square).x])
            else:
                return render_template('board.html', content=[game, square])
    else:
        if square:
            return render_template('board.html', content=[game, Move(square).x])
        else:
            return render_template('board.html', content=[game, square])


if __name__ == '__main__':
    app.run(debug=True)
