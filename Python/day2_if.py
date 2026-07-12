# コメントアウト
'''
複数行コメント
コードの説明とかを書くのに便利
'''
"""
これも複数行コメント
こちらもコードの説明とかを書くのに便利
"""
# 本日の学び　条件分岐（IF文）

age = 17

if age > 18:
    print("成人です")
elif age < 18:
    print("成人ではありません")
else:
    print("成人になりたてです")
    
import random

score = random.randint(0,100)
print(score)

if score == 100:
    print("満点")
elif score <= 99 and score > 50:
    print("合格点")
else:
    print("不合格")

hp = 100
damage = random.randint(1,100)

print(damage)
hp -= damage
if hp >= 50:
    print('まだまだ余裕')
elif hp < 50:
    print('回復させよう')
elif hp == 0:
    print('気絶しました')