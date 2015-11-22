# from motor import MotorClient
from tornado import testing
from tornado.ioloop import IOLoop
from tornado.testing import gen_test
from hello import server
# from tornado.httpclient import AsyncHTTPClient
#
# __author__ = 'alay'
#
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
    def test_home(self):
        response = yield self.http_client.fetch(self.get_url('/'))
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, "hello world")

