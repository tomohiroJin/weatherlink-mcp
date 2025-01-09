"""
このモジュールではPythonの例外処理について詳しく説明します。
例外処理はプログラムの実行時に発生するエラーを管理し、安全にプログラムを終了させたり
特定のエラーを補正したりするために使用されます。
"""


# **基本的な例外処理**
def divide(a, b):
    """
    2つの数値を割り算します。
    Args:
        a (float): 分子。
        b (float): 分母。
    Returns:
        float: 割り算結果。
    Raises:
        ValueError: 分母が0の場合に発生します。
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


# **例外の種類**
def parse_int(value):
    """
    文字列を整数に変換します。
    Args:
        value (str): 数値を表す文字列。
    Returns:
        int: 整数値。
    Raises:
        ValueError: valueが整数に変換できない場合に発生します。
    """
    return int(value)


# **カスタム例外**
class CustomError(Exception):
    """
    カスタム例外クラス。
    Attributes:
        message (str): エラーメッセージ。
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# **例外処理の使用例**
def process_data(data):
    """
    データを処理します。
    Args:
        data (any): 処理するデータ。
    Returns:
        str: 処理結果。
    """
    try:
        if not isinstance(data, str):
            raise CustomError("Data must be a string.")
        return data.upper()
    except CustomError as e:
        return f"Error: {e.message}"
