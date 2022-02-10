import process as pro

def disp_point(dicex):    
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

    return point , y


