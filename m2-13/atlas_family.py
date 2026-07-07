from functools import wraps
class CountCalls:
    """统计函数调用次数的装饰器"""
    
    def __init__(self, func):
        self.func = func
        self.count = 0
        wraps(func)(self)  # 让self看起来像func
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"第 {self.count} 次调用 {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def greet(name):
    return f"Hello {name}"

greet("A")
greet("B")
greet("C")