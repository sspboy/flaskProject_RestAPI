from flask_restful import Resource                      # 接口处理方法
from API_.DB.DB_model import Basic_Operations           # 数据查询方法
from API_.DB.Data_con import *                          # 数据库操作方法
from API_.resources.admin.Model_Menu import menu_list   # 菜单数据转义方法
from API_.resources.admin.Model_Version import version_list   # 菜单数据转义方法
from flask import request,session
from flask_login import UserMixin,LoginManager,login_user,logout_user,login_required
import json, re


login_manager = LoginManager()                      # 初始化一个 LoginManager 类对象
login_manager.login_message_category = 'info'       # 消息类别，默认是 ‘message’
login_manager.login_message = 'Access denied.'      # 用户未登录时显示的消息；
login_manager.session_protection = "strong"


# 定义【user】模版
class User(UserMixin):
    def __init__(self, id, username, password, account_type, user_obj):
        self.id = id
        self.username = username
        self.password = password
        self.account_type = account_type
        self.user_obj = user_obj


# 数据库查询用户信息
class LoadingUser():

    def __init__(self, username):

        self.username = username

    # 判断用户返回用户信息：管理员、主账号、子账号
    def get_user_obj(self):

        user_type = self.hold_user_type() # 判断用户

        if user_type == 'admin':     # 【后台管理员】【主账号】
            # 载入管理员菜单权限
            user_data = self.get_admin_data()
            return user_data

        elif user_type == 'member':   # 【子账号】
            # 载入主张号菜单权限
            pass


    # 通过用户名称识别用户类别：
    def hold_user_type(self):
        search_res = re.search(':', self.username)

        if search_res == None:
            return 'admin'
        else:
            return 'member'

    # def get_user_obj(self):     # 根据 username 查询用户详情信息
    #     user = Basic_Operations('user')
    #     res = user.detaile(self.username)
    #     detaile_data = _list().re_detaile_data_name(res)
    #     return detaile_data

    # 【获取主账号数据】# 用户信息+版本信息+全部菜单
    def get_admin_data(self):

        sql = "SELECT * FROM (user INNER JOIN version ON user.v_id = version.id and user.id='%s') INNER JOIN menu" % self.username

        res = Data().select(sql)

        if len(res) == 0:
            return 'None'
        else:

            user_data = self.get_user_data(res)                             # 获取用户信息

            version_data = self.get_version_data(res)                       # 获取版本信息

            all_menu_list = self.get_menu_data(res)                         # 获取所有菜单列表

            super_menu = self.get_menu_child_list(all_menu_list)            # 【后台管理员】菜单、权限

            admin_menu = self.get_admin_menu(all_menu_list, version_data)   # 【主账号】菜单、权限

            account_type = user_data.get('account_type')

            if account_type == '2': # 管理员

                user_data['menu'] = super_menu.copy()

            elif account_type == '0':# 主账号

                user_data['menu'] = admin_menu.copy()

            return user_data

    # 用户信息
    def get_user_data(self,data):
        user_data = _list().re_detaile_data_name(list(data[0])[:14])
        return user_data

    # 版本信息
    def get_version_data(self,data):
        ver_data = version_list().re_detaile_data_name(list(data[0])[14:26])
        return ver_data

    # 【全部菜单信息】
    def get_menu_data(self,data):
        res_data_list = []
        for i in data:
            res_data_list.append(i[23:33])
        menu_data_list = menu_list().re_data_list_name(res_data_list)
        return menu_data_list

    # 获取后台管理员菜单：全部菜单+全部权限
    def get_menu_child_list(self, data):

        first_list = []  # 一级菜单
        for i in data:
            if i.get('parent_id') == '0':
                first_list.append(i.copy())

        for z in first_list:
            id = z.get('id')
            c_list = []
            for y in data:
                if y.get('parent_id') == str(id):
                    c_list.append(y)
            z['child'] = c_list

        return first_list

    # 获取主账号菜单：：无管理后台：：过滤版本中没有的菜单
    def get_admin_menu(self, all_menu_list, version_data):
        # 版本菜单id
        menu_setting = version_data.get('menu_setting')
        menu_setting_list = json.loads(menu_setting)

        # 当前版本绑定的所有菜单
        ver_menu_list = []
        for i in all_menu_list:
            if str(i.get('id')) in menu_setting_list:
                ver_menu_list.append(i.copy())

        # 当前版本所有菜单
        for d in ver_menu_list:
            parent_id = d.get('parent_id')
            if parent_id != 0:
                for z in all_menu_list:
                    if str(z.get('id')) == parent_id and z not in ver_menu_list:
                        ver_menu_list.append(z.copy())

        admin_menu_list = self.get_menu_child_list(ver_menu_list)

        return admin_menu_list


    # 【获取子账号数据】
    def get_member_data(self):
        sql = ''
        member_menu = '' # 子账号菜单
        pass


    # 获取子账号菜单：：过滤权限配置中不存在的菜单和功能
    def get_member_menu(self):
        # 获取角色：：# 通过角色获取绑定的菜单
        # 获取父标签
        # 根据父标签载入子标签
        pass

    # 【角色信息】
    def get_role(self):
        pass


    # 【数据权限】
    def get_data_pemiss(self):
        pass

    # 【管理员】！无需版本信息：：！无需角色权限：：！无需菜单权限：：：！无需数据权限：：

    # 【主账号】！无需角色权限：：！无需菜单权限：：：！无需数据权限：：

    # 【子账号】通过用户id查询，角色列表：：：一条对多条：：合并后等待菜单权限+数据权限




