from flask_restful import Resource                      # 接口处理方法
from API_.DB.DB_model import Basic_Operations           # 数据查询方法
from flask import request
import json
from flask_login import login_required,current_user

# 定义【输出】模型：详情
class version_list:

    def __init__(self):      # 列表数据
        self.table_name = 'version'
        # 数据表头名称、数据类型、描述说明
        self.DataColumn =[
            {
                'key':'1',
                "field_name": "id",    # 字段名称
                "field_type": "int",   # 字段类型
                "title": "id",  # 备注描述
                "dataIndex": "id",

            },
            {'key':'2',"field_name": "version_number", "field_type": "float", "title": "版本号","dataIndex": "version_number",},
            {'key':'3',"field_name": "version_name", "field_type": "str", "title": "版本名称","dataIndex": "version_name",},
            {'key':'4',"field_name": "menu_setting", "field_type": "json", "title": "菜单以及权限","dataIndex": "menu_setting",},
            {'key':'5',"field_name": "price", "field_type": "int", "title": "价格","dataIndex": "price",},
            {'key':'6',"field_name": "sub_account_number", "field_type": "int", "title": "账号数量","dataIndex": "sub_account_number",},
            {'key':'7',"field_name": "duration", "field_type": "int", "title": "使用时长月为单位","dataIndex": "duration",},
            {'key':'8',"field_name": "create_time", "field_type": "timestamp", "title": "创建时间","dataIndex": "create_time",},
            {'key':'9',"field_name": "update_time", "field_type": "timestamp", "title": "更新时间","dataIndex": "update_time",}
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
class VersionDetaile(Resource):

    # 查询详情
    @login_required
    def get(self, u_id):
        user = Basic_Operations(version_list().table_name)
        res = user.detaile(u_id)
        detaile_data = version_list().re_detaile_data_name(res)
        return detaile_data


    # 删-详情
    def delete(self, u_id):
        user = Basic_Operations(version_list().table_name)
        res = user.delete(u_id)
        return res


    # 改（更新）-详情
    def put(self, u_id):
        re_data = json.loads(request.get_data())
        setting_data = re_data.get('setting_data')
        user = Basic_Operations(version_list().table_name)
        res = user.update(setting_data, u_id)
        return res


# 用户列表接口资源
class VersionList(Resource):


    # 批量删除
    def put(self):
        re_data = json.loads(request.get_data())
        user = Basic_Operations(version_list().table_name)
        res = user.batchdel(re_data)
        return res


    # 列表查询::
    def post(self):

        re_data = json.loads(request.get_data())

        page = re_data.get('page')

        page_size = re_data.get('page_size')

        condition = re_data.get('condition')

        user = Basic_Operations(version_list().table_name)

        res = user.show(page, page_size, condition)

        # 转换datalist字段名称
        data_list = res.get('data')

        res['data'] = version_list().re_data_list_name(data_list)

        # 用户信息
        res['user'] = current_user.user_obj

        # 表头信息
        res['colum'] = version_list().DataColumn

        return res


# 添加数据
class VersionAdd(Resource):

    # 增
    def post(self):
        re_data = json.loads(request.get_data())
        user = Basic_Operations(version_list().table_name)
        res = user.add(re_data)
        return res
