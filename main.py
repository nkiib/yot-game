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

def result(dicex):
    # 各要素の出現回数を数える
    res = [0,0,0,0,0,0]
    i = 0
    while i < 6:
        res[i] = dicex.count(i+1)

    # いつでも選択できるものの判定
    # チョイス以外は出現回数と出目を乗算する。チョイスはすべての要素の合計値とする。
    ace     = res[0] * 1
    duce    = res[1] * 2
    three   = res[2] * 3
    four    = res[3] * 4
    five    = res[4] * 5
    six     = res[5] * 6
    choice  = sum(dicex)

    # ヨット判定：すべての出目が同じ数 ex.1,1,1,1,1
    # 点数は固定50点
    if res.count(5) == 1 and res.count(0) == 4: # 出現回数が5回のものを判定する。念の為、他がすべて0であることも確認する。
        yot = 50

    # フルハウス判定：同じ出目が3つと2つで出来ている ex.1,1,2,2,2
    # 点数は出目の合計
    if res.count(2) == 1 and res.count(3) == 1: # 出現回数が2回と3回のものの両方が存在することを判定する。
        full_house = sum(dicex)
    
    # フォーナンバーズの判定 ex.1,1,1,1,2 or 1,1,1,1,1
    # 点数は出目の合計
    if res.count(4) == 1 or res.count(5) == 5 : # 出現回数が4以上のものを判定する
        four_num = sum(dicex)

    # ビッグストレートの判定：5つの出目がすべて連続している ex.1,2,3,4,5
    # 点数は固定30点
    if res.count(1) == 5:
        if dicex.count(1) == 0 or dicex.count(6) == 0: # 出現回数が1回のものが5つあり、出目1と出目6のどちらかが0であることを確認する
            big_st = 30
    
    # スモールストレートの判定：4つの出目が連続している 1,2,3,4,2
    # 点数は固定15点
    
