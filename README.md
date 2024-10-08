# HAHARYEONGWU

## 기술 스택

![img2](https://img.shields.io/badge/Apache_kafka-2.13-231F20)
![img2](https://img.shields.io/badge/Apache_spark-3.5.1-E25A1C)
![img2](https://img.shields.io/badge/Apache_Airflow-2.9.3-017CEE)
![img2](https://img.shields.io/badge/Apache_Zeppelin-0.11.1-4E5EE4)

## 설명
- 같은 Server, 같은 topic을 공유하는 팀원 간 채팅 기능을 제공합니다.
- Airflow를 통해 해당 topic을 이용하는 사용자 간 대화를 감사할 수 있습니다.
- '@챗봇 영화이름'으로 Box Office에 등록된 영화 정보를 얻을 수 있습니다.
- Airflow Task가 끝난 경우 채팅 공간에 알림 기능을 제공합니다.
- 특정 시간에 정해진 일정(ex. Kanban Meeting)을 위하여 채팅 공간에 알림 기능을 제공합니다.

### 요구사항 정의서
![image](https://github.com/user-attachments/assets/579ae89d-3bbf-40cf-b813-1b8f60b308c4)

### 테스트 계획 및 테스트 결과
![image](https://github.com/user-attachments/assets/fc30b642-5830-4638-96f0-53f4a3ddb412)
![image](https://github.com/user-attachments/assets/b9266c5d-2d38-4d81-9e56-865b4028f704)

### 시스템 아키텍쳐
![image](https://github.com/user-attachments/assets/639c307e-c10d-4700-8edd-f647df226055)

## 실행 방법
```bash
$ git clone https://github.com/pladata-encore/DE32-2rd_team6
$ cd DE32-2rd_team6

#option for dev
$ source .venv/bin/activate

$ pip install .
$ python src/de32_2rd_team6/con_chat3.py
$ python src/de32_2rd_team6/pro_chat3.py
```

### 업무 메신저 기능
**메시지 송수신**

- python src/de32_2rd_team6/pro_chat3.py ->  발신자

![image](https://github.com/user-attachments/assets/b3833d39-4c0d-48c7-b227-d5df71b3f2ee)

- python src/de32_2rd_team6/con_chat3.py -> 수신자

![image](https://github.com/user-attachments/assets/0a0b1176-e607-4cca-bc62-9c981fa4a5b6)

### 영화 관련 Q&A 챗봇 기능

- 입력 : @영화 파묘
![image](https://github.com/user-attachments/assets/dbe84f4d-a75a-412f-b947-074b3c08f041)


### 관리자 기능

- 대화 내용 저장 및 출력, 일정 알림 기능
![image](https://github.com/user-attachments/assets/a2fa15b9-1c7e-44d6-9ca6-8cd7a9dcda37)

- 대화 주제 통계
![image](https://github.com/user-attachments/assets/2277f1b1-49d4-4f35-87cb-59252f6f3994)

![image](https://github.com/user-attachments/assets/81e9cd40-1fa6-4769-a6d3-3b7a6fea03f9)

### Kanban Board 알림
![image](https://github.com/user-attachments/assets/4cb5d921-caa2-43b0-8690-1e18060024c4)

### 기술 조사
Konlpy : https://konlpy.org/ko/latest/index.html

