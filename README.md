# Team 3 - Noise Addition API

이 문서는 팀 3의 노이즈 추가 API에 대한 설명을 제공합니다. API는 두 가지 노이즈 유형(가우시안 노이즈와 균일 노이즈)을 신호에 추가하는 기능을 제공합니다.

## API 엔드포인트

### 1. 가우시안 노이즈 추가

- **URL**: `/add_noise/gaussian`
- **Method**: `POST`
- **Description**: 입력된 신호에 지정된 수준의 가우시안 노이즈를 추가합니다.

#### Request

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
      "encoded_signal": [
        {"I": 0.707, "Q": 0.707},
        {"I": -0.707, "Q": 0.707},
        {"I": -0.707, "Q": -0.707},
        {"I": 0.707, "Q": -0.707}
      ],
      "noise_level": 0.1
    }
    ```

#### Response

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
      "noisy_signal": [
        {"I": 0.807, "Q": 0.657},
        {"I": -0.707, "Q": 0.857},
        {"I": -0.607, "Q": -0.907},
        {"I": 0.757, "Q": -0.657}
      ]
    }
    ```

### 2. 균일 노이즈 추가

- **URL**: `/add_noise/uniform`
- **Method**: `POST`
- **Description**: 입력된 신호에 지정된 범위의 균일 분포 노이즈를 추가합니다.

#### Request

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
      "encoded_signal": [
        {"I": 0.707, "Q": 0.707},
        {"I": -0.707, "Q": 0.707},
        {"I": -0.707, "Q": -0.707},
        {"I": 0.707, "Q": -0.707}
      ],
      "noise_range": [-0.1, 0.1]
    }
    ```

#### Response

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
      "noisy_signal": [
        {"I": 0.607, "Q": 0.807},
        {"I": -0.757, "Q": 0.657},
        {"I": -0.657, "Q": -0.607},
        {"I": 0.657, "Q": -0.807}
      ]
    }
    ```

## Getting Started

### Local Development

To run the preprocessing server in a local development environment, ensure you have Docker installed and use the provided Dockerfile to build and run the server.

1. **Build the Docker image**:
    ```bash
    docker build -f Dockerfile.dev -t dev-noise-server .
    ```

2. **Run the Docker container**:
    ```bash
    docker run -p 5003:5003 -v $(pwd):/app --rm --name container__dev-noise-server dev-noise-server
    ```

The server will be available on `http://localhost:5001`.

### mock

To run the preprocessing server in a mock environment, ensure you have Docker installed and use the provided Dockerfile to build and run the server.

1. **Build the Docker image**:
    ```bash
    docker build -f Dockerfile.mock -t mock-noise-server .
    ```

2. **Run the Docker container**:
    ```bash
    docker run -p 6003:6003 --rm --name container__mock-noise-server mock-noise-server
    ```

The server will be available on `http://localhost:6003`.

## License

This project is licensed under the MIT License.
