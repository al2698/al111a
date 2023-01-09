# [WAKUWAKU 尋找興奮源 (⌓‿⌓)](https://zerojudge.tw/ShowProblem?problemid=i793)

## 內容

安妮亞是一位小學一年級學生(但實際上她只有 4 歲)
她每天最喜歡做的事，就是尋找能讓她興奮(WAKUWAKU)的來源。

伊甸學園坐落於一個 R 列、 C 行的矩形，
左上角座標 (0, 0)，右下角座標 (R-1, C-1)

對於每格的狀態，我們可以用數字來表示：
0 表示該處可以通行
1 表示該處有障礙物
2 表示該處有能夠讓安妮亞興奮(WAKUWAKU)的東西

已知安妮亞一開始在第 a 列、第 b 行，也就是位置 (a, b)
每步只能向周圍(上、下、左、右)四個方向走一格。

其中能夠讓安妮亞興奮(WAKUWAKU)的東西可能不只一個。
並可以假設伊甸學園外圍四邊皆以障礙物包覆，且初始位置 (a, b) 必定不會是障礙物。

舉例來說，假設 R = 8, C = 7
每格狀態為：

```
1 1 1 1 1 1 1
1 0 1 2 1 1 1
1 0 0 1 0 2 1
1 0 0 0 0 1 1
1 0 1 1 1 1 1
1 0 1 2 1 2 1
1 0 0 0 0 0 1
1 1 1 1 1 1 1
```

假設一開始位於 (1, 1) 也就是標示為綠字的地方，
則至少經過 7 步，也就是標示為紅字的路徑後，就能夠順利找到離她最近的興奮源。

請協助撰寫程式，計算安妮亞最少要走幾步，
才能夠找到任何會讓她興奮(WAKUWAKU)的東西?

WAKUWAKU 好興奮啊 (⌓‿⌓)

---

## 輸入說明

第一行有四個正整數 R, C, a, b，
代表總列數、總行數、起點列、起點行
3 ≤ R, C ≤ 1000
0 < a < R-1
0 < b < C-1

接著有 R 列，每列有 C 行，代表學園每格狀態
狀態標示如題目敘述

---

## 輸出說明

最少要走幾步，才能夠找到任一會讓人興奮(WAKUWAKU)的東西？如果不論怎麼走都找不到的話，則請印出"WAKUWAKU"！

---

## 範例輸入 #1

```
8 7 1 1
1 1 1 1 1 1 1
1 0 1 2 1 1 1
1 0 0 1 0 2 1
1 0 0 0 0 1 1
1 0 1 1 1 1 1
1 0 1 2 1 2 1
1 0 0 0 0 0 1
1 1 1 1 1 1 1
```

## 範例輸出 #1

```
7
```

---

## ChatGPT 建議

首先，你需要創建一個二維數組，用來存儲學園的狀態。然後你可以使用一個叫做DFS(深度優先搜索)的函數，用來遍歷每一個格子。在遍歷的時候，你可以使用一個變量來記錄你已經走過的步數，並判斷是否找到了能夠讓人激動的東西。如果找到了，則可以返回步數。如果沒有找到，則繼續遍歷下一個格子。

該代碼使用深度優先搜索的方法，從起點開始，一直搜到能夠讓人興奮的東西，或者搜不到為止。每次搜索時，會先把當前位置標記為 1，表示已經搜過了，然後再向周圍四個方向搜索。如果找到了興奮的東西，就返回當前步數；如果搜不到，就返回 -1。



## Code

```python
from collections import deque
import sys

sys.stdin = open("input3.txt", "r")
input = sys.stdin.readline

def bfs(r, c, a, b, state):
    queue = deque()
    visited = set()

    queue.append((a, b))
    visited.add((a, b))

    steps = 0

    while queue:
        size = len(queue)
        for _ in range(size):
            x, y = queue.popleft()
            if state[x][y] == 2:
                #print('位置：',(x,y))
                return steps
            for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < r and 0 <= new_y < c and (new_x, new_y) not in visited and state[new_x][new_y] != 1:
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
        steps += 1
    return "WAKUWAKU"

r, c, a, b = map(int, input().split())
state = [list(map(int, input().split())) for _ in range(r)]
'''for row in state:
    for elem in row:
        print(elem, end='  ')
    print()
print('---\nsteps：',bfs(r, c, a, b, state))'''
print(bfs(r, c, a, b, state))
```

![WAKUWAKU 尋找興奮源 解題結果](Picture/2_2.png)

---

[Code](https://github.com/ccccourse/alg111a/issues/6)
