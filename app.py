from flask import Flask
from flask_restful import Api

# 【login】登录资源
from API_.resources.Model_Users import UserDetaile,UserList,UserAdd # 【user】用户资源
from API_.resources.Model_Menu import MenuDetaile,MenuList,MenuAdd# 【menu】菜单资源
# 【】权限资源
# 【version】版本资源

app = Flask(__name__)
api = Api(app)

# login


# 用户
api.add_resource(UserAdd, '/user/add') # 新增数据
api.add_resource(UserList, '/user/list') # 列表+条件查询、批量删除
api.add_resource(UserDetaile, '/user/<u_id>') # 删除、查询、更新

# 菜单
api.add_resource(MenuAdd, '/menu/add')              # 新增数据
api.add_resource(MenuList, '/menu/list')            # 列表+条件查询、批量删除
api.add_resource(MenuDetaile, '/menu/<u_id>')       # 删除、查询、更新

# 权限

# 版本

if __name__ == '__main__':
    app.run(debug=True)