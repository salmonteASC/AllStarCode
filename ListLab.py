from random import *
def randomMovies():
    lst1 = ["The Adventure of ","The tales of ","The Odyssey of ","The life of ","The hunting of ","The stories of ","The trials of ","The return of ", ]
    lst2 = ["David","Sam","Shorlock Homes","Hulk","","Charlie","Joshua","Christina","Shinjini"]
    lst3 = [" the killer"," the Great"," the Amazing"," the Magnificient"," the Pharaoh"]
    lst4 = [] #empty list for random movie titles
    
    for i in range(len(lst1)):
       first = lst1[randrange(len(lst1))]
       second = lst2[randrange(len(lst2))]
       third = lst3[randrange(len(lst3))]
       lst4.append(first + second + third)
    print(lst4)
randomMovies()