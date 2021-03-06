from tornado.web import Application
from tornado.ioloop import IOLoop

from request_handlers.base_request_handler import BaseRequestHandler


class HelloWorldHandler(BaseRequestHandler):
    def get(self):
        self.write("Hello, world")


def run():
    app = Application(
        [
            (r'/', HelloWorldHandler)
        ]
    )
    app.listen(8888)
    IOLoop.current().start()


if __name__ == '__main__':
    run()
