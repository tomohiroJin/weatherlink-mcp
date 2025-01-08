"""
Template Method パターンは、アルゴリズムの骨格をスーパークラスで定義し、
サブクラスで詳細な処理を実装するデザインパターンです。

このファイルでは、Template Method パターンを Python で実装し、
テストコードを含めています。
"""

from abc import ABC, abstractmethod


# **抽象クラス**
class DataProcessor(ABC):
    """
    データ処理のテンプレートクラス。
    """

    def process(self):
        """
        データ処理のテンプレートメソッド。
        """
        self.read_data()
        self.process_data()
        self.save_data()

    @abstractmethod
    def read_data(self):
        """
        データの読み込みを行う抽象メソッド。
        """
        pass

    @abstractmethod
    def process_data(self):
        """
        データの処理を行う抽象メソッド。
        """
        pass

    @abstractmethod
    def save_data(self):
        """
        データの保存を行う抽象メソッド。
        """
        pass


# **具体的なクラス**
class CSVDataProcessor(DataProcessor):
    def read_data(self):
        self.data = "CSV data"

    def process_data(self):
        self.data = self.data.upper()

    def save_data(self):
        self.result = f"Processed {self.data}"


class JSONDataProcessor(DataProcessor):
    def read_data(self):
        self.data = {"key": "value"}

    def process_data(self):
        self.data["key"] = self.data["key"].upper()

    def save_data(self):
        self.result = f"Processed {self.data}"
