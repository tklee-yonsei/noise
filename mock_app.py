from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add_noise/<method>', methods=['POST'])
def add_noise(method):
    symbols = request.json.get('symbols')
    # Mock: 노이즈 없이 원본 심볼 그대로 반환
    noisy_symbols = symbols
    return jsonify({'noisy_symbols': noisy_symbols})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6003)  # 모든 인터페이스에서 수신하도록 설정
