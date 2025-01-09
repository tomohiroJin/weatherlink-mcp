"""
このスクリプトでは、Pythonで`pytest`などのテストフレームワークを使用せずに
手動でテストを実行する方法を説明します。

実行手順:
1. このスクリプトをPythonで直接実行してください。
2. 各テスト結果が端末に出力されます。
3. 出力メッセージを確認し、成功/失敗を判断してください。

"""


# **テスト対象のコード**
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


# **テスト関数**
def test_add():
    try:
        assert add(3, 2) == 5, "3 + 2 は 5 であるべき"
        print("test_add (足し算のテスト): 成功")
    except AssertionError as e:
        print(f"test_add (足し算のテスト): 失敗 - {e}")


def test_subtract():
    try:
        assert subtract(5, 3) == 2, "5 - 3 は 2 であるべき"
        print("test_subtract (引き算のテスト): 成功")
    except AssertionError as e:
        print(f"test_subtract (引き算のテスト): 失敗 - {e}")


def test_multiply():
    try:
        assert multiply(4, 3) == 12, "4 * 3 は 12 であるべき"
        print("test_multiply (掛け算のテスト): 成功")
    except AssertionError as e:
        print(f"test_multiply (掛け算のテスト): 失敗 - {e}")


def test_divide():
    try:
        assert divide(10, 2) == 5, "10 / 2 は 5 であるべき"
        print("test_divide (割り算のテスト): 成功")
    except AssertionError as e:
        print(f"test_divide (割り算のテスト): 失敗 - {e}")

    try:
        divide(10, 0)
        print(
            "test_divide (割り算のテスト): 失敗 - 0で割っても例外が発生しませんでした"
        )
    except ValueError:
        print("test_divide (割り算のテスト): 成功 - 0で割った際に例外が正しく発生")


# **テストの実行**
def run_tests():
    print("手動テストを実行中...")
    test_add()
    test_subtract()
    test_multiply()
    test_divide()


# **エントリーポイント**
if __name__ == "__main__":
    run_tests()
