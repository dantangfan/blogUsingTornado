#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import tornado
from tornado import web
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options, define

from urls import handlers, sub_handlers, ui_modules

define('port', default=8000, help='run on the given port', type=int)


class Application(web.Application):
    def __init__(self):
        settings = dict(
            debug=True,
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            cookie_secret="you will never guess",
            login_url='/login',
            autoescape=None,
            ui_modules=ui_modules,
        )
        super(Application, self).__init__(handlers, **settings)


def main():
    tornado.options.parse_command_line()
    http_server = HTTPServer(Application(), xheaders=True).listen(options.port)
    IOLoop.instance().start()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt, e:
        print 'Quit server'