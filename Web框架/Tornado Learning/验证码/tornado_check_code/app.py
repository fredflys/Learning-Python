#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import io
import check_code

class CheckCodeHandler(tornado.web.RequestHandler):
    def get(self):
        mstream = io.BytesIO()
        img, code = check_code.create_validate_code()
        img.save(mstream, "GIF")
        # self.session["CheckCode"] = code
        print(mstream.getvalue())
        self.write(mstream.getvalue())

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

settings = {
    'template_path': 'template',
    'static_path': 'statics',
    'static_url_prefix': '/statics/',
    'cookie_secret': 'aiuasdhflashjdfoiuashdfiuh',
}

application = tornado.web.Application([
    (r"/index", MainHandler),
    (r"/check_code", CheckCodeHandler),
], **settings)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()