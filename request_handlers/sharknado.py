from random import choice
from uuid import uuid4
import logging
import time

from tornado.web import RequestHandler
from tornado.httpclient import AsyncHTTPClient
from bs4 import BeautifulSoup



SHARKNADO_IMDB_URL = 'http://www.imdb.com/title/tt2724064/quotes'


class SharknadoQuote(RequestHandler):

    async def _get_quote(self):
        result = await AsyncHTTPClient(max_clients=100).fetch(SHARKNADO_IMDB_URL)
        soup = BeautifulSoup(result.body, 'html.parser')
        sodatexts = soup.body.find_all(class_=r'sodatext')
        random_quote = choice(sodatexts)
        return str(random_quote.extract())

    def __init__(self, *args, **kwargs):
        self._request_id = uuid4()
        self._start = time.time()
        self.logger = logging.getLogger("SharknadoQuote")
        super(SharknadoQuote, self).__init__(*args, **kwargs)

    def initialize(self):
        self.logger.info("Request with id {} initialized".format(self._request_id))

    async def get(self):
        quote = await self._get_quote()
        self.write(quote)

    def on_finish(self):
        self.logger.info("Request with id {} finished in {}s".format(
            self._request_id,
            time.time() - self._start
        ))

