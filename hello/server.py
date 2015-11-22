from tornado import gen
from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer


class HelloHandler(RequestHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        yield gen.sleep(1)
        self.write("hello world")

    def post(self, *args, **kwargs):
        raise Exception()


def make_app():
    return Application([
        (r"/", HelloHandler)
    ])

def get_io_loop():
    return IOLoop.current()

def get_http_server(app):
    return HTTPServer(app)

if __name__ == '__main__':
    app = make_app()
    app.listen(8080)
    get_http_server(app)
    get_io_loop().start()
