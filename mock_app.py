from flask import Flask, jsonify, request

app = Flask(__name__)

# Gaussian noise mock endpoint
@app.route("/add_noise/gaussian", methods=["POST"])
def add_gaussian_noise():
    data = request.json
    encoded_signal = data["encoded_signal"]

    # Mock response: return the input signal as-is
    response = {"noisy_signal": encoded_signal}
    return jsonify(response)

# Uniform noise mock endpoint
@app.route("/add_noise/uniform", methods=["POST"])
def add_uniform_noise():
    data = request.json
    encoded_signal = data["encoded_signal"]

    # Mock response: return the input signal as-is
    response = {"noisy_signal": encoded_signal}
    return jsonify(response)

if __name__ == "__main__":
    # Flask 서버 실행
    app.run(host="0.0.0.0", port=6003)