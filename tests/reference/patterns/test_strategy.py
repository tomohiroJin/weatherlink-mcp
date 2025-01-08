from reference.patterns.strategy import CreditCardPayment, PaymentContext, PayPalPayment


def test_credit_card_payment():
    """クレジットカード支払いのテスト"""
    strategy = CreditCardPayment("1234-5678-9876-5432", "John Doe")
    context = PaymentContext(strategy)
    result = context.execute_payment(100.0)
    assert result == "Paid 100.0 using Credit Card (John Doe)."


def test_paypal_payment():
    """PayPal支払いのテスト"""
    strategy = PayPalPayment("john.doe@example.com")
    context = PaymentContext(strategy)
    result = context.execute_payment(50.0)
    assert result == "Paid 50.0 using PayPal (john.doe@example.com)."


def test_dynamic_strategy_change():
    """支払い方法の動的切り替えテスト"""
    context = PaymentContext(CreditCardPayment("1234-5678-9876-5432", "John Doe"))
    result = context.execute_payment(75.0)
    assert result == "Paid 75.0 using Credit Card (John Doe)."

    context.set_strategy(PayPalPayment("john.doe@example.com"))
    result = context.execute_payment(25.0)
    assert result == "Paid 25.0 using PayPal (john.doe@example.com)."
