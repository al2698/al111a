import random
from gateLib import *
from collections import Counter

def mapMin(goal, gateLib):
    pass

def addLibPart(gate, part, gateLib):
    partExp = part.normalForm()
    g = gateLib.find(partExp)
    if g:
        gate.partMap[partExp]=g

# 一開始先亂選 node，然後才呼叫 randomTree 遞迴生長
def randomSubTrees(gate, n): # 隨機取得 n 個子樹 (可重複取得同一個數次)。
    nodes = gate.allNodes() # 取得 gate 的所有子節點
    trees = [] # 
    for i in range(n):
        chooseNode = random.choice(nodes)
        prob = random.random()
        trees.append(randomGrowTree(chooseNode, prob))
    return trees

def randomGrowTree(root, prob):
    if not isinstance(root, Gate): return node
    tree = Gate(root.name, [])
    for param in root.params:
        if isinstance(param, Gate):
            child = '_' if random.random() < prob else randomGrowTree(param, prob)
        else:
            child = '_'
        tree.params.append(child)
    return tree

if __name__ == '__main__':
    glib = GateLib(gateLib)
    # glib.dump()
    # print(glib.find('not(_)'))
    # print('Nand(a,b)=', Nand(a,b).normalForm())
    goal = \
    Nand(
        Not(
            Nand(
                Not(
                    Nand(
                        Nand(Nand(a,b),
                             Not(c)
                            ),
                        Not(d)
                        )
                    ),
                Nand(
                    Not(Nand(e,f)),
                    g)
                )
            )
        ,h)
    # print(goal.normalForm())
    trees = randomSubTrees(goal, 10000)
    exps = [tree.normalForm() for tree in trees]
    expMap = Counter(exps)
    print(expMap)
    print("=========== in Gate Lib =============")
    for exp in expMap:
        if glib.find(exp):
            print(exp)
