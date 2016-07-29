from Processing import *
from random import *
window(500,500)
width=25
length=25
i=0
while i<25:
    Xp=width *i
    line(Xp,0,Xp,500)
    Yp=length*i
    line(0,Yp,500,Yp)
    i=i+1
board=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
board[randrange(4)][randrange(4)]==1
GAMEOVER=False    
while GAMEOVER==False:
    row=int(input("which row"))
    column=int(input("which column"))
    while row>20 or row<0:
        row=int(input("Type a number between 0 and 4"))
    while column>20 or column<0:
        column=int(input("Type a number between 0 and 4"))    
    if board[row][column]== 1:
        GAMEOVER=True
        input("VICTORY!!!!!!!")
    else:
        fill(124,97,101)
        rect(width*column,length*row,25,25)
                
## def draw():
##    for i in range(len(board[0])):
##      if(board[0][i]==1):
##         rect(i*10 + 50,50,10,10)
##      elif(board[0][i]==0):
##         ellipse(i*10 + 55,50,10,10) 
##           
##    for i in range(len(board[1])): 
##      if(board[1][i]==1):
##         rect(i*10 + 50,50,10,10)
##      elif(board[1][i]==0):
##         ellipse(i*10 + 55,50,10,10)
##            
##    for i in range(len(board[2])):
##      if(board[2][i]==1):
##         rect(i*10 + 50,50,10,10)
##      elif(board[2][i]==0):
##         ellipse(i*10 + 55,50,10,10)
##                 
## frameRate(100)
## onLoop += draw
## loop()              