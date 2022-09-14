# https://ccckmit.gitbooks.io/rlab/content/solveEquation.html

def f(x) : return x*x-4*x+1  

def g(x) : return x-f(x)/4  

def isolve(g, x) :
  print("x=", x) 
  for (var i=0  i<100000  i++) :
    if (Math.abs(x-g(x)) < 0.001)
      return x 
    x = g(x) 
    print("x=", x) 
  
  return x 


var x = isolve(g, 1)
print("x=", x, "f(x)=", f(x))