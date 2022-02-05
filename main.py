import random

def dice_th(dice): # 初回のダイス振り
    i = 0
    while i < 5:
        dice[i] = random.randint(1,6)
        i += 1
    return dice

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


dicex = [0,0,0,0,0]
dice_th(dicex)
turn = 0
while turn <= 1:
    print('A:' + str(dicex[0]) + ' B:' + str(dicex[1]) + ' C:' + str(dicex[2]) + ' D:' + str(dicex[3]) + ' E:' + str(dicex[4]))
    print('振り直したい値をアルファベットで入力してください ex. A B D')
    print('この出目で決定する場合"F"を入力指定ください')
    choice = input().split(" ")
    # if choice == 'F' : break
    dicex = rechoice(choice,dicex)
    turn += 1

print(dicex)

poss_point = result(dicex)

print("ヨット(a)" + str(poss_point[7]))
print("フルハウス(b)" + str(poss_point[8]))
print("フォーナンバーズ(c)" + str(poss_point[9]))
print("ビッグストレート(d)" + str(poss_point[10]))
print("スモールストレート(e)" + str(poss_point[11]))
print("チョイス(f)" + str(poss_point[0]))
print("エース(g)" + str(poss_point[1]))
print("デュース(h)" + str(poss_point[2]))
print("スリー(i)" + str(poss_point[3]))
print("フォー(j)" + str(poss_point[4]))
print("ファイブ(k)" + str(poss_point[5]))
print("シックス(l)" + str(poss_point[6]))


yaku = input("この回で自分の得点とする役を括弧内のアルファベット小文字で入力してください")

if yaku == 'a' : point = poss_point[7]
if yaku == 'b' : point = poss_point[8]
if yaku == 'c' : point = poss_point[9]
if yaku == 'd' : point = poss_point[10]
if yaku == 'e' : point = poss_point[11]
if yaku == 'f' : point = poss_point[0]
if yaku == 'g' : point = poss_point[1]
if yaku == 'h' : point = poss_point[2]
if yaku == 'i' : point = poss_point[3]
if yaku == 'j' : point = poss_point[4]
if yaku == 'k' : point = poss_point[5]
if yaku == 'l' : point = poss_point[6]

print("この回でのあなたの得点は" + str(point) + "点でした")
