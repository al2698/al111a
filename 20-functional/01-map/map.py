def _map(a, f):
    r = []
    for x in a:
        r.append(f(x))
    return r

def _filter(a, f):
    r = []
    for x in a:
        if f(x): r.append(x)
    return r

def _reduce(a, f, init):
    r = init
    for x in a:
        r = f(r, x)
    return r

print(_map([1,2,3,4,5], lambda x:x*x))
print(_filter([1,2,3,4,5], lambda x:x%2==1))
print(_reduce([1,2,3,4,5], lambda x,y:x+y, 0))
