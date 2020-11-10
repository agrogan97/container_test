from kafka import KafkaProducer
import time
a = 0
while True:
    producer = KafkaProducer(bootstrap_servers='my-cluster-kafka-bootstrap:9092')
    producer.send('sample', b'Hello, World!')
    producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')