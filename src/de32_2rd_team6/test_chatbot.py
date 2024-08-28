import os
import json
from kafka import KafkaConsumer, KafkaProducer

# 모든 year=nnnn 디렉터리를 순회하며 영화 데이터를 검색하는 함수
def search_movie_in_directories(base_dir, movie_name):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.json'):
                json_file_path = os.path.join(root, file)
                with open(json_file_path, 'r', encoding='utf-8') as f:
                    movies = json.load(f)
                    for movie in movies:
                        if movie['movieNm'] == movie_name:
                            return movie
    return None

# Kafka producer를 설정하는 함수
def send_response_to_kafka(response_message):
    producer = KafkaProducer(
        bootstrap_servers=['ec2-43-203-210-250.ap-northeast-2.compute.amazonaws.com:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send('haha', value=response_message)
    producer.flush()
    producer.close()

# Kafka 메시지를 소비하고, 영화 데이터를 검색한 후, 응답을 전송하는 함수
def consume_messages():
    consumer = KafkaConsumer(
        'haha',
        bootstrap_servers=['ec2-43-203-210-250.ap-northeast-2.compute.amazonaws.com:9092'],
        auto_offset_reset='earliest',
        #enable_auto_commit=True,
        #group_id='chatbot-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    base_dir = '/home/esthercho/code/mdata/data/movies'  # 영화 데이터가 저장된 기본 디렉터리

    for message in consumer:
        data = message.value
        if 'message' in data:
            user_input = data['message']
            if user_input.startswith('@챗봇'):
                movie_name = user_input.split('@챗봇', 1)[-1].strip()
                movie_data = search_movie_in_directories(base_dir, movie_name)
                if movie_data:
                    response = {"status": "success", "data": movie_data}
                else:
                    response = {"status": "error", "message": f"영화 '{movie_name}'를 찾을 수 없습니다."}
                
                # 결과를 출력하고, Kafka로 전송
                send_response_to_kafka(response)

if __name__ == "__main__":
    consume_messages()

