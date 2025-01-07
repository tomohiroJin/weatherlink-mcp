"""
このモジュールではPythonの関数について詳しく説明します。
関数はコードを再利用可能にし、ロジックを整理するために使用されます。
基本的な関数の定義、引数の種類（デフォルト引数、可変長引数、キーワード引数、
位置引数、キーワード専用引数、組み込み関数の拡張）、
および匿名関数（ラムダ関数）について説明します。
"""


# **基本的な関数の定義**
def greet(name):
    """
    指定された名前で挨拶を返します。
    Args:
        name (str): 挨拶する相手の名前。
    Returns:
        str: 挨拶メッセージ。
    """
    return f"Hello, {name}!"


# **デフォルト引数**
def power(base, exponent=2):
    """
    指定された数値のべき乗を計算します。
    Args:
        base (int or float): 基数。
        exponent (int, optional): 指数。デフォルトは2。
    Returns:
        int or float: 計算結果。
    """
    return base**exponent


# **位置引数とキーワード専用引数**
def divide(a, b, *, precision=2):
    """
    2つの数値を割り算し、指定された精度で結果を返します。
    Args:
        a (float): 分子。
        b (float): 分母。
        precision (int, optional): 結果の小数点以下桁数。デフォルトは2。
    Returns:
        float: 割り算結果。
    """
    return round(a / b, precision)


# **可変長引数**
def sum_all(*args):
    """
    任意の数の数値を合計します。
    Args:
        *args (int or float): 加算対象の数値。
    Returns:
        int or float: 合計値。
    """
    return sum(args)


# **キーワード引数**
def describe_person(name, **kwargs):
    """
    人物の名前とその他の情報を説明します。
    Args:
        name (str): 名前。
        **kwargs: その他の情報。
    Returns:
        str: 説明文。
    """
    description = f"Name: {name}"
    for key, value in kwargs.items():
        description += f", {key}: {value}"
    return description


# **匿名関数（ラムダ関数）**
multiply = lambda x, y: x * y  # noqa: E731 # 2つの数値を掛け算


# **関数の内部関数（ネスト関数）**
def make_multiplier(factor):
    """
    指定した因子で掛け算を行う関数を返します。
    Args:
        factor (int or float): 掛け算の因子。
    Returns:
        function: 掛け算を行う関数。
    """

    def multiplier(x):
        return x * factor

    return multiplier


# **再帰関数**
def factorial(n):
    """
    再帰的に階乗を計算します。
    Args:
        n (int): 階乗を計算する非負整数。
    Returns:
        int: 階乗の結果。
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)
