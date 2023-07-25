from flask import render_template, Blueprint, request, send_file
from CaesarCipher.logic.cipher import Cipher
from CaesarCipher.logic.get_time import get_current_time
import json



index_blueprint = Blueprint('index', __name__)
history_blueprint = Blueprint('history', __name__)

messages = []


@index_blueprint.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        message = request.form['message']
        try:
            shift = int(request.form['shift'])
        except:
            return render_template("index.html")
        time = get_current_time()
        message_wrapped = Cipher(message, shift)
        messages.append((message_wrapped.encrypted_message, shift, time))
        return render_template("index.html")
    else:
        return render_template("index.html")


@index_blueprint.route('/history')
def history():
    return render_template("history.html", messages=messages)


@index_blueprint.route('/download')
def download():
    data_json = {}
    for msg, shift, time in messages:
        print(msg, shift, time)
        data_json[time] = [msg, shift]
    with open('/history.json', 'w') as outfile:
        json.dump(data_json, outfile)
    return send_file('/history.json', as_attachment=True)
