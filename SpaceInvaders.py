from Processing import *
from random import *

window(500,500)
background(255,180,0)
fill(255,255,0)
def Game():
    window(500,500)
    rect(10,20,10,10)
Enemies=[]
for i in range(7):
    fill(0,255,255)
    rect(i*50,20,10,10)
    Enemies.append(i*50)
Enemies=[0,50,100,150,200,250,300]
width=10
length=20
for j in range(17):
    background(255,190,100)
    for enemyX in Enemies:
        rect(enemyX+width,20+length,10,10)
        rect(enemyX+width,40+length,10,10)
        rect(enemyX+width,60+length,10,10)
    width+=10
    length+=20
    delay(800)
## for j in range(6):    
##     rect(enemyX+width,20+length,10,10)
##     rect(enemyX+width,60+length,10,10)
## width-=10
## length-=20
## delay(800)
##     for enemyX in Enemies:
##         rect(enemyX+width,60+length,10,10)
##     width+=10
##     length+=30
##     delay(800)    
##     j=0
##     for j in range(6):
##         background(255,100,100)
##     for enemyX in Enemies:
 #    rect(enemyX+width,20+length,10,10)
 #    width-=10
 ##    length-=20
 #    delay(800)            
print(Enemies)
## for i in Enemies:        
##     length=20
##     width=10 
##     for j in range(6):
##        background(255,100,100)
##        rect(width,length,10,10)
##        width+=10
##        length+=10
##        fill(255,255,0)
##        delay(800)
##     j=0
##     for j in range(6):
##        background(255,100,100)
##        rect(width,length,10,10)
##        width-=10
##        length-=10
##        fill(255,255,0)
##        delay(800)    
## def doKeyPressed():
##     print( key(), keyCode(""))
##     
## onKeyPressed += doKeyPressed
## 
## Game()