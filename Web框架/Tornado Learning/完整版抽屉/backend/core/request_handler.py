import tornado.web
from ..session.session import SessionFactory


class BaseRequestHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session = SessionFactory.get_session_obj(self)


class BaseResponse:
    def __init__(self):
        self.status = False  # 状态信息，是否注册成功，是否登陆成功，是否点赞成功、是否评论成功等
        self.code = StatusCodeEnum.Success
        self.data = None  # 前端需要展示的数据
        self.summary = None  # 错误信息
        self.message = {}  # 字典类型的错误信息