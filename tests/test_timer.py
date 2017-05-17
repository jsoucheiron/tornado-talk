from unittest.mock import patch

from asynctest.mock import patch as asyncpatch
from tornado.gen import Future
from tornado.ioloop import IOLoop
from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application

from request_handlers.timer_handler import TimerHandler


class TestTimerHandler(AsyncHTTPTestCase):

    def setUp(self):
        IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')
        super().setUp()

    def get_app(self):
        return Application([
            (r"/timer", TimerHandler),
        ])

    def test_sleep1(self):
        response = self.fetch('/timer?seconds=1')
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b'Slept for 1 seconds')

    def test_default_sleep(self):
        # Tests timeout after 5s by default
        self.assertRaises(AssertionError, self.fetch, '/timer')

    @patch('request_handlers.timer_handler.sleep')
    def test_default_sleep_manual_mock(self, sleep_mock):
        # We need to wrap the mock in a Future
        mock_future = Future()
        mock_future.set_result(None)
        sleep_mock.return_value = mock_future
        response = self.fetch('/timer?seconds=10')
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b'Slept for 10 seconds')
        sleep_mock.assert_called_once_with(10)

    @asyncpatch('request_handlers.timer_handler.sleep')
    def test_default_sleep_manual_mock_asynctest(self, sleep_mock):
        # Using asynctest we don't need to wrap the mock in a Future anymore
        response = self.fetch('/timer?seconds=10')
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b'Slept for 10 seconds')
        sleep_mock.assert_called_once_with(10)
