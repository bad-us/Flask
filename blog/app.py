# from flask import Flask
# from flask import request
#
# app = Flask(__name__)
#
#
# @app.route('/<string:search>', methods=['GET', 'POST'])
# def index(search: str):
#     # name = request.args.get('search', None)
#     # return f'Hello {request.method}'
#
#     if request.method == 'GET':
#         return f'This is a {request.method} request'
#     elif request.method == 'POST':
#         return f'This is a {request.method} request'
from flask import Flask

from blog.report.views import report
from blog.user.views import user

def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app

def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)
