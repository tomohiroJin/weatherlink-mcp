# **テストコード**
# 条件分岐とループに関するテストを記述
import reference.basic.conditionals_and_loops as cal


def test_if_elif_else():
    """if-elif-else文による判定が正しいことを確認する"""
    assert cal.grade == "B", "スコア85はグレードBであるべきです。"


def test_ternary_operator():
    """三項演算子の結果を確認する"""
    assert cal.is_even == "奇数", "スコア85は奇数であるべきです。"


def test_for_loop():
    """forループで平方計算が正しいことを確認する"""
    assert cal.squares == [1, 4, 9, 16, 25], "平方計算の結果が正しくありません。"


def test_while_loop():
    """whileループでカウントアップが正しいことを確認する"""
    assert cal.counts == [0, 1, 2], "カウントアップの結果が正しくありません。"


def test_break_and_continue():
    """breakとcontinueの動作が正しいことを確認する"""
    assert cal.filtered_numbers == [1, 3], "ループ制御の結果が正しくありません。"


def test_list_comprehension():
    """リスト内包表記での立方計算が正しいことを確認する"""
    assert cal.cubes == [1, 27, 125], "リスト内包表記の結果が正しくありません。"
