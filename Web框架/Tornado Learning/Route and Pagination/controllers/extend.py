import tornado.web


class ExtendIndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('extend/index.html')


class ExtendHomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('extend/home bak.html')