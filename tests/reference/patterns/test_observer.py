# **テストコード**
from reference.patterns.observer import (
    ConcreteObserverA,
    ConcreteObserverB,
    Subject,
)


def test_observer_pattern():
    """Observer パターンの基本的な動作テスト"""
    subject = Subject()
    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()

    subject.add_observer(observer_a)
    subject.add_observer(observer_b)

    # 状態の変化を通知
    subject.notify_observers("Event 1")
    assert observer_a.messages == ["ObserverA received: Event 1"]
    assert observer_b.messages == ["ObserverB received: Event 1"]

    # ObserverBを削除し、新たな通知
    subject.remove_observer(observer_b)
    subject.notify_observers("Event 2")
    assert observer_a.messages == [
        "ObserverA received: Event 1",
        "ObserverA received: Event 2",
    ]
    assert observer_b.messages == ["ObserverB received: Event 1"]
