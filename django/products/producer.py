import pika

# rabbitmq server url : http://localhost:5672

params = pika.URLParameters('amqps://absrgbxt:zynMVuPUiKpg0kr5VaKvjek_9xfhUHR7@armadillo.rmq.cloudamqp.com/absrgbxt')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='admin', body=b"hello from pika")
