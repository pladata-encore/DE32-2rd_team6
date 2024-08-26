import threading
from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads
from datetime import datetime
import time
import json
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, Static
from textual.scroll_view import ScrollView

# Kafka 설정
producer = KafkaProducer(
    bootstrap_servers=['ec2-43-203-210-250.ap-northeast-2.compute.amazonaws.com:9092'],
    value_serializer=lambda x: dumps(x, default=str).encode('utf-8')
)

consumer = KafkaConsumer(
    'haha',
    bootstrap_servers=['ec2-43-203-210-250.ap-northeast-2.compute.amazonaws.com:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='chat-group6',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

# 채팅 내역을 저장할 리스트
chatting_history = []

class ChatApp(App):
    def compose(self) -> ComposeResult:
        self.chat_content = Static("")
        self.scroll_view = ScrollView(self.chat_content)

        yield Header()
        yield self.scroll_view
        yield Input(placeholder="Type something...", name="input")
        yield Footer()

    def on_input_submitted(self, message: Input.Submitted) -> None:
        if message.value.strip().lower() == 'exit':
            self.exit()
            return

        # GUI에 새로운 메시지를 추가
#        new_content = f"{self.chat_content.renderable}\nYou: {message.value}"
#        self.chat_content.update(new_content)

        # Kafka 프로듀서를 통해 메시지 전송
        data = {'username': "USER3", 'message': message.value, 'time': time.time()}
        producer.send('haha', value=data)
        producer.flush()

        self.query_one(Input).value = ""
    def on_message_received(self, message):
        sender = message['username']
        formatted_time = datetime.fromtimestamp(message['time']).strftime('%Y-%m-%d %H:%M:%S')
        chat_message = f"(받은 시간 : {formatted_time}) [{sender}]: {message['message']}"
        
        # GUI에 새로운 메시지를 추가
        new_content = f"{self.chat_content.renderable}\n{chat_message}"
        self.chat_content.update(new_content)

def producer_thread():
    try:
        while True:
            # 여기서는 메시지를 입력하지 않음
            time.sleep(1)
    except KeyboardInterrupt:
        print("Producer 종료")
    finally:
        producer.close()

def consumer_thread(app):
    try:
        for m in consumer:
            data = m.value
            # 메시지를 GUI 앱으로 전달
            app.on_message_received(data)
    except KeyboardInterrupt:
        print("Consumer 종료")
    finally:
        consumer.close()

# 스레드와 앱 실행
def main():
    app = ChatApp()
    producer_thread_instance = threading.Thread(target=producer_thread)
    consumer_thread_instance = threading.Thread(target=consumer_thread, args=(app,))

    # 스레드 시작
    producer_thread_instance.start()
    consumer_thread_instance.start()

    # GUI 앱 실행
    app.run()

    # 스레드가 끝날 때까지 기다림
    producer_thread_instance.join()
    consumer_thread_instance.join()

if __name__ == "__main__":
    main()

