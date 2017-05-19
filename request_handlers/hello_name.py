from tornado.web import Application
from tornado.ioloop import IOLoop

from request_handlers.base_request_handler import BaseRequestHandler


class HelloNameHandler(BaseRequestHandler):
    def get(self, name):
        self.write("Hello, {}".format(name))


def run():
    app = Application(
        [
            (r'/hello/(?P<name>.+)/?', HelloNameHandler)
        ]
    )
    app.listen(8888)
    IOLoop.current().start()


if __name__ == '__main__':
    run()
