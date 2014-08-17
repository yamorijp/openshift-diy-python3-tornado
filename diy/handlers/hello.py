# -*- coding: utf-8 -*-
# Copyright 

import sys

from tornado import gen, web
from tornado.httpclient import AsyncHTTPClient
import tornado


class Hello(web.RequestHandler):
    @gen.coroutine
    def get(self):
        cli = AsyncHTTPClient()
        responses = yield [cli.fetch("http://www.twitter.com"), cli.fetch("http://www.facebook.com")]
        for response in responses:
            if response.code != 200:
                raise tornado.web.HTTPError()

        self.render("hello.html",
                    python_version=sys.version, tornado_version=tornado.version,
                    coroutine="ok")


routes = [
    web.url(r"/", Hello)
]