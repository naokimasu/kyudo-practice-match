import random

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