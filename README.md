# start-fintech
Financial Technology 핀테크 학습 리포지토리

## 개요
- **금융(Finance) + 기술(Technology)**의 결합
- 금융 서비스에 인공지능, 빅데이터, 블록체인, 클라우드, 모바일 앱 등을 적용해서 기존 금융을 더 `편리하고, 저렴하고, 빠르게 만드는 기술` 또는 산업 분야

### 대표적인 핀테크 분야
1. 간편결제 - 카카오페이, 네이버페이, 삼성페이 등 모바일 기반 결제
2. P2P 대출 - 은행 없이 개인 간 대출 거래를 연결 (예: 8퍼센트)
3. 로보어드바이저 - 인공지능이 포트폴리오 관리 및 투자 조언
4. 암호화폐/블록체인 - 비트코인, 이더리움 등 디지털 자산 기반 금융 시스템
5. 오픈뱅킹/마이데이터 - 여러 금융기관의 정보를 통합하여 사용자에게 맞춤형 서비스
6. 핀테크 API - 금융기관과 개발자 사이의 데이터 연동 기술 (예: 토스의 API)

### 활용할 수 있는 기술 키워드
- 프로그래밍 언어: Python, JavaScript, Java, Kotlin
- 기술스택:
    - 웹 개발: React, Flask/Django, Spring Boot
    - 데이터 처리: Pandas, NumPy, SQL
    - API 연동: REST API, OAuth, OpenBanking API
    - 보안: 암호화/해시 알고리즘, 인증(Authentication), 인증서
    - 클라우드/DevOps: AWS, Docker
- 도구/플랫폼:
    - 금융 데이터 API (예: 금융감독원 오픈API, 카카오페이 테스트 API 등)
    - 국내 핀테크 샌드박스 또는 오픈플랫폼 (예: 금융결제원 오픈플랫폼)

### 기존 커리큘럼
- Python, 재무/회계관리
- GoLang1
- GoLang2
- HTML5, CSS, Javascript
- Node.js, React
- Kotlin
- MySQL Modeling
- Java Backend
- Fintech Cryptography
- Machine Learning/Deep Learning
- Chatbot
- Real Fintech

### 위 커리큘럼의 문제점
1. 취업 타깃과 실습 결과물 간의 연결 약함
    - 각 과목이 단편적인 기술 습득으로 보일 수 있음
    - "이걸 배워서 뭘 할 수 있지?"에 대한 `학생의 동기 유발과 결과물 중심 흐름`이 부족
2. Python 단원이 지나치게 재무/회계로만 한정
    - 파이썬은 ML/데이터/핀테크 자동화 등 활용도가 높은데, "재무회계"로 제한되면 기술 응용력을 보여주기 어려움
3. 실제 핀테크 서비스 구조에 대한 학습 부족
    - "Real Fintech"라는 이름은 있지만,
    - "송금/이체/조회 시스템", "오픈뱅킹 API", "보안/인증 시스템" 등 실제 핀테크 시스템 구현이 명확하게
3. 실제 핀테크 서비스 구조에 대한 학습 부족 
    - 머신러닝, 챗봇, 자바 백엔드 등 많은 내용을 배우지만, "하나의 완성된 핀테크 서비스"로 통합되지 않음
    - GitHub, 배포, 발표용 포트폴리오를 염두에 둔 구성 필요

### 수정 커리큘럼
1. Python 기초 + Pandas, Matplotlib로 재무제표 분석
2. REST API, 서버 성능 튜닝, JWT 인증 GoLang
3. 프론트엔드 완성형 → 핀테크 대시보드, 거래조회 UI 구성 
4. Android 송금 앱 개발 실습 Kotlin
5. 트랜잭션, 정합성, ACID, 금융 로그 설계 중심의 MySQL
6. Spring Boot 기반 이체 서비스 / 보안 인증 Spring Boot
7. 해싱, 대칭/비대칭 키, HTTPS, OAuth2 구조 실습, 핀테크 보안
8. 금융 데이터 기반 사기탐지 모델, 로보어드바이저 머신러닝/딥러닝
9. 금융 상담 챗봇개발
10. 진짜 프로젝트 

## 프로젝트 예시
1. 간편 송금 서비스 - React + Spring Boot/Go + MySQL 
    - 회원가입, 인증, 계좌등록, 송금, 내역조회
2. 로보어드바이저 - Python, Pandas, Streamlit
    - 투자 성향 분석 + 포트폴리오 추천 + 백테스트
3. 사기 탐지 시스템 - ML, Flask, RabbitMQ
    - 비정상 거래 탐지, 이상알림
4. 금융 챗봇 - 비정상 거래 탐지, 이상알림
    - FAQ 자동응답 + 잔액조회 시뮬레이션


## 뉴 커리큘럼

### 1~2주차: Python + 재무/회계 기초
- [링크](./fintech01_python/README.md) 