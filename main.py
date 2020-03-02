# This program is a guess the number game

from random import randint
from os import environ
from webbrowser import open
from Button import Button
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_difficulty():
    html = ""
    html += "<div class='btn-group' style='width:100%'>"
    html += "<button id='easy' value='1'>Easy</button>" \
            "<button id='medium' value='2'>Medium</button>" \
            "<button id='hard' value='3'>Hard</button>"
    return render_template('index.html', html=html)
    # Add three buttons for choosing difficulty (1, 2, 3)


@app.route('/guess-the-number', methods=['GET'])
def guess_the_number():
    diff = int(request.args.get('difficulty'))
    width = 9.80
    correct_number = randint(1, 10 ** diff)
    environ["CORRECT"] = str(correct_number)
    button_list = [Button(i) for i in range(1, 10 ** diff + 1)]
    html = ""
    html += "<div class='btn-group' id='wrapper' style='width:100%'>"
    html += print_buttons(button_list, width)
    html += "</div>"
    return render_template('guess-the-number.html', html=html)


@app.route('/check-guess', methods=['GET'])
def check_guess():
    guess = int(request.args.get('guess'))
    correct_number = int(environ["CORRECT"])
    if guess < correct_number:
        return "less"
    elif guess > correct_number:
        return "greater"
    else:
        return "correct"


@app.route('/kill', methods=["GET", "POST"])
def kill():
    shutdown_server()
    return("Server shutting down...")



def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError("Not running with the Werkzeug Server")
    func()


def print_buttons(button_list, width):
    output = ""
    for button in button_list:
        if button.is_on:
            output += button.render(width, 1)
        else:
            output += button.render(width, 0)
    return output


open('http://127.0.0.1:5000', new=0)
if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=5000)
