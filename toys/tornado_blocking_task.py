# coding=utf-8
"""
Ref:
    https://gist.github.com/methane/2185380

测试方法:
    curl 'http://127.0.0.1:8888/' &
    curl 'http://127.0.0.1:8888/' &
    curl 'http://127.0.0.1:8888/' &
    curl 'http://127.0.0.1:8888/' &
    curl 'http://127.0.0.1:8888/hello' &
    curl 'http://127.0.0.1:8888/hello' &
    curl 'http://127.0.0.1:8888/hello' &
    curl 'http://127.0.0.1:8888/hello' &
"""
import time
import functools

import tornado.ioloop
import tornado.web
import tornado.options
from concurrent.futures import ThreadPoolExecutor   # `pip install futures` for python2


MAX_WORKERS = 2
GLOBE_EXECUTOR = ThreadPoolExecutor(max_workers=MAX_WORKERS)


def run_on_executor(method):
    """copy from tornado.concurrent, using special executor"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        callback = kwargs.pop("callback", None)
        executor = kwargs.pop("executor", None) or self.executor
        future = executor.submit(method, self, *args, **kwargs)
        if callback:
            self.io_loop.add_future(future,
                                    lambda future: callback(future.result()))
        return future
    return wrapper


class MainHandler(tornado.web.RequestHandler):
    @run_on_executor
    def background_task(self, variable):
        """ This will be executed in `executor` pool. """
        time.sleep(10)
        return variable + " work"

    @tornado.gen.coroutine
    def get(self):
        """ Request that asynchronously calls background task. """
        res = yield self.background_task("get", executor=GLOBE_EXECUTOR)
        self.write(res)


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")


def make_app():
    return tornado.web.Application([
        (r"/?", MainHandler),
        (r"/hello/?", HelloHandler),
    ])


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
