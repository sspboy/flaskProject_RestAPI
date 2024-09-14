from API_.DB.Data_con import Data
import datetime, json, math

# 注册验证用户名称是否存在
# 要检查的用户名
# username_to_check = 'desired_username'
#
# # 执行查询
# cursor.execute("""
#   SELECT EXISTS(
#     SELECT 1 FROM users WHERE username = %s
#   ) AS `user_exists`
# """, (username_to_check,))



# 数据表-组件+翻页+跳转指定页面
class Select_table():

    # 参数 数据表名称\查询条件where、排序条件order by desc asc、翻页数量、翻页条数、第几页
    config = {

        'table_name': '',

        'condition': [

        ],
        # where 多条件、排序 order by name asc desc、like %关键字% 模糊匹配
        # 模糊匹配 WHERE name LIKE ‘%孙%'；
        # 文本条件 where id='1231231'
        # 时间范围 where start_time > '2020-08-24 00:00:00' and end_time < '2020-08-24 00:00:00'
        # 排序条件 order by name asc desc

        'page_size': '',
        'page': ''}

    def __init__(self, table_name, page=1, page_size=10, condition=None):
        # 数据表名称
        self.table_name = table_name
        self.page = page
        self.page_size = page_size
        self.condition = condition

    # 转译条件语句
    def translation_condition(self):

        if self.condition != None:  # 条件不为空

            where_text = ''
            o_text = ''
            for i in self.condition:
                type = i.get('type')
                if type == 'where':  # 筛选 where语句
                    w_text = ''
                    condition = i.get('condition')
                    for w in condition:
                        w_text = w_text + ' and ' + w.get('column_name') + ' ' + w.get('operator') + ' ' + "'" + w.get(
                            'value') + "'"
                    where_text = 'where' + w_text[4:]

                if type == 'orderby':  # 排序 orderby

                    condition = i.get('condition')[0]

                    o_text = ' order by ' + condition.get('column_name') + ' ' + condition.get('value')

            condition_text = where_text + o_text

            return condition_text
        else:  # 条件为空
            return None


    def page_num(self):  # limit(page_num, page_size)
        page = self.page
        if page <= 1:
            page_num = 0
        elif page > 1:
            page_num = (page - 1) * self.page_size
        return page_num

    def get_total_page_num(self):  # 获取内容总页数-可见

        # 需要where 条件计算出内容总页数
        sql = "select count(*) from %s %s;" % (self.table_name, self.translation_condition())
        
        total = {}

        res = Data().select(sql)

        total['total_number'] = int(math.ceil(int(res[0][0])))

        total['total_page'] = int(math.ceil(int(res[0][0]) / (self.page_size + 0.0)))

        return total

    def select_content_list(self):  # 查询内容列表

        # 需要where条件+排序条件
        sql = "select * from %s %s limit %s,%s;" % (
        self.table_name, self.translation_condition(), self.page_num(), self.page_size)

        res = Data().select(sql)
        if len(res) != 0:
            res_list = []
            for i in res:
                list_one = list(i)
                res_list.append(list_one)
            return res_list
        else:
            return 'None'

    def get_page_list(self, total_page):  # 翻页列表11页

        if total_page != 0:
            total_list = []

            for i in range(1, total_page + 1):

                total_list.append(i)

            if self.page <= 6 or len(total_list) <= 11 :

                # 截取总列表前11位
                page_list = total_list[:11]

            elif self.page > 6 and self.page <= total_page - 6:

                # 截取 当前左侧5位
                page_list_left = total_list[self.page - 6:self.page]

                # 截取 当前右侧5位
                page_list_right = total_list[self.page:self.page + 5]

                # 拼接为一个list
                page_list = page_list_left + page_list_right

            elif self.page > 6 and self.page > total_page - 6:

                page_list = total_list[total_page - 11:]

            return page_list
        else:
            return 'None'

    def page_message(self):  # 翻页信息=当前页，上一页，下一页，页面列表

        page_message = dict()

        page_message['total_number'] = self.get_total_page_num().get('total_number') # 数据总条数

        page_message['now_page'] = self.page  # 当前页

        page_message['page_size'] = self.page_size  # 数量

        total_page = self.get_total_page_num().get('total_page')

        page_message['total_page'] = total_page  # 总页数

        page_message['page_list'] = self.get_page_list(total_page)  # 总页数

        previous_page = self.page - 1  # 上一页int(page_num) - 1

        if previous_page <= 0:

            previous_page = 1

        page_message['previous_page'] = previous_page  # 上一页

        next_page = self.page + 1  # 下一页int(page_num) + 1

        if next_page > total_page:

            next_page = total_page

        page_message['next_page'] = next_page  # 下一页

        page_message['data'] = self.select_content_list()  # 数据列表

        return page_message


