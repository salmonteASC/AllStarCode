from Processing import *
window(500,500)
Enemies=[6,9,12,15,18,21,24]
for i in Enemies:
    x=19*i
    rect(x-50,10,40,40)
    x+=40
    