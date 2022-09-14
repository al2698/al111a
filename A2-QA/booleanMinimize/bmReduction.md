## 測試題

請最小化下列算式

f(a,b,c,d)=ab+cd+acd+abc

答案應該是 f(a,b,c,d)=ab+cd

## 方法: reduce 為 integer programming

minimize:


constraint:
a+b >= 2
c+d >= 2
a+c+d >= 3
a+b+c >= 3

