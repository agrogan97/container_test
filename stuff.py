from kafka import KafkaProducer
import time
# producer = KafkaProducer(bootstrap_servers='my-cluster-kafka-1:9092')
# producer.send('sample', b'Hello, World!')
# producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')
a = 0
while True:
    print("Hello - %d" % (a))
    a = a + 1
    time.sleep(2)