import datetime

# DB config
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/db'
SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_MAX_OVERFLOW = 20
SQLALCHEMY_TRACK_MODIFICATIONS = False

# session config
SECRET_KEY = 'my_secret_key'
PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=10)

# mail config
MAIL_SERVER = 'smtp.xxx.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'xxx@x.com'
MAIL_PASSWORD = 'email_token'

# wxpay config
WXPAY_MCHID = 'your_merchant_id'
WXPAY_KEY = 'your_merchant_key'
WXPAY_NOTIFY_URL = 'your_notify_url'

# alipay config
ALIPAY_SERVER_URL = 'https://openapi-sandbox.dl.alipaydev.com/gateway.do'
ALIPAY_APP_ID = '9021000100000'
APP_PRIVATE_KEY = 'APP_PRIVATE_KEY'
ALIPAY_PUBLIC_KEY = 'ALIPAY_PUBLIC_KEY'
ALIPAY_RETURN_URL = None
ALIPAY_NOTIFY_URL = None
