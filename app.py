from flask import Flask, render_template, request, session
import random, json, os
from flask_session import Session
from opponents import opponents

app = Flask(__name__)
# セッションを安全に使うために必要
app.secret_key = os.environ.get("SECRET_KEY")
# if not app.secret_key:
#     raise ValueError("SECRET_KEY is not set")

# セッション情報をサーバー側のファイルとして保存する
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# トップページを表示するときに行う処理
@app.route("/") #/にアクセスされた時、直後の関数を実行
def index(): 
    if "data" not in session:
        # 初期設定を作る（初回アクセス時の処理）
        num_people = 4
        total_shots = num_people * 4
        num = random.randint(0, len(opponents)-1)
        opponent = opponents[num] #対戦相手を設定
        lowHit = total_shots//2
        highHit = total_shots
        mode = "off"
    else:
        # すでに一度設定を保存したことがある場合
        data = session.get("data")
        num_people = data["num_people"]
        total_shots = data["total_shots"]
        opponent = data["opponent"]
        lowHit = data["lowHit"]
        highHit = data["highHit"]
        mode = data["mode"]

    # Python側の変数をHTMLへ渡す
    return render_template("index.html", opponents=opponents, num_people=num_people, total_shots=total_shots, opponent=opponent, lowHit=lowHit, highHit=highHit, mode=mode)

# 「行射開始」を押したあとの処理
@app.route("/kanteki", methods=["POST"])
def kanteki():
    # index.htmlから設定を受け取る
    opponent = request.form["opponent"]
    num_people = int(request.form["num_people"])
    lowHit = int(request.form["lowHit"])
    highHit = int(request.form["highHit"])
    display_speed = request.form["display_speed"] #"slow"/"normal"/"fast"を取得

    if request.form.get("mode") == "on":
        mode = "on"
    else:
        mode = "off"

    total_shots = num_people*4
    res, hit = make_result(lowHit, highHit, total_shots)
    
    display_time = 13500
    if display_speed == "slow":
        display_time = 15000
    elif display_speed == "normal":
        display_time = 13500
    else:
        display_time = 12000

    data = {
        "opponent": opponent,
        "num_people": num_people,
        "total_shots": total_shots,
        "lowHit": lowHit,
        "highHit": highHit,
        "mode": mode,
        "display_time": display_time,
    }

    session["data"] = data
    print(session)

    def save_json(data):    
        with open('static/data.json', 'w', encoding='utf-8') as f:
            json.dump(data,f, indent=4, ensure_ascii=False)
    
    save_json(data)
    # 要修正

    return render_template("kanteki.html", opponent=opponent, num_people=num_people, res=res, hit=hit)
    
@app.route("/kyousya", methods=["GET", "POST"])
def kyousya():
    data = session.get("data")
    opponent = data["opponent"]
    num_people = data["num_people"]
    max_hit = int(data["total_shots"]/2) #2本競射
    min_hit = int(max_hit/2)

    res, hit = make_result(min_hit, max_hit, max_hit)
    
    return render_template("kyousya.html", opponent=opponent, num_people=num_people, res=res, hit=hit)

@app.route("/kyousya2", methods=["GET", "POST"])
def kyousya2():
    data = session.get("data")
    opponent = data["opponent"]
    num_people = data["num_people"]
    max_hit = int(data["total_shots"]/4) #1本競射
    min_hit = int(max_hit/2)

    res, hit = make_result(min_hit, max_hit, max_hit)
    
    return render_template("kyousya2.html", opponent=opponent, num_people=num_people, res=res, hit=hit)

def make_result(min_hit, max_hit, total_shots):
    # 的中数をランダムに決める
    hit = random.randint(min_hit, max_hit)

    # 最初は全部○にする
    res = ["○"] * total_shots

    # 外れ本数を計算
    miss_count = total_shots - hit

    # 外れにする位置をランダムに選ぶ
    miss_positions = random.sample(range(total_shots), miss_count)

    # 選ばれた位置を×にする
    for position in miss_positions:
        res[position] = "×"

    return res, hit


if __name__ == "__main__":
    app.run(debug=True)