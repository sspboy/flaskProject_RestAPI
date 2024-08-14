# 基础设置setting路由
from flask import Blueprint
from flask_restful import Api

from API_.resources.BasicSettings.Model_Brandinf import BrandDetaile        # 【user】品牌用户查询、编辑资源
from API_.resources.BasicSettings.Model_Role import RoleAdd,RoleList,RoleDetaile        # 【role】角色资源
from API_.resources.BasicSettings.Model_Team import TeamAdd,TeamList,TeamDetaile        # 【role】团队资源
from API_.resources.BasicSettings.Model_Department import DepartmentAdd,DepartmentList,DepartmentDetaile # 【department】部门资源

setting_blueprint = Blueprint('setting', __name__)

api = Api(setting_blueprint)


# 品牌信息[编辑、查询]
api.add_resource(BrandDetaile, '/brand/<u_id>')

# 角色管理
api.add_resource(RoleAdd, '/role/add')
api.add_resource(RoleList, '/role/list')
api.add_resource(RoleDetaile, '/role/<u_id>')

# 组织架构
api.add_resource(DepartmentAdd, '/department/add')
api.add_resource(DepartmentList, '/department/list')
api.add_resource(DepartmentDetaile, '/department/<u_id>')

# 团队管理
api.add_resource(TeamAdd, '/team/add')
api.add_resource(TeamList, '/team/list')
api.add_resource(TeamDetaile, '/team/<u_id>')

# ------------------ #

# 素材库管理

# 产品-视频混剪

# 产品-智能图文

# 内容批量发布

# 评论管理

# 私信管理

# 群管理

# 群通知

# 留资卡片

# 数据分析




