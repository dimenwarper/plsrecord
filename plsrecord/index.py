from collections import defaultdict
_db = defaultdict(list)

def store(key, value):
    _db

def fetch(key):
    return _db[key]

def append(key, value):
    _db[key].append(value)

def fetch_all():
    return _db.iteritems()

def clear():
    global _db
    _db = defaultdict(list)

def pop(type=None, n=None):
    all_values = []
    if type is None:
        for k, values in fetch_all():
            if n is None:
                all_values += values
            else:
                for i in range(n):
                    try:
                        all_values.append(values.pop())
                    except IndexError:
                        break
        if n is None:
            clear()
    else:
        if n is None:
            all_values = _db.pop(type)
            _db[type] = []
        for i in range(n):
            all_values.append( _db[type].pop())
    return all_values



