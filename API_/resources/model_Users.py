from flask_restful import fields,Resource,marshal_with
# 定义一个模型
class Users:
    def __init__(self, username, email):
        self.username = username
        self.email = email

# 定义字段
user_fields = {
    'username': fields.String,
    'email': fields.String
}

# 创建资源
class UserResource(Resource):
    @marshal_with(user_fields)
    def get(self, username):
        # 假设这里从数据库获取用户信息
        user = Users(username=username, email='user@example.com')
        return user