"""
このモジュールではPythonのクラスについて詳しく説明します。
クラスはオブジェクト指向プログラミングの基本単位であり、データとそれに関連する操作をまとめます。
基本的なクラス定義、コンストラクタ、メソッド、クラス変数、インスタンス変数、
継承、特殊メソッド（__str__など）について解説します。
"""


# **基本的なクラスの定義**
class Person:
    """
    人を表すクラス。
    Attributes:
        name (str): 名前。
        age (int): 年齢。
    """

    def __init__(self, name, age):
        """
        Personクラスのコンストラクタ。
        Args:
            name (str): 名前。
            age (int): 年齢。
        """
        self.name = name
        self.age = age

    def introduce(self):
        """
        自己紹介メッセージを生成します。
        Returns:
            str: 自己紹介メッセージ。
        """
        return f"My name is {self.name} and I am {self.age} years old."


# **クラス変数とインスタンス変数**
class Counter:
    """
    インスタンスごとにカウントを管理するクラス。
    クラス全体の総カウントも管理します。
    """

    total_count = 0  # クラス変数

    def __init__(self):
        self.instance_count = 0  # インスタンス変数

    def increment(self):
        """
        インスタンスとクラスのカウントを1増やします。
        """
        self.instance_count += 1
        Counter.total_count += 1


# **継承**
class Employee(Person):
    """
    従業員を表すクラス。
    Personクラスを継承。
    Attributes:
        name (str): 名前。
        age (int): 年齢。
        job_title (str): 職位。
    """

    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    def introduce(self):
        """
        従業員用の自己紹介メッセージを生成します。
        Returns:
            str: 自己紹介メッセージ。
        """
        return (
            f"My name is {self.name}, I am {self.age} years old, "
            f"and I work as a {self.job_title}."
        )


# **特殊メソッド**
class Vector:
    """
    2次元ベクトルを表すクラス。
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        2つのベクトルを加算します。
        Args:
            other (Vector): 加算するもう1つのベクトル。
        Returns:
            Vector: 加算された結果のベクトル。
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        """
        ベクトルの文字列表現を返します。
        Returns:
            str: ベクトルの文字列表現。
        """
        return f"Vector({self.x}, {self.y})"
