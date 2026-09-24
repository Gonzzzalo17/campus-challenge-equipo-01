from challenge_tools import (
    average_score,
    normalize_answer,
    rank_teams,
    rotate_left,
    round_score_to_ten,
    unique_tags,
)


def test_r08_average_score_media_decimal():
    """
    R-08: Comprueba el cálculo del promedio cuando el resultado
    no es un entero exacto (da un decimal).
    """
    puntuaciones = [10, 15]
    esperado = 12.5

    assert average_score(puntuaciones) == esperado


def test_r08_average_score_un_solo_elemento():
    """
    R-08: Comprueba el promedio cuando la lista solo contiene 1 elemento.
    """
    puntuaciones = [85.5]
    esperado = 85.5

    assert average_score(puntuaciones) == esperado