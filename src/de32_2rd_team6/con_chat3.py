from kafka import KafkaConsumer
from json import loads, dump, json
from datetime import datetime
consumer = KafkaConsumer(
        'chat',
        bootstrap_servers=['ec2-43-203-210-250.ap-northeast-2.compute.amazonaws.com:9092'],
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
        formatted_time = datetime.fromtimestamp(data['time']).strftime('%Y-%m-%d %H:%M:%S')
        chatting_log={
            'received_time': formatted_time,
            'message': data['message'],
            'sender': 'FRIEND'
        }

        print(f"(받은 시간 : {formatted_time}) [FRIEND]: {data['message']}")
        chatting_history.append(chatting_log)
except KeyboardInterrupt:
    print("채팅 종료")
finally:
    consumer.close()

    with open('chatting_log.json', 'w', encoding='utf-8') as file:
        json.dump(chatting_history, file, indent=4, ensure_ascii=False)
