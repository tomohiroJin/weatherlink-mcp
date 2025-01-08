"""
このファイルでは、Observer パターンのシンプルなカスタム実装を
`property` デコレータとリストを使用して行います。

この方法は、小規模な監視メカニズムを実装したい場合に適しています。
"""


class Observable:
    """
    シンプルな監視対象クラス。
    プロパティの変更を監視できます。
    """

    def __init__(self):
        self._value = None
        self._observers = []

    @property
    def value(self):
        """
        現在の値を取得します。
        """
        return self._value

    @value.setter
    def value(self, new_value):
        """
        値を変更し、変更を監視者に通知します。
        """
        self._value = new_value
        self._notify_observers(new_value)

    def add_observer(self, observer):
        """
        監視者を登録します。
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        """
        監視者を登録解除します。
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def _notify_observers(self, value):
        """
        すべての監視者に通知を送ります。
        """
        for observer in self._observers:
            observer(value)


# **具体的な監視者関数の例**
def observer_a(value):
    print(f"Observer A notified with value: {value}")


def observer_b(value):
    print(f"Observer B notified with value: {value}")
