from random import choice

from bs4 import BeautifulSoup
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop
from tornado.web import Application

from request_handlers.base_request_handler import BaseRequestHandler


SHARKNADO_IMDB_URLS = {
    '1': 'http://www.imdb.com/title/tt2724064/quotes',
    '2': 'http://www.imdb.com/title/tt3062074/quotes',
    '3': 'http://www.imdb.com/title/tt3899796/quotes',
    '4': 'http://www.imdb.com/title/tt4831420/quotes'
}


class SharknadoQuote(BaseRequestHandler):

    async def _get_quote(self, movie='1'):
        if movie not in SHARKNADO_IMDB_URLS:
            return 'Sorry, no Sharknado {} yet'.format(movie)
        result = await AsyncHTTPClient(max_clients=100).fetch(
            SHARKNADO_IMDB_URLS[movie],
        )
        quote = self._extract_quote_from_body(result.body)
        return quote

    def _extract_quote_from_body(self, body):
        soup = BeautifulSoup(body, 'html.parser')
        sodatexts = soup.find_all(attrs={'class': 'sodatext'})
        random_quote = choice(sodatexts)
        quote = str(random_quote.extract())
        return quote

    async def get(self):
        quote = await self._get_quote(self.get_argument('movie', '1'))
        self.write(quote)


def run():
    app = Application(
        [
            (r"/quote/?", SharknadoQuote),
        ]
    )
    app.listen(8888)
    IOLoop.current().start()


if __name__ == '__main__':
    run()
