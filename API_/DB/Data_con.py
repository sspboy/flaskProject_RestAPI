# -*- coding: utf-8 -*-
import pymysql


# 链接数据库方法
class Data():

    def __init__(self):
        # 阿里云数据库
        self.config = {'host': 'rm-bp10793gy177qcs4loo.mysql.rds.aliyuncs.com',
                       'port': 3306,
                       'user': 'sspboy',
                       'passwd': 'Shaoshipeng123', 'db': 'master', 'charset': 'utf8'}


    # 查询方法
    def select(self, sql):
        db = pymysql.connect(**self.config)
        cursor = db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        db.close()
        return result

    # 查询方法
    def select_one(self, sql):
        db = pymysql.connect(**self.config)
        cursor = db.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        db.close()
        return result

    # 更新方法
    def updata(self, sql):
        db = pymysql.connect(**self.config)
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return 'True'
        except IOError:
            db.rollback()
            cursor.close()
            db.close()
            return 'False'


    # 插入上传数据方法
    def inset(self, sql):
        db = pymysql.connect(**self.config)
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            inset_id = db.insert_id()   # 插入数据返回自增id
            db.commit()
            cursor.close()
            db.close()
            return inset_id
        except IOError:
            db.rollback()
            cursor.close()
            db.close()
            return 'False'

    # 删除方法
    def delete(self, sql):
        db = pymysql.connect(**self.config)
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return 'True'
        except IOError:
            db.rollback()
            cursor.close()
            db.close()
            return 'False'


