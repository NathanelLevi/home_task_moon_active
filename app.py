from flask import Flask, jsonify

import numbers_api.main

app = Flask(__name__)


@app.route('/ready')
def get_ready():
    return jsonify(success=True)


@app.route('/oddnumber')
def get_odd():
    return numbers_api.main.odd_number()


@app.route('/evennumber')
def get_even():
    return numbers_api.main.even_number()


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)