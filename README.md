# flask-shring

### 主要特性
- 邮件注册与登录；
- selenium播放任务（线程池）；
- spider获取driver所需的代理和User-Agent；

## 上手指南
###  开发前的配置要求
1.修改配置文件config.py中的设置：
```sh
# DB config
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/db'

# session config
SECRET_KEY = 'my_secret_key'
PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=10)

# mail config
MAIL_SERVER = 'smtp.xxx.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'xxx@x.com'
MAIL_PASSWORD = 'email token'

# wxpay config
WXPAY_MCHID = 'your_merchant_id'
WXPAY_KEY = 'your_merchant_key'
WXPAY_NOTIFY_URL = 'your_notify_url'

# alipay config
ALIPAY_SERVER_URL = 'https://openapi-sandbox.dl.alipaydev.com/gateway.do'
ALIPAY_APP_ID = '9021000100000000'
APP_PRIVATE_KEY = ''
ALIPAY_PUBLIC_KEY = ''
ALIPAY_RETURN_URL = None
ALIPAY_NOTIFY_URL = None
```
## 项目结构
```
filetree 
├── APP
|  ├──static
|  ├──templates
|  ├──views  视图函数
|  ├──__init__.py
|  ├──alipay.py  支付宝接口
|  ├──config.py
|  ├──decorator.py  装饰器
|  ├──extentions.py
|  ├──models.py
|  ├──spider.py  爬虫：Proxy、UA
|  ├──worker.py  验证邮件、任务函数等
├──app.py
├──requirements.txt
```
## 版权说明
该项目签署了MIT 授权许可，详情请参阅 LICENSE.txt

## 待解决问题
1、支付接口（微信、支付宝）
2、admin页面、视图等




