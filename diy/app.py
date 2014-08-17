# -*- coding: utf-8 -*-

import os
import sys

import tornado.ioloop
import tornado.web


PRODUCTION = 0
DEVELOPMENT = 9

cwd = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(cwd, "lib"))

environment = PRODUCTION if os.environ.get('OPENSHIFT_APPNAME') else DEVELOPMENT

# settings
settings = {
    "debug": True,
    "template_path": os.path.join(cwd, "templates"),
    "static_path": os.path.join(cwd, "static"),
}
if environment == PRODUCTION:
    settings.update({
        "debug": False
    })


# routing
from handlers import routes

files = [
    (r'/(favicon\.ico)', tornado.web.StaticFileHandler, dict(path=settings['static_path']))
]

application = tornado.web.Application(routes + files, **settings)


def main(ip, port):
    application.listen(port, ip)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    address = "127.0.0.1"
    main(address, 8080)
