from game_logic import make_result


def test_result_length():
    res, hit = make_result(5, 10, 16)

    assert len(res) == 16


def test_hit_count_matches_result():
    res, hit = make_result(5, 10, 16)

    assert res.count("○") == hit
    assert res.count("×") == 16 - hit


def test_hit_is_within_range():
    res, hit = make_result(5, 10, 16)

    assert 5 <= hit <= 10


def test_all_hits():
    res, hit = make_result(16, 16, 16)

    assert hit == 16
    assert res == ["○"] * 16