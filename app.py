from flask import Flask
from flask_restful import Api

from API_.resources.model_Users import UserResource # 用户资源
# 菜单资源
# 权限资源
# 版本资源

app = Flask(__name__)
api = Api(app)






# 用户
api.add_resource(UserResource, '/user/<string:username>')

# 菜单

# 权限

# 版本

if __name__ == '__main__':
    app.run(debug=True)