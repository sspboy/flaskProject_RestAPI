from flask_restful import Resource                      # 接口处理方法
from API_.DB.DB_model import Basic_Operations           # 数据查询方法
from API_.resources.admin.Model_Menu import menu_list   # 菜单数据转义方法
from flask import request,session
from flask_login import UserMixin,LoginManager,login_user,logout_user,login_required


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
    def judgment_user(self):

        account_type = self.get_user_obj().get('account_type')

        if account_type == '2':     # 【管理员】account_type = '2'
            pass
        elif account_type == '0':   # 【主账号】account_type = '0'
            pass
        elif account_type == '0':   # 【子账号】account_type = '1'
            pass

    # 管理员信息
    def hold_super_admin(self):
        sql = ''
        pass

    # 主账号信息
    def hold_admin(self):
        pass

    # 子账号信息
    def hold_member(self):
        pass

    def get_user_obj(self):     # 根据 username 查询用户详情信息
        user = Basic_Operations('user')
        res = user.detaile(self.username)
        detaile_data = _list().re_detaile_data_name(res)
        return detaile_data

    # 【版本信息】# 根据版本号查询菜单信息
    def get_version(self):
    # 通过id差版本信息
    # select * from version where id=(select v_id from user where id='xiaohaha')
        pass

    # 【全部菜单信息】
    def get_menu(self):
        menu = Basic_Operations('menu')
        res = menu.show(1, 100, None)
        res_data = res.get('data')
        menu_data_list = menu_list().re_data_list_name(res_data)
        return menu_data_list

    # 获取所有一级菜单
    def get_first_menu(self):
        menu_data_list = self.get_menu()
        # 过滤菜单
        first_list = []
        for i in menu_data_list:
            if i.get('parent_id') == '0':
                first_list.append(i)
        return first_list

    # 获取后台管理员菜单
    def get_super_admin_menu(self):
        first_list = self.get_first_menu()  # 一级菜单
        menu_data_list = self.get_menu()    # 所有菜单
        for i in first_list:
            id = i.get('id')
            c_list = []
            for y in menu_data_list:
                if y.get('parent_id') == str(id):
                    c_list.append(y)
            i['child'] = c_list
        for x in first_list:
            print(x)

    # 获取主账号菜单：：无管理后台
    def get_admin_menu(self):
        pass

    # 获取子账号菜单：：过滤权限配置中不存在的菜单和功能
    def get_member_menu(self):
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
    loadinguser.get_super_admin_menu()