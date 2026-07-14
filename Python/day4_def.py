#じゃんけんミニゲーム
import random

def get_player_choice():
    player = int(input("1:グー,2:チョキ,3:パー → "))
    return player

def get_cpu_choice():
    cpu = random.randint(1,3)
    return cpu

def judge(player,cpu):
    if player == cpu:
        print("あいこだよ！")
        result = False
        return result
    elif (player == 1 and cpu == 2) or\
         (player == 2 and cpu == 3) or\
         (player == 3 and cpu == 1):
        print("あなたの勝ち！")
        result = True
        return result
    else:
        print("あなたの負け")
        result = True
        return result

def play():
    print("じゃんけんゲームを始めるよ！")
    result = False
    while result == False:
        player = get_player_choice()
        cpu = get_cpu_choice()
        result = judge(player,cpu)
    print ("ゲーム終了！")

play()

# def hello(name):
#     print(f"こんにちは{name}!")

# hello("スン")

# import random

# def play():
#     answer = selectLevel()
#     count = game(answer)
#     print(f"{count}回でクリアしたよ！")

    
# def selectLevel():
#     while True:
#         mode = str(input("難易度を入力してね！ (Easy or Hard): ").lower())
#         if mode == 'easy':
#             answer = random.randint(1,10)
#             print("1から10までの数字を当てみて")
#             return answer
#         elif mode == 'hard':
#             answer = random.randint(1,100)
#             print("1から100までの数字を当てみて")
#             return answer
#         else:
#             print("難易度を正しく入力してね！")


        
    
# def game(answer):
#     count = 0
#     while True:
#         try:
#             guess = int(input("数字を入力: "))
#         except ValueError:
#             print("数字を正しく入力してね！")
#             continue

#         count += 1

#         if guess == answer:
#             print("正解！！")
#             return count
#         elif guess > answer:
#             print("もっと小さいよ！")
#         else:
#             print("もっと大きいよ！")

# play()

# #難易度選択
# while True:
#     game = str(input("難易度を入力してね！ (Easy or Hard): ").lower())
#     if game == 'easy':
#         answer = random.randint(1,10)
#         print("1から10までの数字を当てみて")
#         break
#     elif game == 'hard':
#         answer = random.randint(1,100)
#         print("1から100までの数字を当てみて")
#         break
#     else:
#         print("難易度を正しく入力してね！")

# #ゲーム画面
# while True:
#     try:
#         guess = int(input("数字を入力: "))
#     except ValueError:
#         print("数字を正しく入力してね！")
#         continue

#     if guess == answer:
#         print("正解！！")
#         break
#     elif guess > answer:
#         print("もっと小さいよ！")
#     else:
#         print("もっと大きいよ！")
