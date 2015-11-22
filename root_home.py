import time
from tornado import testing
from tornado.ioloop import IOLoop
from tornado.testing import gen_test
from hello import server

class MyTestCase(testing.AsyncHTTPTestCase):
    def get_app(self):
        return server.make_app()

    def get_http_port(self):
        return 8080

    def get_new_ioloop(self):
        return IOLoop.current()

    def get_http_server(self):
        return server.get_http_server(self._app)

    @gen_test
    def test_home_get(self):
        start = time.time()
        response = yield self.http_client.fetch(self.get_url('/'))
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b"hello world")
        self.assertAlmostEqual(time.time() - start, 1, places=1)

    @gen_test
    def test_home_post(self):
        with self.assertRaises(Exception) as error:
            _ = yield self.http_client.fetch(self.get_url("/"), method="Post")
            print(error)
            return
