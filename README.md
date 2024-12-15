# Devcontainer Python

このリポジトリは、Pythonプロジェクトの開発環境を簡単に構築できるDevcontainerを利用したテンプレートです。必要なツールや依存関係があらかじめ設定されており、一貫した開発環境を提供します。

## 特徴

- Python 3.11 を使用
- あらかじめインストールされているツール:
  - `pytest`（テスト用）
  - `flake8`（コードリント用）
  - `black`（コードフォーマット用）
- Devcontainer による開発環境の構築
- Dockerベースの隔離された環境で、設定の一貫性を保証

## はじめに

以下の手順で、この開発環境を利用できます。

1. このリポジトリをクローンします:

   ```bash
   git clone https://github.com/tomohiroJin/devcontainer-python.git
   cd devcontainer-python
   ```

2. VS Code でプロジェクトを開きます:

   ```bash
   code .
   ```

3. Devcontainerでプロジェクトを再オープンするように求められたら、指示に従って再オープンします。

4. セットアップを確認するためにテストを実行します:

   ```bash
   pytest
   ```

## プロジェクト構成

```plaintext
devcontainer-python/
├── .devcontainer/        # Devcontainer設定ファイル
├── src/                  # ソースコード
│   └── hello_world/      # サンプルモジュール
│       ├── __init__.py
│       └── main.py       # サンプルコード
├── tests/                # テストコード
│   ├── __init__.py
│   └── test_hello_world/ # hello_worldモジュール用テスト
│       ├── __init__.py
│       └── test_main.py  # サンプルテスト
├── requirements.txt      # Python依存関係
├── pytest.ini            # pytest設定ファイル
└── README.md             # プロジェクトの説明
```

## 使用方法

- `src/` ディレクトリにPythonコードを追加してください。
- `tests/` ディレクトリにテストコードを作成してください。サンプルの構造を参考にしてください。
- 開発中は必要に応じて `pytest` や `flake8` を実行してコードをチェックできます。

## カスタマイズ

`.devcontainer/devcontainer.json` ファイルを編集することで、開発環境をカスタマイズできます。  
例えば、Pythonのバージョンを変更したり、追加のツールをインストールする設定を追加することが可能です。

## ライセンス

このプロジェクトはMITライセンスの下で提供されています。
