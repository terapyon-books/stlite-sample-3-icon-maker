# Streamlitデモアプリ

- 名称: stlite-sample-3-icon-maker
- 目的: アイコンを生成
- 機能: アイコン用PNGファイルを作成

このレポジトリは、XXXX用のサンプルデモアプリです。
さらに、@stlite/desktopに対応させ、OSにインストール可能なアプリです。


## 機能詳細

- フォントアイコンを選ぶ
- キーイメージをアップロード
- バックグラウンドの色を選ぶ
- 画像を確認
- PNGファイルをダウンロード


## セットアップ

### 必須条件

- Python 3.11 (3.8以上)
- Streamlit 1.31以上
- npm or yarn (node v18以降)

### 仮想環境

venvを用いてインストールを行います。
venvは、Pythonの標準ライブラリです。

https://docs.python.org/ja/3/tutorial/venv.html


```sh
% cd (任意のフォルダ)
% python3 -m venv venv
% source venv/bin/activate
```

### インストール

単体インストール

```sh
(venv) % pip install streamlit
```

GitHubからパッケージをダウンロードしてインストール（推奨）

```sh
(venv) % git clone https://github.com/terapyon-books/stlite-sample-3-icon-maker.git
(venv) % stlite-sample-3-icon-maker
(venv) % pip install -r requirements.txt -c constraints.txt
```

### node

```sh
% nvm use v20
% npm install
```

## 起動方法

```
(venv) % streamlit run sample_3_icon_maker/streamlit_app.py
```

## 表示確認

起動すると、デフォルトブラウザが立ち上がり表示確認ができる。

もし、ブラウザが立ち上がらない場合は、コンソールに表示されるポート付URLをブラウザで呼び出す。


# LICENCE

This package is under MIT License.
Please see [LICENSE](LICENSE) file.
