def benchmark(func):
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print("\t"+func.__name__, time.clock()-t)
        return res
    return wrapper