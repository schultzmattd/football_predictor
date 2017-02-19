from munging import get_scores


def test_get_scores():

    scores = get_scores(2015,5)

    assert scores["points"][5] == 38
    assert scores["team"][5] == "Tampa Bay Buccaneers"