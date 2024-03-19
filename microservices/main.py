from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)


@app.route('/')
def get_response():
    # Get the URL from the environment variable
    url = os.getenv('API_URL')

    if not url:
        return jsonify({'error': 'API_URL environment variable is not set'}), 500

    # Send a GET request to the API URL
    try:
        response = requests.get(url)
        response_data = response.json()
        return jsonify(response_data), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
