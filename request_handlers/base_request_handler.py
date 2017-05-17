from tornado.web import RequestHandler


class BaseRequestHandler(RequestHandler):

    def __init__(self, *args, **kwargs):
        self._start_time = None
        super().__init__(*args, *kwargs)

    def on_finish(self):
        super().on_finish()
        self._send_metrics()

    def _send_metrics(self):
        print("The request to {} took {:.2f}s and had a {} status".format(
            self.request.uri, self.request.request_time(), self.get_status()))
