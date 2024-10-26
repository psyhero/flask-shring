import json
import re
import time

import requests
from bs4 import BeautifulSoup

from .extentions import db
from .models import UserAgent,Proxy

def get_user_agent_to_db():
    url = 'https://config.net.cn/tools/UserAgent.html'
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content,'lxml')
    blocks = soup.select('div.box1 .panel-body ul:nth-child(2) > *:not(:first-child)')
    data = []
    for it in blocks:
        tag = str(it.select('.input-group input'))
        pattern = r'value="([^"]*)"'
        match = re.search(pattern, tag)
        value = match.group(1)
        ua = UserAgent(
            user_agent = value[11:]
        )
        data.append(ua)
    db.session.add_all(data)
    db.session.commit()

def get_proxy_to_db(amount):
    pages = amount // 12 +1
    for i in range(pages):
        url = f'https://www.kuaidaili.com/free/intr/{i+1}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }
        try:
            response = requests.get(url,headers=headers)
            response.raise_for_status()  # 检查响应状态码，如果失败则抛出异常
            content = response.text
            soup = BeautifulSoup(content, 'lxml')
            scripts = soup.find_all('script')
            for script in scripts:
                script_content = str(script)
                if 'const fpsList' in script_content:
                    fpsList_content = script_content.split('const fpsList = ')[1].split(';')[0]
            data =  json.loads(fpsList_content)
            prs = []
            for it in data:
                pr = Proxy(
                    ip = it['ip'],
                    port = int(it['port']),
                    last_check_time = it['last_check_time']
                )
                prs.append(pr)
            db.session.add_all(prs)
            db.session.commit()
            time.sleep(5)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")