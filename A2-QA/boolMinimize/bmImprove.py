import random

def boolMinimize(nin, nout, table, names):
    r = []
    for i in range(nout):
        ri = boolMin1(nin, table, i, names)
        r.append(ri)
    return '\n'.join(r)

def boolMin1(nin, table, i, names, maxTry=100000000, maxFail=10000):
    # print(f"==============name:{names[nin+i]}=============")
    # initialize satMap, satArray
    satMap = {}
    satArray = []
    for row in table:
        if row[nin+i]!='0':
            satArray.append(row[0:nin]) 
            satMap[row[0:nin]]=row[nin+i]
    xArray = satArray.copy()
    if len(satArray)==0:
        return names[nin+i]+'=0'
    # keep improving
    fail = 0
    for t in range(maxTry):
        if improve(satMap, satArray):
            fail = 0
        else:
            fail += 1
        if (fail > maxFail): break
    # cover set (greedy)
    # print('xArray=', xArray)
    # print('satArray before sort=', satArray)
    satArray.sort(reverse=True, key=lambda x:x.count('-'))
    rules = []
    for rule in satArray:
        rules.append(rule)
        if cover(rules, table, nin+i, nin):
            # print(f'cover({rules}, {i})')
            break
    # print('satArray=', satArray)
    # print('rules=', rules)
    exp = names[nin+i]+'='+toDnf(rules, names, nin)
    # print('exp=', exp)
    return exp

def toDnf(rules, names, n):
    terms = []
    for rule in rules:
        term = toTerm(rule[0:n], names)
        terms.append(term)
    return '+'.join(terms)

def toTerm(rule, names):
    term = ""
    for i in range(len(rule)):
        if rule[i]=='1':
            term += names[i]
        elif rule[i]=='0':
            term += names[i]+"'"
        else:
            pass
    return "1" if term=="" else term
    
def improve(satMap, satArray):
    s1 = random.choice(satArray)
    i = random.randrange(0, len(s1))
    if s1[i] == '-': return False # xx-x 選到 - 不用改進
    side2 = '0' if s1[i]=='1' else '1' # 把該位反過來
    s2 = f"{s1[0:i]}{side2}{s1[i+1:]}"
    if satMap.get(s2)=='1': # 若反過來後也已滿足，則開始嘗試將 xx-x 加入改進之 # s1 是 satArray 抽出來的，所以 satMap.get(s1) 必然為 '1' ，不用再檢查
        s = f"{s1[0:i]}-{s1[i+1:]}" # s1,s2 只有在第 i 位不同，有0有1，所以將該位合併為 -
        if satMap.get(s)==None: # 如果 xx-x 不在 satMap 中，就加入
            satMap[s] = '1' # 將 xx-x 加入 satMap 與 satArray 中
            satArray.append(s)
            return True # 改進成功
    return False

def cover(rules, table, i, n):
    for row in table:
        if row[i]=='0': continue # f(x)=0, 不須涵蓋。
        # f(x)=1, 至少要有一條規則滿足，就是涵蓋
        satisfy = False
        for rule in rules:
            if match(row[0:n], rule):
                satisfy = True
                break
        if not satisfy:
            return False
    return True

def match(x, rule):
    for i in range(len(x)):
        if rule[i]!='-' and x[i]!=rule[i]:
            return False
    return True
