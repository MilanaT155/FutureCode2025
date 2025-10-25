from time import *
from random import randint
from turtle import *
bgcolor('yellow')
color('green')
width(3)
start = time()
l = 100
a = 120
for i in range(3):
    forward(l)
    right(a)

finish = time()
print(finish - start)
exitonclick()