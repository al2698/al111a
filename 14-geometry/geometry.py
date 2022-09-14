import numpy as np

# 叉積 a0*b1-a1*b0 (只適用於二維向量)
def cross(a,b):
  return a[0]*b[1]-a[1]*b[0]

# 檢測轉向：結果為正代表是順時針右轉 (負代表逆時針左轉)
def direction(p0, p1, p2):
  return cross(np.subtract(p2, p0), np.subtract(p1, p0))

# 檢測 pk 是否位於 pi, pj 所形成的矩形內部。
def inBox(pi, pj, pk):
    return (min(pi[0], pj[0]) <= pk[0] and pk[0] <= max(pi[0], pj[0]) and
            min(pi[1], pj[1]) <= pk[1] and pk[1] <= max(pi[1], pj[1]))

# 檢測 (p1, p2) 和 (p3, p4) 是否相交 
def intersect(p1, p2, p3, p4):
    d1 = direction(p3, p4, p1)
    d2 = direction(p3, p4, p2)
    d3 = direction(p1, p2, p3)
    d4 = direction(p1, p2, p4)
    if d1*d2 < 0 and d3*d4 < 0: return True
    if d1==0 and inBox(p3, p4, p1): return True
    if d2==0 and inBox(p3, p4, p2): return True
    if d3==0 and inBox(p1, p2, p3): return True
    if d4==0 and inBox(p1, p2, p4): return True
    return False

if __name__ == '__main__':
    print('cross([1,2], [2,1])=', cross([1,2], [2,1]))
    p0 = [0,0]; p1 = [1,1]; p2 = [2, 1]; p3 = [-1, 0]
    print('direction(p0, p1, p2)=', direction(p0, p1, p2))
    print('intersect(p0, p1, p2, p3)=', intersect(p0, p1, p2, p3))
