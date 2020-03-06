import time
# Decorator
def cal_time(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        print("Func %s takes %4f secs"%(func,end_time-start_time))
        return result
    return wrapper
