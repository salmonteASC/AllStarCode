from Myro import *
init("sim")
penDown()
i=0
while(i<8):
  forward(2,2)
  turnBy(90)
  i=i+1
  i=0
  while(i<4):
    forward(1,1)
    turnBy(90)
    i=i+1