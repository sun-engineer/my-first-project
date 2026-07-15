'''
player = {"name": "Sun","level": 1,"hp": 100} 

player["hp"] -= 10
player["mp"] = 10

player = {"name": "Sun","level": 1,"hp": 100} 

player["hp"] -= 10
player["mp"] = 10

for key in player:
    print(key,":",player[key])
'''

#じゃんけんミニゲーム
import random

def get_player_choice():
    player = int(input("1:グー,2:チョキ,3:パー → "))
    return player

def get_cpu_choice():
    cpu = random.randint(1,3)
    return cpu

#じゃんけん結果判定
def judge(player,cpu,status,result_dict):
    if player == cpu:
        print("あいこだよ！")
        return False
    elif (player == 1 and cpu == 2) or\
         (player == 2 and cpu == 3) or\
         (player == 3 and cpu == 1):
        print("あなたの勝ち！")
        status.append("勝ち")
        result_dict["勝ち"] += 1
        return True
    else:
        print("あなたの負け")
        status.append("負け")
        result_dict["負け"] += 1
        return True

#続けるか判定
def doSelectContinue():
    select = int(input("1:もう一回する, 2:もうやめる"))
    if select == 1:
        return True
    else:
        return False

#じゃんけんゲーム処理
def play(status,result_dict):
    print("じゃんけんゲームを始めるよ！")
    is_finished = False
    while not is_finished:
        player = get_player_choice()
        cpu = get_cpu_choice()
        is_finished = judge(player,cpu,status,result_dict)
    print ("ゲーム終了！")

#終了時の戦績表示
def result_display(status,result_dict):
    print("========成績========")
    for key in result_dict:
        print(f"{key} : {result_dict[key]}回")
    print("=======対戦履歴======")
    for n in status:
        print (n)

#メイン処理
status = []
result_dict = {"勝ち":0,"負け":0}

select = True
while select == True:
    play(status,result_dict)
    select = doSelectContinue()
    
result_display(status,result_dict)
