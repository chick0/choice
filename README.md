# choice!

메뉴를 랜덤으로 하나 골라주는 웹 사이트 입니다.

## 메뉴 추가 요청하기

1. 이메일로 요청하기
2. 깃헙 이슈 또는 PR 등록하기

## 서버 실행하기
1. 의존성 설치하기
    ```bash
    pip install -r requirements.txt
    ```
3. 서버 실행하기
    ```bash
    gunicorn -c gunicorn.py
    ```