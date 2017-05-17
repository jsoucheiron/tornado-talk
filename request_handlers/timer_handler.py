from asyncio import sleep
from tornado.ioloop import IOLoop
from tornado.web import Application

from request_handlers.base_request_handler import BaseRequestHandler


class TimerHandler(BaseRequestHandler):
    async def get(self):
        duration = int(self.get_argument('seconds', 10))
        await sleep(duration)
        self.write("Slept for {} seconds".format(duration))


def run():
    IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')
    app = Application(
        [
            (r'/sleep/?', TimerHandler)
        ]
    )
    app.listen(8888)
    IOLoop.current().start()


if __name__ == '__main__':
    run()
