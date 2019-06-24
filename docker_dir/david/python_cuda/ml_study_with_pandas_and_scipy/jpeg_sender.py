from kiel import clients
from tornado import gen, ioloop


@gen.coroutine
def consume():
    c = clients.SingleConsumer(brokers=["192.168.2.12:9096"])

    yield c.connect()

    while True:
        msgs = yield c.consume("test1test")
        for msg in msgs:
            print(msg)


def run():
    loop = ioloop.IOloop.instance()

    loop.add_callback(consume)

    try:
        loop.start()
    except KeyboardInterrupt:
        loop.stop()


if __name__ == "__main__":
    run()