"""
Decorator パターンは、オブジェクトの機能を動的に拡張するためのデザインパターンです。
Python の組み込みデコレータ機能を活用して、関数やクラスに柔軟に機能を追加できます。

このファイルでは、Decorator パターンを Python で実装し、テストコードを含めています。
"""


# **基本的なデコレータ関数**
def uppercase_decorator(func):
    """
    文字列を大文字に変換するデコレータ。
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


# **複数のデコレータを組み合わせた例**
def exclamation_decorator(func):
    """
    文字列の末尾に感嘆符を追加するデコレータ。
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"{result}!"

    return wrapper


# **デコレータを適用した関数**
@uppercase_decorator
@exclamation_decorator
def greet(name: str) -> str:
    """
    挨拶メッセージを生成します。
    """
    return f"Hello, {name}"


# **デコレータをクラスに適用した例**
class BaseNotifier:
    """
    基本的な通知クラス。
    """

    def send(self, message: str) -> str:
        return message


class DecoratedNotifier:
    """
    デコレータを使用して通知機能を拡張したクラス。
    """

    def __init__(self, notifier: BaseNotifier):
        self._notifier = notifier

    def send(self, message: str) -> str:
        decorated_message = f"[IMPORTANT] {message}"
        return self._notifier.send(decorated_message)
