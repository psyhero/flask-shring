import os

from flask import Flask

from APP import config
from .extentions import init_exts
from .views.index import blue
from .views.admin import badmin
from .views.user import buser
from .views.order import border
from .views.pay import bpay

def create_app():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    static_folder = os.path.join(BASE_DIR,'static')
    template_folder = os.path.join(BASE_DIR,'templates')

    app = Flask(
            __name__,
            static_folder=static_folder,
            template_folder=template_folder
    )

    app.config.from_object(config)

    app.register_blueprint(blueprint=blue)
    app.register_blueprint(blueprint=badmin)
    app.register_blueprint(blueprint=buser)
    app.register_blueprint(blueprint=border)
    app.register_blueprint(blueprint=bpay)

    init_exts(app=app)

    return app

