# from bmDelegate import *
from bmImprove import *

table = [
#abco1A0CPf
"0000100000",
"0010100111",
"0100100011",
"0111100101",
"1000110010",
"1011110100",
"1101110000",
"1111110110"
]

'''
import sys
print('match=', match("101", "1--"))
print('match=', match("001", "1--"))
print('cover=', cover(["1--"], table, 5, 3))
sys.exit(1)
'''
# 測試 parity 有錯？
report = boolMinimize(3, 7, table, ["a", "b", "c", "o", "one", "A", "zero", "C", "parity", "f"])
print(report)



'''
import sys
print("start---------")
print(match("111", "-11"))
print(match("111", "-10"))
print(match("111", "011"))
print("cover=", cover(["-11", "1-1"], table, 3))
print("cover=", cover(["-11", "1-1", "11-"], table, 3))
sys.exit(1)
'''
