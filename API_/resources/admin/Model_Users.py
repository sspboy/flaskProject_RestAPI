from flask_restful import Resource                      # 接口处理方法
from API_.DB.DB_model import Basic_Operations           # 数据查询方法
from flask import request
from flask_login import login_required,current_user
from API_.resources.admin import get_admin_power      # 鉴权方法
import json


# 定义【输出】模型：详情
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


# 用户详情接口资源
class UserDetaile(Resource):

    # 查询详情
    @login_required
    @get_admin_power
    def get(self, u_id):
        user = Basic_Operations(_list().table_name)
        res = user.detaile(u_id)
        detaile_data = _list().re_detaile_data_name(res)
        return detaile_data


    # 删-详情
    @login_required
    @get_admin_power
    def delete(self, u_id):
        user = Basic_Operations(_list().table_name)
        res = user.delete(u_id)
        return res


    # 改（更新）-详情
    @login_required
    @get_admin_power
    def put(self, u_id):
        re_data = json.loads(request.get_data())
        setting_data = re_data.get('setting_data')
        user = Basic_Operations(_list().table_name)
        res = user.update(setting_data, u_id)
        return res


# 用户列表接口资源
class UserList(Resource):

    # 批量删除
    @login_required
    @get_admin_power
    def put(self):
        re_data = json.loads(request.get_data())
        user = Basic_Operations(_list().table_name)
        res = user.batchdel(re_data)
        return res


    # 列表查询::
    @login_required
    @get_admin_power
    def post(self):
        user_name = current_user.id
        account_type = current_user.account_type
        print(user_name)
        print(account_type)
        re_data = json.loads(request.get_data())

        page = re_data.get('page')

        page_size = re_data.get('page_size')

        condition = re_data.get('condition')

        user = Basic_Operations(_list().table_name)

        res = user.show(page, page_size, condition)

        # 转换datalist字段名称
        data_list = res.get('data')

        res['data'] = _list().re_data_list_name(data_list)

        return res


# 添加数据
class UserAdd(Resource):


    # 增
    @login_required
    @get_admin_power
    def post(self):
        re_data = json.loads(request.get_data())
        user = Basic_Operations(_list().table_name)
        res = user.add(re_data)
        return res
