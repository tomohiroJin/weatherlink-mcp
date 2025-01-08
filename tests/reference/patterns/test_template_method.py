from reference.patterns.template_method import CSVDataProcessor, JSONDataProcessor


def test_csv_data_processor():
    """CSVDataProcessor のテンプレートメソッド動作を確認"""
    processor = CSVDataProcessor()
    processor.process()
    assert processor.result == "Processed CSV DATA"


def test_json_data_processor():
    """JSONDataProcessor のテンプレートメソッド動作を確認"""
    processor = JSONDataProcessor()
    processor.process()
    assert processor.result == "Processed {'key': 'VALUE'}"
