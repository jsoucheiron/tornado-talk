from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.httpserver import HTTPServer

from request_handlers.hello_world import HelloWorldHandler
from request_handlers.timer_handler import TimerHandler

if __name__ == "__main__":
    app = Application([
        (r"/hello-world", HelloWorldHandler),
        (r"/timer", TimerHandler),
    ])
    server = HTTPServer(app)
    server.bind(8888)
    server.start(0)
    IOLoop.current().start()

