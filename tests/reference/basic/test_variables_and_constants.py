# **テストコード**
# 各変数やデータ構造が正しく動作するかを確認する
import reference.basic.variables_and_constants as vc


def test_basic_variables():
    """基本的な変数の型と値を確認する"""
    assert isinstance(vc.name, str), "nameは文字列であるべきです。"
    assert isinstance(vc.age, int), "ageは整数であるべきです。"
    assert isinstance(vc.height, float), "heightは浮動小数点数であるべきです。"
    assert isinstance(vc.is_student, bool), "is_studentはブール型であるべきです。"


def test_constants():
    """定数の値を確認する"""
    assert vc.PI == 3.14159, "PIは3.14159であるべきです。"
    assert vc.MAX_USERS == 100, "MAX_USERSは100であるべきです。"


def test_list_operations():
    """リスト操作の動作を確認する"""
    assert vc.fruits == [
        "apple",
        "banana",
        "cherry",
        "date",
    ], "リスト操作の結果が正しくありません。"


def test_dictionary_operations():
    """辞書操作の動作を確認する"""
    assert vc.student["name"] == "Alice", "辞書の値が正しくありません。"
    assert vc.student["major"] == "Physics", "辞書のキー追加が正しくありません。"


def test_tuple():
    """タプルの値を確認する"""
    assert vc.point == (10, 20), "タプルの値が正しくありません。"


def test_set_operations():
    """集合操作の動作を確認する"""
    assert vc.unique_numbers == {1, 2, 3, 4}, "集合操作の結果が正しくありません。"


def test_unpacking():
    """アンパック操作の動作を確認する"""
    assert vc.x == 1 and vc.y == 2 and vc.z == 3, "複数代入が正しくありません。"
    assert vc.first == 10 and vc.rest == [
        20,
        30,
        40,
    ], "リストのアンパックが正しくありません。"
