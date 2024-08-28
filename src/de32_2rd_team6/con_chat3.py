from kafka import KafkaConsumer
from json import loads, dump
from datetime import datetime
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

consumer = KafkaConsumer(
        'test',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='chat-group3',
        value_deserializer=lambda x: loads(x.decode('utf8'))
        
)

print("채팅 프로그램 - 메시지 수신")
print("메시지 대기 중...")

chatting_history=[]

try:
    for m in consumer:
        data = m.value
        sender = data['username']
        formatted_time = datetime.fromtimestamp(data['time']).strftime('%Y-%m-%d %H:%M:%S')
        chatting_log={
            'received_time': formatted_time,
            'message': data['message'],
            'sender': sender
        }
        st=f"(받은 시간 : {formatted_time}) [{sender}]: {data['message']}"
        print(st.encode('utf-8', 'ignore').decode('utf-8'))
except KeyboardInterrupt:
    print("채팅 종료")
finally:
    consumer.close()
