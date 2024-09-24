from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Gaussian noise mock endpoint
@app.route("/add_noise/gaussian", methods=["POST"])
def add_gaussian_noise():
    data = request.json
    encoded_signal = data["encoded_signal"]
    noise_level = data["noise_level"]
    
    # Mock response: add Gaussian noise (fixed example)
    noisy_signal = []
    for point in encoded_signal:
        I = 1
        Q = 2
        noisy_signal.append({"I": I, "Q": Q})
    
    response = {"noisy_signal": noisy_signal}
    print(response)
    return jsonify(response)

# Uniform noise mock endpoint
@app.route("/add_noise/uniform", methods=["POST"])
def add_uniform_noise():
    data = request.json
    encoded_signal = data["encoded_signal"]
    noise_range = data["noise_range"]
    
    # Mock response: add Uniform noise (fixed example)
    noisy_signal = []
    for point in encoded_signal:
        I = point["I"] + round(random.uniform(noise_range[0], noise_range[1]), 3)
        Q = point["Q"] + round(random.uniform(noise_range[0], noise_range[1]), 3)
        noisy_signal.append({"I": I, "Q": Q})
    
    response = {"noisy_signal": noisy_signal}
    return jsonify(response)

if __name__ == "__main__":
    # Flask 서버 실행
    app.run(host="0.0.0.0", port=5003)