from tornado.web import UIModule
from tornado import escape

class custom(UIModule):
    def render(self, *args, **kwargs):
        return 'UIModule result'