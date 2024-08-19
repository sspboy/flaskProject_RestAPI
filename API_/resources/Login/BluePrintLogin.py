from flask import Blueprint # 蓝图
from flask_restful import Api

# 引入登录路由资源

from API_.resources.Login.Model_Login import Login,LoginOut

login_blueprint = Blueprint('login', __name__)

api = Api(login_blueprint)


# 验证登录
api.add_resource(Login, '')

# 登出用户
api.add_resource(LoginOut, '/out')