import tornado.web
from commons.pagination import Pagination

INFO_LIST = [
    {'name': 'yeff', 'age': '23'},
]
for i in range(99):
    INFO_LIST.append({
        'name': 'a'+str(i), 'age': '0'+str(i)
    })





class IndexHandler(tornado.web.RequestHandler):
    def get(self, page):
        pn = Pagination(page, 5, INFO_LIST)
        str_pages = pn.get('/index')
        display_list = pn.items[pn.start_item:pn.end_item]
        self.render("home/index.html", info_list=display_list, current_page=page, page_nums=str_pages)

    def post(self, page):
        # 之前提交时，action连接的是/index，因此在没有添加current_page参数之前，page都只会为空字符串
        name = self.get_argument('name')
        age = self.get_argument('age')
        _dic = {'name': name, 'age': age}
        INFO_LIST.append(_dic)
        self.redirect("/index/" + page)
