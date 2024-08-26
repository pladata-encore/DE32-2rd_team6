from kafka import KafkaProducer
from json import dumps
import time
#from datetime import time, timedelta, datetime

p = KafkaProducer(
    bootstrap_servers=['ec2-43-203-210-250.ap-northeast-2.compute.amazonaws.com:9092'],
    value_serializer = lambda x:dumps(x,default=str).encode('utf-8')
)

print("채팅 프로그램- 메시지 발신자")
print("메시지를 입력하세요. (종료시 'exit' 입력)")

while True:
    username = "USER4"
    msg = input(f"{username}: ")
    if msg.lower() == 'exit':
        break
    data = {'username' : username, 'message' : msg, 'time' : time.time()}
    p.send('haha', value = data)
    p.flush()
