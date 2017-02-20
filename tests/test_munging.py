from munging import get_scores_year_range


def test_get_scores():
    scores = get_scores_year_range(2016, 2016)

    assert scores["team"][5] == "Baltimore Ravens" and scores["points"][5] == 13
    assert scores["team"][64] == "Houston Texans" and scores["points_for_per_game"][64] == 21.0
    assert scores["team"][64] == "Houston Texans" and scores["points_against_per_game"][64] == 13.0
