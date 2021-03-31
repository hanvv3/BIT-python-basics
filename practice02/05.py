# 5.

def randsum(*args):
    res = 0
    try:
        for i in (list(args)):
            res += int(i)
    except:
        pass
    return res

