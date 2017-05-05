import index

def record(type='data', callback=lambda x:x):
    def decor(function):
        def wrapper(*args, **kwargs):
            storable, res = function(*args, **kwargs)
            storable['callback'] = callback
            index.append(type, storable)
            return res
        return wrapper
    return decor
