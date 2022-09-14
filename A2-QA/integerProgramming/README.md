# Integer Programming

ipDelegate.py 程式來源

* [An MIP Problem with Python with Constraints Define with Arrays](https://www.kindsonthegenius.com/data-science/an-mip-problem-with-python-with-constraints-define-with-arrays/)

請完成 ipHillClimbing.py 與 ipBruteForce.py

提示：

爬山演算法從 0 開始爬，高度函數可以用

(7x1 + 8x2 + 2x3 + 9x4 + 6x5)-(違反限制式的懲罰)

貪婪法每次讓 7x1 + 8x2 + 2x3 + 9x4 + 6x5 增大最多即可。

```
根據 4x1 + 7x2 + 3x3 + 8x4 + 5x5	≤ 211 

   0<=x1<=211/4
   0<=x2<=211/7
   0<=x3<=211/3
   0<=x4<=211/8
   0<=x5<=211/5

所以簡化來看 0 <=> xi <= 70 範圍內一定會有解答。

暴力法可以只考慮這個範圍。
```

