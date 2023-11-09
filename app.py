from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/convert', methods=['POST'])
def convert_pounds_to_kilograms():
    data = request.get_json()
    pounds = data['pounds']
    kilograms = pounds * 0.45359237
    return jsonify(kilograms=kilograms)


if __name__ == '__main__':
    app.run(debug=True)
