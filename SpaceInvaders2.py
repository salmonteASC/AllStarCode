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
    delay(1600) 
    
enemies = [[]]
numEnemies = 10
incr = (width()-100)/numEnemies
bullets = []


pX = width()/2
pY = height()-50
edge = width()-10
ballX = pX
ballY = pY
showBullet = False
i=0

def SpaceInvaders():
    fill(green)
    rectMode(CENTER)
    rect(width()/2,height()-50,75,50)

def doKeyPressed():
    #print (key())   
    movePlayer(key())

    
def movePlayer(d):
    global pX,pY,showBullet,i
    speed = 5 

    if(d=="space"):
        ellipse(pX,pY,10,10)
        bullets.append([])
        bullets[i].append(pX)
        bullets[i].append(pY)
        i+=1
        showBullet = True 

    if(d=="Right"):
        pX+=speed
        if(pX>=edge):
            speed=-speed
            pX = width()-pX
    if(d=="Left"):
        pX-=speed
        if(pX<=10):
            speed=-speed
            pX = width()-pX
    """
    if(d=="Up"):
        pY-=speed
        update()
        if(pY>=edge):
            speed=-speed
            pY = width()-pY
    if(d=="Down"):
        pY+=speed
        update()
        if(pY>=edge):
            speed=-speed
            pY = width()-pY
    """

    
def hit():
    global ballY,showBullet
    if(ballY<=100):
        showBullet = False
        
def update():
    global pX,pY,ballX,ballY,showBullet,bulles
    background(240)
    fill(green)
    rect(pX,pY,75,50)
    if(showBullet):
        fill(255,0,0)
        for b in bullets:
            b[1]-=5
            ellipse(b[0],b[1],10,10)
            #delay(1)        
        hit()

onKeyPressed += doKeyPressed
frameRate(50)
onLoop+=update
SpaceInvaders()
loop()
