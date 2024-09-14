from flask_login import current_user
# 验证管理员权限
def get_admin_power(func):
    def wrapper(*args, **kwargs):
        print(current_user.id)
        print(current_user.account_type)
        account_type = current_user.account_type
        if account_type != "2":
            # 路由名称名称
            return 'Not admin power'
        # ruter_name = func.__qualname__
        # print(f"Function name: {func.__qualname__}")
        return func(*args, **kwargs)
    return wrapper