from flask_restful import Resource                      # 接口处理方法
from API_.DB.DB_model import Basic_Operations           # 数据查询方法
from flask import request,session
import json
from flask_login import UserMixin


# 定义【输出格式】模型：详情
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


    # 添加数据列表字段名称
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

    # 数据详情添加字段名称
    def re_detaile_data_name(self, detaile_data):
        if detaile_data != 'None':  # 不为空
            colum_name_list = self.re_colum_list()
            res_one = dict(list(zip(colum_name_list, detaile_data)))
            res_one['create_time'] = str(res_one.get('create_time'))
            res_one['update_time'] = str(res_one.get('update_time'))
            return res_one
        else:  # 为空
            return 'None'


# 定义【user】模型
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password




# 数据库加载用户信息
class LoadingUser():

    def __init__(self, username):
        self.username = username

    def get_user_obj(self):
        user = Basic_Operations(_list().table_name)
        res = user.detaile(self.username)
        detaile_data = _list().re_detaile_data_name(res)
        return detaile_data

    # 加载后台管理员
    # 加载品牌主账号
    # 加载品牌子账号





# 【品牌用户】权限验证
def get_function_name(func):
    def wrapper(*args, **kwargs):
        print(f"Function name: {func.__qualname__}")
        return func(*args, **kwargs)
    return wrapper


