from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add_noise/<method>', methods=['POST'])
def add_noise(method):
    symbols = request.json.get('symbols')
    # Mock: 노이즈 없이 원본 심볼 그대로 반환
    noisy_symbols = symbols
    return jsonify({'noisy_symbols': noisy_symbols})

if __name__ == '__main__':
    app.run(port=6003)
