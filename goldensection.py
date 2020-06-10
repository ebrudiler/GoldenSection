import matplotlib.pyplot as plt
import numpy as np

alpha = 0.618 

e = 0.1

def f(x):
  return  2 * x - ( ( x - 20)**4  / 500 )

def GoldenSection(a, b):
  x1 = a + (1 - alpha)*(b - a)
  f1 = f(x1)
  x2 = a + alpha * ( b - a )
  f2 = f(x2)
  i = 0
  iteration = []
  x = []
  while ((b - a ) > e ):
    i += 1
    iteration.append(i)
    print(i, a, b)
    if f1 < f2:
      a = x1
      x1 = x2
      f1 = f2
      x2 = a + alpha*(b - a)
      f2 = f(x2)
    else:
      b = x2
      x2 = x1
      f2 = f1
      x1 = a + (1 - alpha)*(b - a)
      f1 = f(x1)
    xOptimum =( a+b ) / 2
    x.append(xOptimum)
  return ( a+b ) / 2, iteration, x

GoldenSection(0, 40)

