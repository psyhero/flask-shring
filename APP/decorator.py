
from .extentions import db
from .models import VideoPlay

def save_to_videoplay(func):
    def inner(*args,**kwargs):
        from APP import create_app
        with create_app().app_context():
            data = func(*args,**kwargs)
            vps = []
            for it in data:
                vp = VideoPlay(
                    oid = it['oid'],
                    url = it['url'],
                    proxy = it['proxy'],
                    user_agent = it['user_agent'],
                    play_time = it['play_time']
                )
                vps.append(vp)
            try:
                db.session.add_all(vps)
                db.session.commit()
            except Exception:
                db.session.rollback()
                raise Exception
    return inner