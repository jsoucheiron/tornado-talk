from tornado.gen import coroutine, sleep
from tornado.web import RequestHandler


class TimerHandler(RequestHandler):
    @coroutine
    def get(self):
        duration = int(self.get_argument('seconds', 10))
        yield sleep(duration)
        self.write("Slept for {} seconds".format(duration))
