import logging
import sys

from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.httpserver import HTTPServer

from request_handlers.hello_world import HelloWorldHandler
from request_handlers.timer_handler import TimerHandler
from request_handlers.sharknado import SharknadoQuote

if __name__ == "__main__":
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(formatter)
    log.addHandler(ch)

    app = Application([
        (r"/hello-world", HelloWorldHandler),
        (r"/timer", TimerHandler),
        (r"/quote", SharknadoQuote),
    ])
    server = HTTPServer(app)
    server.bind(8888)
    server.start(0)
    IOLoop.current().start()

