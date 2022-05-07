from flask_bootstrap import Bootstrap4
from flask_wtf import CSRFProtect
from flask_apscheduler import APScheduler

bootstrap = Bootstrap4()
csrf = CSRFProtect()
scheduler = APScheduler()