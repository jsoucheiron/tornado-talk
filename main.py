import asyncio

from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.httpserver import HTTPServer

import uvloop

from request_handlers.hello_name import HelloNameHandler
from request_handlers.hello_world import HelloWorldHandler
from request_handlers.timer_handler import TimerHandler
from request_handlers.sharknado import SharknadoQuote


def run():
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')
    app = Application([
        (r'/', HelloWorldHandler),
        (r"/quote", SharknadoQuote),
        (r'/sleep/?', TimerHandler),
        (r'/(?P<name>.+)', HelloNameHandler)
    ])
    server = HTTPServer(app)
    server.bind(8888)
    server.start(0)
    IOLoop.current().start()


if __name__ == "__main__":
    run()
