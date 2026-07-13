"""
繰り返し文練習
"""
"""
for i in range(5):
    print(i)
"""
'''
while count < 5:
    print(count)
    count += 1
'''
'''
for item in ['勇者','魔法使い','戦士']:
    print(item)
'''
import random

#難易度選択
while True:
    game = str(input("難易度を入力してね！ (Easy or Hard): ").lower())
    if game == 'easy':
        answer = random.randint(1,10)
        print("1から10までの数字を当てみて")
        break
    elif game == 'hard':
        answer = random.randint(1,100)
        print("1から100までの数字を当てみて")
        break
    else:
        print("難易度を正しく入力してね！")


while True:
    try:
        guess = int(input("数字を入力: "))
    except ValueError:
        print("数字を正しく入力してね！")
        continue

    if guess == answer:
        print("正解！！")
        break
    elif guess > answer:
        print("もっと小さいよ！")
    else:
        print("もっと大きいよ！")
    


