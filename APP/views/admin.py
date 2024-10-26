
from flask import Blueprint

from ..spider import get_user_agent_to_db,get_proxy_to_db

badmin = Blueprint('admin',__name__)

@badmin.route('/test')
def test():
    url = 'https://www.bilibili.com/video/BV1g74TefEp2/?spm_id_from=333.337.search-card.all.click&vd_source=8412a41bcfce475bc1df1ac2f30d2ec6'

    return 'Video played.'

@badmin.route('/useragent')
def user_agent():
    get_user_agent_to_db()
    return 'success'

@badmin.route('/proxy')
def proxy():
    get_proxy_to_db(500)
    return 'success'