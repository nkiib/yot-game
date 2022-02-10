import random

def result(dicex):
    # 各要素の出現回数を数える
    res = [0,0,0,0,0,0]
    i = 0
    while i < 6:
        res[i] = dicex.count(i+1)
        i += 1

    res_point = [0,0,0,0,0,0,0,0,0,0,0,0]

    # いつでも選択できるものの判定
    # チョイス以外は出現回数と出目を乗算する。チョイスはすべての要素の合計値とする。
    res_point[0] = sum(dicex) # チョイス
    res_point[1] = res[0] * 1 # エース
    res_point[2] = res[1] * 2 # デュース
    res_point[3] = res[2] * 3 # スリー
    res_point[4] = res[3] * 4 # フォー
    res_point[5] = res[4] * 5 # ファイブ
    res_point[6] = res[5] * 6 # シックス
    
    # ヨット判定：すべての出目が同じ数 ex.1,1,1,1,1
    # 点数は固定50点
    if res.count(5) == 1 and res.count(0) == 4: # 出現回数が5回のものを判定する。念の為、他がすべて0であることも確認する。
        res_point[7] = 50

    # フルハウス判定：同じ出目が3つと2つで出来ている ex.1,1,2,2,2
    # 点数は出目の合計
    if res.count(2) == 1 and res.count(3) == 1: # 出現回数が2回と3回のものの両方が存在することを判定する。
        res_point[8] = sum(dicex)
    
    # フォーナンバーズの判定 ex.1,1,1,1,2 or 1,1,1,1,1
    # 点数は出目の合計
    if res.count(4) == 1 or res.count(5) == 1 : # 出現回数が4以上のものを判定する
        res_point[9] = sum(dicex)

    # ビッグストレートの判定：5つの出目がすべて連続している ex.1,2,3,4,5
    # 点数は固定30点
    if res.count(1) == 5:
        if dicex.count(1) == 0 or dicex.count(6) == 0: # 出現回数が1回のものが5つあり、出目1と出目6のどちらかが0であることを確認する
            res_point[10] = 30
    
    # スモールストレートの判定：4つの出目が連続している 1,2,3,4,2
    # 点数は固定15点
    if dicex.count(3) >= 1 and dicex.count(4) >= 1:
        if dicex.count(5) >= 1:
            if dicex.count(6) >= 1 or dicex.count(2) >= 1:
                res_point[11] = 15 # 2,3,4,5と3,4,5,6の判定
        elif dicex.count(2) >= 1 and dicex.count(1) >= 1:
            res_point[11] # 1,2,3,4の判定

    return res_point    

def rechoice(choice,dicex): # 2/3回目のダイス振り

    recho = [False , False , False , False , False]
    if 'A' in choice: recho[0] = True
    if 'B' in choice: recho[1] = True
    if 'C' in choice: recho[2] = True
    if 'D' in choice: recho[3] = True
    if 'E' in choice: recho[4] = True

    i = 0
    while i < 5:
        if recho[i] == True:
            dicex[i] = random.randint(1,6) 
            i += 1
        else: i += 1
    return dicex

def dice_th(dice): # 初回のダイス振り
    i = 0
    while i < 5:
        dice[i] = random.randint(1,6)
        i += 1
    return dice