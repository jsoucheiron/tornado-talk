from tornado.web import RequestHandler


class HelloWorldHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")
