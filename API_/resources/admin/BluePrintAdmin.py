from flask import Blueprint
from flask_restful import Api

from API_.resources.admin.Model_Users import UserDetaile,UserList,UserAdd               # 【user】用户资源
from API_.resources.admin.Model_Menu import MenuDetaile,MenuList,MenuAdd                # 【menu】菜单资源
from API_.resources.admin.Model_Version import VersionDetaile,VersionList,VersionAdd    # 【version】版本资源
from API_.resources.admin.Model_Fun import FunDetaile,FunList,FunAdd                    # 【function】功能权限资源


admin_blueprint = Blueprint('admin', __name__)

api = Api(admin_blueprint)

# 登录管理后台


# 用户
api.add_resource(UserAdd, '/user/add')              # 新增
api.add_resource(UserList, '/user/list')            # 列表+条件查询、批量删除
api.add_resource(UserDetaile, '/user/<u_id>')       # 删除、查询、更新

# 菜单
api.add_resource(MenuAdd, '/menu/add')
api.add_resource(MenuList, '/menu/list')
api.add_resource(MenuDetaile, '/menu/<u_id>')

# 版本
api.add_resource(VersionAdd, '/version/add')
api.add_resource(VersionList, '/version/list')
api.add_resource(VersionDetaile, '/version/<u_id>')

# 功能
api.add_resource(FunAdd, '/function/add')
api.add_resource(FunList, '/function/list')
api.add_resource(FunDetaile, '/function/<u_id>')
