# 布林邏輯最小化

像卡諾圖那樣，給定真值表，輸出一個最小化的邏輯式。

## 測試題

請最小化下列真值表

cab|o
---|-
000|0
001|0
010|0
011|1
100|0
101|1
110|1
111|1

較好的答案是 o <= a.b + c.b + c.a

但其他答案也行，閘數愈少就愈好

## 解題方法

bmDelegate.py 已透過委託給 logicmin 解決問題。

你可以試著採用 Greedy/Improve/Reduction/... 等方法寫一版自己的解法。

## Quine-McCluskey Algorithm

想法: Improve 

1. 先列出所有的 f()=1
2. 想辦法合併其中兩式，得到更小的 and 組合
3. 反覆這樣做，直到沒辦法改進為止。

* [Quine-McCluskey算法](https://zh.wikipedia.org/wiki/%E5%A5%8E%E5%9B%A0%EF%BC%8D%E9%BA%A6%E5%85%8B%E6%8B%89%E6%96%AF%E5%9F%BA%E7%AE%97%E6%B3%95)

## 想法: Greedy 

從 0 變數, 1 變數, 2 變數, ....

1. 將尚未涵蓋的 f()=1 列出
2. 找一個新的最少變數卻可完全符合的 and(x y ...) 加入
3. 直到能完全涵蓋所有的 1 為止，否則回到第一條



