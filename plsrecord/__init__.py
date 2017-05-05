import index

def play(type=None, n=None):
    values = index.pop(type, n)
    for value in values:
        value['callback'](**value)

