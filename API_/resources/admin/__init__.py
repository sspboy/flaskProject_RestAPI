def get_function_name(func):
    def wrapper(*args, **kwargs):
        # 路由名称名称
        ruter_name = func.__qualname__
        print(f"Function name: {func.__qualname__}")
        return func(*args, **kwargs)
    return wrapper