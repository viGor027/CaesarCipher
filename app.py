from flask import render_template, Blueprint, request, send_file
from CaesarCipher.logic.cipher import Cipher
from CaesarCipher.logic.get_time import get_current_time
import json

index_blueprint = Blueprint('index', __name__)
history_blueprint = Blueprint('history', __name__)

messages = []


@index_blueprint.route('/', methods=["POST", "GET"])
def index():
    """
    view for landing page of a project, renders index.html
    """
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


@index_blueprint.route('/history')
def history():
    """
    redirects to history page triggered by button click on a main page
    """
    return render_template("history.html", messages=messages)


@index_blueprint.route('/download')
def download():
    """
    lets user download encrypted/decrypted messages to json on a button click on a history.html page
    """
    data_json = {}
    for msg, shift, time in messages:
        print(msg, shift, time)
        data_json[time] = [msg, shift]
    with open('/history.json', 'w') as outfile:
        json.dump(data_json, outfile)
    return send_file('/history.json', as_attachment=True)


@index_blueprint.route('/upload', methods=["POST", "GET"])
def upload():
    """
    lets user upload previously encrypted/decrypted messages from a json file on a button click on a history.html page
    """
    if request.method == "POST":
        file = request.files['file'].read()
        file_dct = json.loads(file.decode('utf-8'))
        messages = []
        for key in file_dct:
            messages.append((file_dct[key][0], file_dct[key][1], key))
    return render_template("history.html", messages=messages)
