- 幾乎都是複製老師的Code，但因為程式碼並不複雜因此稍花一點時間就能理解。除了做了些許修改以`tuple`顯示答案外邏輯都沒有改變。

## 系統式列舉

```python
def combination(A, m): # 從 A 陣列中取出 m 個的所有可能性
    chooses = []
    results = {}
    Cnk(A, len(A), m, chooses, m, results)
    return results

def Cnk(A, n, k, chooses, m, results): # 從 A[0..n] 中選取 k 個補進 chooses，如果滿 m 個就儲存在results
    if len(chooses)==m:
        result = tuple(chooses)
        if result in results:
            results[result] += 1
        else:
            results[result] = 1
        return
    if n <= 0: return
    Cnk(A,n-1,k,chooses,m,results) # C(n-1,k) // A[n-1] 沒取到

    chooses.append(A[n-1])
    Cnk(A,n-1,k-1,chooses,m,results) # C(n-1,k-1) // A[n-1] 有取到
    del chooses[-1]

print(combination([1,2,3,4,5], 3))
```

---

## 隨機式列舉

```python
import random as rd

def rdCombined(pA, k):
    A = pA.copy()
    chooses = []
    for _ in range(k):
        i = rd.randrange(0, len(A))
        chooses.append(A[i])
        del A[i] #選到哪個就刪除哪個，防止隨機選擇到同樣的
    chooses.sort() #由大排到小
    return chooses # 將函式結果傳出去

A = [1,2,3,4,5]
results = {}
for _ in range(55):
    result = tuple(rdCombined(A, 3))
    if result in results:
        results[result] += 1
    else:
        results[result] = 1

print(results)
```

---

[Code](https://github.com/al2698/al111a/blob/main/HW/2_Cnk.ipynb)
