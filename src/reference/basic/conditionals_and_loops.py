"""
このモジュールではPythonの条件分岐とループのさまざまな構文を網羅的に説明します。
条件分岐は`if-elif-else`や三項演算子、ループは`for`ループ、`while`ループ、`break`や`continue`を含む制御構文を取り上げます。
また、リスト内包表記やジェネレーター式も紹介します。
"""

# **条件分岐の例**
# if-elif-else文
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# 三項演算子
# 条件式を1行で書く簡略化構文
is_even = "偶数" if score % 2 == 0 else "奇数"

# **ループの例**
# forループ: リストを繰り返す
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num**2)

# whileループ: カウントアップ
count = 0
max_count = 3
counts = []
while count < max_count:
    counts.append(count)
    count += 1

# breakとcontinue: ループ制御
filtered_numbers = []
for num in range(10):
    if num == 5:
        break  # 5に達したらループ終了
    if num % 2 == 0:
        continue  # 偶数をスキップ
    filtered_numbers.append(num)

# リスト内包表記: 簡潔なループ
cubes = [num**3 for num in range(1, 6) if num % 2 != 0]  # 奇数の立方
