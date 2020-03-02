import tornado.ioloop
import tornado.web

from handlers import user as user_handlers

HANDLERS = [
    (r"/api/users", user_handlers.UserListHandler),
    (r"/api/users/(\d+)", user_handlers.UserHandler),      # 使用正则匹配user_id
]


def run():
    app = tornado.web.Application(
        HANDLERS,
        debug=True,
    )

    http_server = tornado.httpserver.HTTPServer(app)
    port = 8888
    http_server.listen(port)

    print(f"\n server start on port:{port}...")

    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    run()
