import random

def dice_th(dice):
    i = 0
    while i < 5:
        dice[i] = random.randint(1,6)
        i += 1
    return dice

def second_th(recho , dice):
    i = 0
    while i < 5:
        
        if recho[i] == True:
            dice[i] = random.randint(1,6) 
            i += 1
        else:
            i += 1
    return dice

dicex = [0,0,0,0,0]
dice_th(dicex)
print(dicex )
recho = [True , True , False , False , True]
second_th(recho,dicex)
print(dicex)

recho = [True , True , False , True , True]
second_th(recho,dicex)
print(dicex)

