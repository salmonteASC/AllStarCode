from Processing import *
from random import *
window(500,500)
background(192,190,50)
X=50 #randrange()
Y=50 #randrange()
ellipse(X,250,50,50)
move=randrange(15)
move1=randrange(15)
while True:
    while X < 500 and Y < 500:
        X=X+move
        Y=Y+move1 
        background(192,192,192,5)
        fill(192,182,0)
        ellipse(X,Y,50,50)
        delay(1)
        if X >= 450 or X <= 25:
         move=-move     
        if Y >= 450 or Y <= 25:
         move1=-move1 
         