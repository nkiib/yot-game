import process as pro

player1 = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
game_turn = 1 # ゲームターン
while game_turn <= 12:
    dicex = [0,0,0,0,0]
    pro.dice_th(dicex)
    turn = 0
    while turn <= 1:
        print('＜＜A:' + str(dicex[0]) + ' B:' + str(dicex[1]) + ' C:' + str(dicex[2]) + ' D:' + str(dicex[3]) + ' E:' + str(dicex[4])+ '＞＞')
        print('振り直したい値をアルファベットで入力してください ex. A B D')
        print('この出目で決定する場合"F"を入力指定ください')
        choice = input().split(" ")
        if 'F' in choice : break
        dicex = pro.rechoice(choice,dicex)
        turn += 1

    while True:
        print(dicex)
        poss_point = pro.result(dicex)

        print("ヨット(a)          " + str(poss_point[7]))
        print("フルハウス(b)       " + str(poss_point[8]))
        print("フォーナンバーズ(c)  " + str(poss_point[9]))
        print("ビッグストレート(d)  " + str(poss_point[10]))
        print("スモールストレート(e)" + str(poss_point[11]))
        print("チョイス(f)        " + str(poss_point[0]))
        print("エース(g)          " + str(poss_point[1]))
        print("デュース(h)        " + str(poss_point[2]))
        print("スリー(i)          " + str(poss_point[3]))
        print("フォー(j)          " + str(poss_point[4]))
        print("ファイブ(k)        " + str(poss_point[5]))
        print("シックス(l)        " + str(poss_point[6]))

        yaku = input("この回で自分の得点とする役を括弧内のアルファベット小文字で入力してください")

        if yaku == 'a' : point = poss_point[7] ; y = 7 
        if yaku == 'b' : point = poss_point[8] ; y = 8
        if yaku == 'c' : point = poss_point[9] ; y = 9
        if yaku == 'd' : point = poss_point[10] ; y = 10
        if yaku == 'e' : point = poss_point[11] ; y = 11
        if yaku == 'f' : point = poss_point[0] ; y = 0
        if yaku == 'g' : point = poss_point[1] ; y = 1
        if yaku == 'h' : point = poss_point[2] ; y = 2
        if yaku == 'i' : point = poss_point[3] ; y = 3
        if yaku == 'j' : point = poss_point[4] ; y = 4
        if yaku == 'k' : point = poss_point[5] ; y = 5
        if yaku == 'l' : point = poss_point[6] ; y = 6

        if player1[y] != -1:
            print('その役はすでに選ばれています。他の役を選んでください')
            continue
        else : break

    player1[y] = point

    print("この回でのあなたの得点は" + str(point) + "点でした")

    player1sum = sum(player1) + player1.count(-1)

    print("ヨット          " + str(player1[7]))
    print("フルハウス       " + str(player1[8]))
    print("フォーナンバーズ  " + str(player1[9]))
    print("ビッグストレート  " + str(player1[10]))
    print("スモールストレート" + str(player1[11]))
    print("チョイス        " + str(player1[0]))
    print("エース          " + str(player1[1]))
    print("デュース        " + str(player1[2]))
    print("スリー          " + str(player1[3]))
    print("フォー          " + str(player1[4]))
    print("ファイブ        " + str(player1[5]))
    print("シックス        " + str(player1[6]))
    print("現在の合計       " + str(player1sum) + "\n") 

    if player1.count(-1) == 0:
        break
    game_turn += 1

out_point = sum(player1)
if player1[1] + player1[2] + player1[3] + player1[4] + player1[5] + player1[6] >= 63:
    out_point += 35
print('あなたの最終的な点数は' + str(sum(player1)) + ' でした。' + "\n")
