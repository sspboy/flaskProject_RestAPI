# -*- coding: utf-8 -*-
import sys,os
from pip._internal import main as pip_main


class Run():


    # pip 批量安装方法
    @staticmethod
    def install_pip():
        os.system('d: &call /www/flaskProject_RestAPI/env/Scripts/activate &cd /www/D_manager &python install_.py requirements.txt')


    # 导出项目依赖库
    @staticmethod
    def export():
        os.system('d: &call /www/flaskProject_RestAPI/env/Scripts/activate &call pip freeze > requirements.txt')


    # 启动项目
    @staticmethod
    def run():
        os.system('d: &call /www/flaskProject_RestAPI/env/Scripts/activate &cd /www/flaskProject_RestAPI &python app.py')


argvs = sys.argv[1:]

task = Run()

for action in argvs:
    func = getattr(task, action)
    func()