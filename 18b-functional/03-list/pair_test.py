from pair import *

x = pair(1, 2)
print('head(x)=', head(x))
print('tail(x)=', tail(x))
    
y = pair(3, 4)
z = pair(x, y)

print('head(head(z))=', head(head(z)))
print('head(tail(z))=', head(tail(z)))
