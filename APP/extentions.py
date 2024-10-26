from concurrent.futures import ThreadPoolExecutor

from flask_caching import Cache
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_wxpay import WXPay

# from .alipay import AlipayModel

pool = ThreadPoolExecutor(max_workers=5)

db = SQLAlchemy()
migrate = Migrate()
cache = Cache(config={'CACHE_TYPE':'simple'})
mail = Mail()
# wxpay = WXPay()
# alipay = AlipayModel()

def init_exts(app):
    db.init_app(app=app)
    migrate.init_app(app=app,db=db)
    cache.init_app(app=app)
    mail.init_app(app=app)