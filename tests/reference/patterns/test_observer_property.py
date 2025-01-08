# **テストコード**
from reference.patterns.observer_property import Observable


def test_observable():
    """Observableクラスの基本動作をテスト"""
    # Observable インスタンスの作成
    observable = Observable()

    # 監視者を登録
    messages_a = []
    messages_b = []

    def observer_a(value):
        messages_a.append(f"Observer A notified with value: {value}")

    def observer_b(value):
        messages_b.append(f"Observer B notified with value: {value}")

    observable.add_observer(observer_a)
    observable.add_observer(observer_b)

    # 値の変更と通知
    observable.value = 10
    observable.value = 20

    # 結果を確認
    assert messages_a == [
        "Observer A notified with value: 10",
        "Observer A notified with value: 20",
    ]
    assert messages_b == [
        "Observer B notified with value: 10",
        "Observer B notified with value: 20",
    ]

    # Observer Bを削除し、通知内容を確認
    observable.remove_observer(observer_b)
    observable.value = 30

    assert messages_a == [
        "Observer A notified with value: 10",
        "Observer A notified with value: 20",
        "Observer A notified with value: 30",
    ]
    assert messages_b == [
        "Observer B notified with value: 10",
        "Observer B notified with value: 20",
    ]
