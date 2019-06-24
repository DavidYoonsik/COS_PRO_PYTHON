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
topic = u'test1test'

qi = -1
a = 10000
flag = True

class KFK_STREAM_CLS(web.RequestHandler):
    # executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)  # max_workers=MAX_WORKERS

    # @run_on_executor
    @gen.coroutine
    def background(self):

        global flag
        global qi

        suricata_stack = [
            ("/usr/local/etc/suricata/suricata1.yaml", "/home/var/pcap/eve1.json"),
            ("/usr/local/etc/suricata/suricata2.yaml", "/home/var/pcap/eve2.json"),
            ("/usr/local/etc/suricata/suricata3.yaml", "/home/var/pcap/eve3.json"),
            ("/usr/local/etc/suricata/suricata4.yaml", "/home/var/pcap/eve4.json"),
            ("/usr/local/etc/suricata/suricata5.yaml", "/home/var/pcap/eve5.json")
        ]

        qi = (qi + 1) % len(suricata_stack)
        item = suricata_stack[qi]

        try:
            with subprocess.Popen("suricata -c " + item[0] + " -r ./bigFlows.pcap", shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE) as pf:
                x, y = pf.communicate()
                x = x.decode('utf-8').strip()
                y = y.decode('utf-8').strip()
                print(x)
                print(y)
                
            self.write(str(x) + "\n\r" + str(y))
            self.flush()

        except Exception as e:
            print(e)
            # consumer.close()
            flag = False
            self.on_connection_close()
            self.on_finish()

        finally:
            pass

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
    port = 5002
    application.listen(port)
    ioloop.IOLoop.instance().start()
    # ioloop.IOLoop.current().start()

