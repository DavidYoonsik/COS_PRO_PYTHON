from datetime import date
from tornado import web, escape, ioloop, httpclient, gen
from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor
from confluent_kafka import Consumer, KafkaError

import time
from pprint import pprint
import json

# connect to Kafka server and pass the topic we want to consume

MAX_WORKERS = 126
topic = u'face'


a = 30000
flag = True

class KFK_STREAM_CLS(web.RequestHandler):
    executor = ThreadPoolExecutor()  # max_workers=MAX_WORKERS

    @run_on_executor
    def background(self):

        global flag
        try:
            global a
            a += 1
            consumer = Consumer({
                'bootstrap.servers': "192.168.2.12:9092",
                'group.id': str(a),
                'default.topic.config': {'auto.offset.reset': 'latest'}
            })
            consumer.subscribe([topic])

            while flag:
                msg = consumer.poll()

                if msg:
                    if not msg.error():
                        print('aaa')
                        self.set_header('Cache-Control',
                                        'no-store, no-cache, must-revalidate, pre-check=0, post-check=0, max-age=0')
                        self.set_header('Connection', 'close')
                        self.set_header('Content-Type', 'multipart/x-mixed-replace; boundary=frame')
                        self.write(b"--frame\r\n")
                        self.write(b"Content-type: image/jpg\r\n\r\n")
                        self.write(str(msg.value()))
                        self.write(b"\r\n\r\n")
                        self.flush()

                else:
                    continue


        except Exception as e:
            print(e)
            consumer.close()
            flag = False
            self.on_connection_close()
            self.on_finish()

        finally:
            # Close down consumer to commit final offsets.
            consumer.close()

    @web.asynchronous
    @gen.coroutine
    def get(self):
        try:
            yield self.background()
        except Exception as e:
            print(e)
            pass
        finally:
            self.on_finish()
            self.on_connection_close()
        pass


application = web.Application([
    (r"/", KFK_STREAM_CLS)
])

if __name__ == '__main__':
    port = 5003
    application.listen(port)
    ioloop.IOLoop.instance().start()
    # ioloop.IOLoop.current().start()

