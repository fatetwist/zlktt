# encoding=utf-8
import os
from datetime import timedelta


DEBUG = True
SECRET_KEY = os.urandom(16)
# 配置数据库
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
SQLALCHEMY_COMMIT_TEARDOWN = True


# 设置session过期时间
PERMANENT_SESSION_LIFETIME = timedelta(days=7)

