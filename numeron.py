import sys
input = sys.stdin.readline
import random

#チュートリアル
def tutorial():
    print("\n\n\n\n<ルール説明>\n")
    print("CPUの決めた数字をcallして当てるゲームです\n")
    print("このゲームには数字を当てるヒントが用意されています")
    print("\"eat\"と\"byte\"という2つの言葉です")
    print("数字と桁があっている場合を表す\"eat\"\n数字のみ合っている場合を表す\"byte\"の二つです\n")
    print("例：cpu　1234　　call　1356\nこの場合1がeat、3がbyteなのでcpuから\"1eat 1byte\"とヒントが与えられます")
    print("ヒントをうまく使って少ない回数でcpuの数字を当ててください！")
    print("これでチュートリアルを終わります")

#ゲーム進行
print("\n\n\n<!!GAME START!!>\nヌメロンへようこそ!")
print("このゲームは初めてですか？")
while 1:
    print("初めてなら 1、そうでないなら 0を入力してください\n")
    check=int(input())
    print("\n")
    if check!=1 and check!=0:
        continue
    else:
        if check==0:
            print("チュートリアルを省略します")
            break
        else:
            tutorial()
            break
#ゲーム繰り返し
while 1:
    print("\n\nそれではゲームを始めます")
    #deciding number
    randamOrigin=["0","1","2","3","4","5","6","7","8","9"]
    selectNumbers=random.sample(randamOrigin,4)
    rivalNumber=""
    for i in range(4):
            rivalNumber+=selectNumbers[i]
    eat=0
    byte=0
    count=0
    while 1:
        while 1:
            print("4桁の重複しない数をcallしてください\n")
            callNumber=input()
            print("\n")
            #print("call=>",callNumber,"length=>",len(callNumber))
            if len(callNumber)!=5:
                print("callされた数が4桁ではありません")
                continue
            check=[callNumber[0],callNumber[1],callNumber[2],callNumber[3]]
            set(check)
            #print("check=>",check)
            if len(check)<4:
                print("callされた数が重複しています")
                continue
            break
        print("\n")
        for i in range(4):
            if callNumber[i]==rivalNumber[i]:
                eat+=1
            elif callNumber[i] in selectNumbers:
                byte+=1
            else:
                pass
        count+=1
        print("\ncallされた数は"+str(eat)+"eat "+str(byte)+"byteです")
        if eat==4:
            print("あなたは"+str(count)+"回目で当てました\nこれでゲームを終わります")
            break
        else:
            eat=0
            byte=0
            print("現在のcall回数:"+str(count)+"回\n次のcallに移ります")
    while 1:
        print("ゲームを続けるのであれば 1、やめるのであれば 0を入力してください\n")
        judge=int(input())
        print("\n")
        if judge!=0 and judge!=1:
            continue
        else:
            break
    if judge==1:
        pass
    else:
        print("ゲームを終了します。お疲れさまでした。")
        break
