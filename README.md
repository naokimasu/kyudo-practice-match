# 対戦相手設定アプリ

大学弓道の対戦相手を設定するWebアプリです。

## 構成
相手の的中数をランダムで生成
（Pythonのrandomモジュールで生成、json形式で保存）
↓
順番に的中（◯×）を表示
（json形式の的中をJavaScriptに渡して表示）

## 使用技術
- Python
- Flask
- Render

## 起動方法
pip install -r requirements.txt
python app.py

こちらのURLからご利用いただけます。
https://kyudo-practice-match.onrender.com/