# 请求视图加载用户====定义用户信息
@login_manager.user_loader
def user_loader(username):

    load = LoadingUser(username)        # 初始化user表操作

    user_obj = load.get_user_obj()      # 从数据库或 读取[用户信息]

    if user_obj == 'None':  # 用户名为空，用户不存在

        return 'None'

    elif user_obj != 'None':  # 存户名不为空，用户存在

        id = user_obj.get('id')  # 用户对象定义id

        username = user_obj.get('nickname')  # 用户对象定义品牌-id

        password = user_obj.get('pass_word')  # 用户对象-定义密码

        account_type = user_obj.get('account_type')   # 账号类型

        user = User(id, username, password, account_type, user_obj)

        return user


# 定义【user输出格式】模型：数据查询
class _list:


    def __init__(self):      # 列表数据
        self.table_name = 'user'
        # 数据表头名称、数据类型、描述说明
        self.DataColumn =[
            {
                "field_name": "b_id",   # 字段名称
                "field_type": "int",    # 字段类型
                "remark": "品牌id",      # 备注描述
            },
            {"field_name": "account_type", "field_type": "int", "remark": "账号类型"},
            {"field_name": "id", "field_type": "str", "remark": "用户登录id"},
            {"field_name": "v_id", "field_type": "int", "remark": "版本id"},
            {"field_name": "nickname", "field_type": "str", "remark": "用户昵称"},
            {"field_name": "pass_word", "field_type": "str", "remark": "密码"},
            {"field_name": "brand_name", "field_type": "str", "remark": "品牌名称"},
            {"field_name": "mobile", "field_type": "str", "remark": "手机号码"},
            {"field_name": "role", "field_type": "str", "remark": "用户角色"},
            {"field_name": "department_id", "field_type": "int", "remark": "部门id"},
            {"field_name": "department_name", "field_type": "str", "remark": "部门名称"},
            {"field_name": "state", "field_type": "int", "remark": "账号状态"},
            {"field_name": "create_time", "field_type": "timestamp", "remark": "创建时间"},
            {"field_name": "update_time", "field_type": "timestamp", "remark": "更新时间"}
        ]


    # 获取数据表的列名称
    def re_colum_list(self):
        r_list = []
        for i in self.DataColumn:
            f_name = i.get('field_name')
            r_list.append(f_name)
        return r_list


    # 添加[数据列表]字段名称
    def re_data_list_name(self,data_list):
        if data_list != 'None':    # 不为空
            colum_name_list = self.re_colum_list()
            res_list = []
            for i in data_list:
                list_one = list(i)
                res_one = dict(list(zip(colum_name_list, list_one)))
                res_one['create_time'] = str(res_one.get('create_time'))
                res_one['update_time'] = str(res_one.get('update_time'))
                res_list.append(res_one)
            return res_list
        else:                           # 为空
            return 'None'


    # 添加[数据详情]字段名称
    def re_detaile_data_name(self, detaile_data):
        if detaile_data != 'None':  # 不为空
            colum_name_list = self.re_colum_list()
            res_one = dict(list(zip(colum_name_list, detaile_data)))
            res_one['create_time'] = str(res_one.get('create_time'))
            res_one['update_time'] = str(res_one.get('update_time'))
            return res_one
        else:  # 为空
            return 'None'


# 用户登录验证---路由资源
class Login(Resource):

    def post(self):

        u_data = request.get_json()

        user_name = u_data.get('username')  # 前台提交的用户

        pass_word = u_data.get('password')  # 前台提交的密码

        user_obj = user_loader(user_name)  # 数据库查询获取的用户信息

        if user_obj == 'None':  # 用户不存在

            return 'None'

        # 密码 用户名称 正确 登录成功
        elif user_obj.password == pass_word and user_obj.id == user_name:

            login_user(user_obj)      # 加载用户信息到全局

            session.permanent = True  # 记住用户

            return 'true'

        else:  # 密码 用户名不正确 登录失败

            return 'false'


# 用户登出验证---路由资源
class LoginOut(Resource):
    @login_required
    def get(self):
        logout_user()
        # return render_template('/view/login.html')
        return 'login out True'


# 未登录授权的提示页面
@login_manager.unauthorized_handler
def unauthorized():
    return 'NOT Login power'


if __name__ == '__main__':
    loadinguser = LoadingUser('xiaohaha')
    loadinguser.get_admin_data()