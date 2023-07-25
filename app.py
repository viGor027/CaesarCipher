from flask import render_template, Blueprint, request
from CaesarCipher.logic.cipher import Cipher


index_blueprint = Blueprint('index', __name__)
history_blueprint = Blueprint('history', __name__)

messages = []


@index_blueprint.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        message = request.form['message']
        shift = int(request.form['shift'])
        message_wrapped = Cipher(message, shift)
        messages.append((message_wrapped.encrypted_message, shift))
        print(messages, message)
        return render_template("index.html")
    else:
        return render_template("index.html")


@index_blueprint.route('/history')
def history():
    return render_template("history.html", messages=messages)
