from flask import Flask, jsonify
import random

app = Flask(__name__)


@app.route('/odd')
def odd_number():
    odd_number = random.choice([i for i in range(1, 21) if i % 2 != 0])
    return jsonify({'odd_number': odd_number})


@app.route('/even')
def even_number():
    even_number = random.choice([i for i in range(1, 21) if i % 2 == 0])
    return jsonify({'even_number': even_number})


if __name__ == '__main__':
    app.run(debug=True)
