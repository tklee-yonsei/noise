# 팀 3 - 노이즈 API 문서

이 문서는 팀 3의 노이즈 추가 API에 대한 설명을 제공합니다. 

API는 두 가지 노이즈 유형(가우시안 노이즈와 균일 노이즈)을 신호에 추가하는 기능을 제공합니다.

본 프로젝트의 설명은 다음 링크에서 보실 수 있습니다.

https://hot-periwinkle-9ea.notion.site/d8c0797eff484f98b099cb9ed885965f

## 관련 작업

본 프로젝트의 github 및 연관 프로젝트의 github 주소는 다음과 같습니다.

- 팀1 - 채널 코딩/디코딩 - coder
    - https://github.com/tklee-yonsei/preprocess
- 팀2 - 변복조 - modulator
    - https://github.com/tklee-yonsei/modulator
- 팀3 - 노이즈 - noise
    - https://github.com/tklee-yonsei/noise
- 클라이언트
    - https://github.com/tklee-yonsei/client

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
      "symbols": [
        [
          -1.0,
          -1.0
        ],
        [
          -1.0,
          1.0
        ],
        [
          1.0,
          1.0
        ],
        [
          -1.0,
          -1.0
        ]
      ],
      "snr_db": 10
    }
    ```

#### Response

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
      "noisy_symbols": [
        [
          -1.1030480607008906,
          -1.120369890649259
        ],
        [
          -1.3260931328994576,
          0.9760636214747762
        ],
        [
          1.3581396365712213,
          1.198680955050817
        ],
        [
          -0.651732392847555,
          -0.6672753280757961
        ]
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
      "symbols": [
        [
          -1.0,
          -1.0
        ],
        [
          -1.0,
          1.0
        ],
        [
          1.0,
          1.0
        ],
        [
          -1.0,
          -1.0
        ]
      ],
      "snr_db": 10
    }
    ```

#### Response

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
      "noisy_symbols": [
        [
          -0.8466725757707981,
          -1.0
        ],
        [
          -0.3674053305959475,
          1.0
        ],
        [
          1.0357426410391966,
          1.0
        ],
        [
          -1.0551227598178854,
          -1.0
        ]
      ]
    }
    ```

## 에러

- **3001**: Invalid noise method
- **3002**: Missing symbols data
- **3003**: Invalid symbols data format

## 시작하기

이 섹션에서는 다양한 환경에서 서버를 설정하고, 
실행하는 방법에 대한 지침을 제공합니다.

### 로컬 개발

로컬 개발 환경에서 서버를 실행하려면, 
Docker가 설치되어 있는지 확인하고, 
제공된 Dockerfile을 사용하여 서버를 빌드하고 실행하세요.

1. **Docker 이미지 빌드**:
    ```bash
    docker build -f Dockerfile.dev -t dev-noise-server .
    ```

2. **Docker 컨테이너 실행**:
    ```bash
    docker run -p 5003:5003 -v $(pwd):/app --rm --name container__dev-noise-server dev-noise-server
    ```

서버는 `http://localhost:5003`에서 사용할 수 있습니다.

### mock

mock 환경에서 서버를 실행하려면, 
Docker가 설치되어 있는지 확인하고, 
제공된 Dockerfile을 사용하여 서버를 빌드하고 실행하세요.

1. **Docker 이미지 빌드**:
    ```bash
    docker build -f Dockerfile.mock -t mock-noise-server .
    ```

2. **Docker 컨테이너 실행**:
    ```bash
    docker run -p 6003:6003 --rm --name container__mock-noise-server mock-noise-server
    ```

서버는 `http://localhost:6003`에서 사용할 수 있습니다.

## License

This project is licensed under the MIT License.
