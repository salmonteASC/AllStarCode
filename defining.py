from Myro import *
init("sim")
penDown()
def square():
 i=0
 while i<4:
   turnBy(90)
   forward(1,5)
   motors(left,right)
   i=i+1
square()