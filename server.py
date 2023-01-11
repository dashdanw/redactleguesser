from flask import Flask
from flask import session
from flask import request
from flask import jsonify

from flask_cors import CORS
from flask_cors import cross_origin

from flask_session import Session

from process_words import get_wordlist

import json


app = Flask(__name__)

app.secret_key = 'redactle_is_dope'
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)
CORS(app)

@app.route("/pop/", methods=['GET'])
@cross_origin('*')
def index():
    if not 'wordlist' in session:
        session['wordlist'] = get_wordlist()
    wordlist = session.get('wordlist')

    count = request.args.get('count', 1000)
    page = request.args.get('page', 0)

    start = int(page) * int(count)
    end = start + int(count)
    print(f'selecting from {start} to {end}')
    try:
        data = wordlist[start:end]
    except IndexError as e:
        return jsonify([])
    
    

    return jsonify(data)



if __name__ == "__main__":
    #app.run(host='localhost', port='8008', ssl_context='adhoc')
    app.run(host='localhost', port='8008')