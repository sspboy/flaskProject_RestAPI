from flask import Flask
from API_.resources.admin.BluePrintAdmin import admin_blueprint

app = Flask(__name__)

# 登录

app.register_blueprint(admin_blueprint, url_prefix='/admin')#管理后台


if __name__ == '__main__':

    app.run(debug=True)