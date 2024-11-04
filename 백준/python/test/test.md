# 문제이름

[백준 > 단계별로 풀어보기 > 입출력과 사칙연산](https://unwind.tistory.com/)

## 문제

문제문제
문제문제

## 풀이

-   코드에 대한 한마디 정도

```python
print('Hello World!')
```

### 진행한 프로젝트

###### Arcane

Node.js와 React를 사용한 _League of Legends_ 전적 검색 웹 페이지입니다.
riot에서 제공하는 API를 실시간으로 받아와 특정 유저의 전적을 검색합니다..

Promise 기반 라이브러리 **Axios**를 통해 Client와 Server의 비동기 통신을 구현했습니다.

Bcrypt와 JWT를 통해 회원가입/로그인을 구현했습니다.

nosql 데이터베이스인 mongoDB를 사용해 데이터베이스를 구성했습니다.

[![블로그 링크](https://tistory-readme-stats.vercel.app/api?name=unwind&postId=26&description=&color=dark)](https://unwind.tistory.com/entry/Nodejs%EC%99%80-Riot-API%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8)

> https://github.com/ysh038/Arcane

###### 별글

SpringBoot 기반 SNS의 백엔드입니다.

RestfulAPI를 설계하는 것에 중점을 두고 진행했습니다.

[![블로그 링크](https://tistory-readme-stats.vercel.app/api?name=unwind&postId=34&description=&color=dark)](https://unwind.tistory.com/entry/34)

> https://github.com/KKaeBu/StarWriting

###### PetRoad

SpringBoot와 Android기반 어플리케이션입니다.

Android 앱과 SpringBoot 기반의 GPS장치와 사용자의 핸드폰 3개의 비동기 통신을 중점으로 구현했습니다.

모든 통신API는 Restful하도록 설계했습니다.

> https://github.com/almond0115/MyPetRoadApp

###### 채팅 서버

Python3기반 채팅 서버입니다.

클라이언트는 터미널에서 간단한 명령어를 통해 채팅방을 사용할 수 있습니다.

mutex와 contidion variable을 통한 비동기처리, socket, multi-threading 등을 학습하게 되었습니다.

> https://github.com/ysh038/backend2023/tree/main/chat_server

###### 메모장 서버

Flask기반 메모장 서버입니다.

네이버 로그인 API를 통해 OAuth 로그인을 구현했습니다.

Restful한 API 설계를 구현했습니다.

nginx, uWSGI, docker를 통해 배포하는 법을 학습했습니다.

> https://github.com/ysh038/memo_server

d

```python
total = 0
i = 0

while i < 10:
    i += 1
    total += i
```

##### 1회차

i = 0, total = 0 인 상태로 들어간다. 들어간 후 i += 1, total += i 실행

    결과 : i = 1 , total = 1

##### 2회차

i = 1, total = 1 인 상태로 들어간다. 들어간 후 i += 1, total += i 실행

    결과 : i = 2 , total = 3

##### 3회차

i = 2, total = 3 인 상태로 들어간다. 들어간 후 i += 1, total += i 실행

    결과 : i = 3, total = 6

...

##### 10회차

i = 9, total = 45 인 상태로 들어간다. 들어간 후 i += 1, total += i 실행

    결과 : i = 10, total = 55

while문의 조건식(i<10)을 만족하는지 **_판단한 후_** i에 1을 더한다.

따라서, while문의 조건식을 지나가고 나서 i에 1을 더하기 때문에,

10회차 실행할 때의 조건식은 i가 9인상태로 조건식을 들어가게 된다.
