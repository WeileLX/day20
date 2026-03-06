#FLASK 小蓝图

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = 'fdasijfas89f8duasf9834huf9322e2'
    from .views import account
    from .views import order
    app.register_blueprint(order.od)
    app.register_blueprint(account.ac)

    return app