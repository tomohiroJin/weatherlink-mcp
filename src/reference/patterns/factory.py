"""
Factory パターンは、オブジェクトの生成を専門とするクラス（ファクトリ）を提供し、
その生成ロジックをカプセル化するデザインパターンです。

このファイルでは、Factory パターンを Python で実装し、テストコードを含めています。
"""


# **プロダクトクラス**
class Shape:
    """
    Shape の基底クラス。
    """

    def draw(self) -> str:
        raise NotImplementedError("Subclasses must implement 'draw' method.")


class Circle(Shape):
    def draw(self) -> str:
        return "Drawing a Circle"


class Square(Shape):
    def draw(self) -> str:
        return "Drawing a Square"


class Triangle(Shape):
    def draw(self) -> str:
        return "Drawing a Triangle"


# **ファクトリクラス**
class ShapeFactory:
    """
    Shape オブジェクトを生成するファクトリクラス。
    """

    @staticmethod
    def create_shape(shape_type: str) -> Shape:
        """
        指定された種類の Shape オブジェクトを生成します。
        Args:
            shape_type (str): 作成する Shape の種類。
        Returns:
            Shape: 指定された種類の Shape インスタンス。
        Raises:
            ValueError: 未知の shape_type の場合。
        """
        shapes = {
            "circle": Circle,
            "square": Square,
            "triangle": Triangle,
        }
        if shape_type not in shapes:
            raise ValueError(f"Unknown shape type: {shape_type}")
        return shapes[shape_type]()
