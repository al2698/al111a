import json

class FiniteStateMachine:
    def __init__(self, start, finals, actionMap):
        self.actionMap = actionMap
        self.start = start
        self.finals = finals
    def accept(self, s):
        state = self.start
        i = 0
        while True:
            if i >= len(s): break
            state = self.actionMap.get(f'{state},{s[i]}')
            if state is None: return False
            i += 1
        return state in self.finals
    def __str__(self):
        return json.dumps({'start':self.start,'finals':self.finals,'actionMap':self.actionMap}, indent=2)

if __name__=="__main__":
    fsm = FiniteStateMachine('s0', ['s0'], {
        's0,a':'s0'
    })
    print(fsm)
    print('aaa:', fsm.accept('aaa'))
    print('aab:', fsm.accept('aab'))

    # 參考 https://zh.wikipedia.org/wiki/%E6%9C%89%E9%99%90%E7%8A%B6%E6%80%81%E6%9C%BA#/media/File:DFAexample.svg
    fsm = FiniteStateMachine('s1', ['s1'], {
        's1,0':'s2',
        's1,1':'s1',
        's2,0':'s1',
        's2,1':'s2'
    })
    print(fsm)
    print('010:', fsm.accept('010'))
    print('101:', fsm.accept('101'))
