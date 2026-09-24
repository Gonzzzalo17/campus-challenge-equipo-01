from challenge_tools import rank_teams


def test_rank_teams_breaks_tie_alphabetically_case_insensitive():
    # R-06: con puntuaciones empatadas, el desempate es alfabético
    # y no distingue mayúsculas/minúsculas ("alpha" antes que "beta").
    assert rank_teams([("beta", 20), ("Alpha", 20)]) == [
        ("Alpha", 20),
        ("beta", 20),
    ]