# 数据表-增、删、改、查(id详情)
class Operate_table():

    def __init__(self, table_name):
        # 数据表名称
        self.table_name = table_name


    # 插入设置数据
    def Add(self, setting_data):
        db_name = ''
        db_value = ''
        for x, y in setting_data.items():
            if y != '':
                db_name = db_name + x + ','
                if type(y) == dict:     # json 字段处理dict转json字符串
                    db_value = db_value + "'" + json.dumps(y, ensure_ascii=False) + "'" + ','
                elif type(y) == int:    # 整数字段处理
                    db_value = db_value + str(y) + ','
                else:                   # 文本字段处理
                    db_value = db_value + "'" + str(y) + "'" + ','

        sql="insert into %s (%s) value (%s)" % (self.table_name, db_name[:-1],db_value[:-1])

        res = Data().inset(sql)

        return res

    # 查询设置数据
    def Detaile(self, set_id):

        sql = "select * from %s where id='%s'" % (self.table_name, set_id)

        res = Data().select(sql)

        # 结果不为空
        if len(res) != 0:

            return res[0]

        else:   # 结果为空

            return 'None'

    # 更新指定id的设置信息
    def Update(self, setting_data, set_id):

        db_text = ''
        print(setting_data)

        for x, y in setting_data.items():

            if y != '':

                if type(y) == dict:     # json 字段处理

                    db_text = db_text + x + '=' + "'" + json.dumps(y,ensure_ascii=False) + "'" + ','

                elif type(y) == int:    # 整数字段处理

                    db_text = db_text + x + '=' + str(y) + ','

                else:                   # 文本字段处理
                    db_text = db_text + x + '=' + "'" + y + "'" + ','

        sql = "UPDATE %s SET %s WHERE id='%s'" % (self.table_name, db_text[:-1], set_id)
        print(sql)
        res = Data().updata(sql)

        return res

    # 删除指定的设置信息
    def Delete(self,set_id):
        sql = "delete from %s where id='%s'" % (self.table_name, set_id)
        res = Data().delete(sql)
        return res

    # 批量删除
    def BatchDelete(self, id_list_obj):

        keys = list(id_list_obj.keys())[0] # 删除字段的名称

        values = id_list_obj.get(keys)

        db_text = ''

        for i in values:

            db_text = db_text + "%s=%s or " % (keys, i)

        sql = "delete from %s where %s" % (self.table_name, db_text[:-4])

        res = Data().delete(sql)

        return res


# 封装[表]的基础操作:将列表查询、增删改查合并到一个类里面
class Basic_Operations():
    def __init__(self, table_name):
        self.table_name = table_name


    # 获取列表数据
    def show(self, page, page_size, condition):

        s = Select_table(self.table_name, page, page_size, condition)  # 示例化查询用例

        res_obj = s.page_message()  # 获取结果json

        return res_obj

    # 添加数据
    def add(self, data_obj):

        o = Operate_table(self.table_name)

        res = o.Add(data_obj)

        return res

    # 更新数据
    def update(self, data_obj, id):

        o = Operate_table(self.table_name)

        res = o.Update(data_obj, id)

        return res

    # 删除数据
    def delete(self, id):
        o = Operate_table(self.table_name)

        res = o.Delete(id)

        return res

    # 查看属性详情
    def detaile(self, id):

        o = Operate_table(self.table_name)

        res = o.Detaile(id)

        return res

    # 数据表批量删除
    def batchdel( self, id_list):

        o = Operate_table(self.table_name)

        res = o.BatchDelete(id_list)

        return res


    # 数据表批量导入CVS
    # 数据表批量导出CVS


# 多表关联查询


if __name__ == '__main__':

    # table:列表、翻页、多条件查询：：：：条件配置说明

    # 条件类型：where

    # 条件类型：orderby

    # 条件类型：模糊搜索

    condition = [
        {
            'type': 'where',

            'condition': [
            #{'column_name': 'create_time', 'value': '2020-11-16 16:10:10', 'operator': '>'},
            #{'column_name': 'create_time', 'value': '2023-11-16 16:12:10', 'operator': '<'},
            {'column_name':'shop_id','value':'5580507','operator':'='}]},                                  # 查询条件语句

        # {'type':'where',
        # 'condition':[{'column_name':'shop_id','value':'%1312830%','operator':'like'}]}, # 模糊查询语句

        {
            'type': 'orderby', 'condition': [{'column_name': 'id', 'value': 'asc', }]}                       # 排序条件语句

    ]

    Select_table = Select_table('item_detaile_res', 3, 10, condition)  # 示例化查询用例

    res_msg = Select_table.page_message()  # 获取结果json

    for i in res_msg.get('data'):
        i['create_time'] = str(i.get('create_time'))
        i['updata_time'] = str(i.get('updata_time'))
        print(i)  # 打印json格式


    # 新增 json
    # Operate_table('shop_setting').Add(setting_data)


    # 删除 id
    # Operate_table('shop_setting').Delete(5)


    # 查询详情 id
    # res = Operate_table('shop_setting').Select_id(2)
    # print (res)


    # 更新 id 更新json
    # Operate_table('shop_setting').Update(setting_data,3)