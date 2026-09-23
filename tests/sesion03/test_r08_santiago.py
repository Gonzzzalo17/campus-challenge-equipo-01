from challenge_tools import average_score


def test_average_score_returns_zero_for_empty_collection():
    # R-08: para una colección vacía de puntuaciones, la media debe
    # ser 0.0 en vez de lanzar un error de división por cero.
    assert average_score([]) == 0.0