import pika

# rabbitmq server url : http://localhost:5672

params = pika.URLParameters('amqps://absrgbxt:zynMVuPUiKpg0kr5VaKvjek_9xfhUHR7@armadillo.rmq.cloudamqp.com/absrgbxt')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('received in admin')
    print(body)
    pass


channel.basic_consume(queue='admin', on_message_callback=callback)

print('started consuming')

channel.start_consuming()
# print('consumer stop')
channel.close()