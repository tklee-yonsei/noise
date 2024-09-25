from flask import Flask, jsonify, request

from noise.gaussian import GaussianNoiseAdder
from noise.uniform import UniformNoiseAdder

app = Flask(__name__)

# 노이즈 방법 매핑 - 클래스 자체를 저장
noise_adder_classes = {
    "gaussian": GaussianNoiseAdder,
    "uniform": UniformNoiseAdder,
}


@app.route("/add_noise/<method>", methods=["POST"])
def add_noise(method):
    noise_adder_class = noise_adder_classes.get(method)
    if noise_adder_class is None:
        return jsonify({"error_code": 3001, "error": "Invalid noise method"}), 400

    # 요청마다 인스턴스 생성
    noise_adder = noise_adder_class()

    symbols_real_imag = request.json.get("symbols")
    if symbols_real_imag is None:
        return jsonify({"error_code": 3002, "error": "Missing symbols data"}), 400

    snr_db = request.json.get("snr_db", 10)

    try:
        noisy_symbols_real_imag = noise_adder.process_request(symbols_real_imag, snr_db)
    except ValueError as e:
        return jsonify({"error_code": 3003, "error": str(e)}), 400

    return jsonify({"noisy_symbols": noisy_symbols_real_imag})


if __name__ == "__main__":
    app.run(port=5003)
