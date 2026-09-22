"""Añade pruebas para comportamientos no cubiertos en test_baseline.py.

Cada prueba debe:
- Tener un nombre que comience con test_.
- Comprobar el comportamiento mediante assert.
- Indicar el requisito correspondiente en un comentario o docstring.

Deriva el resultado esperado del requisito, no del resultado
que devuelve la implementación actual.
"""

from challenge_tools import (
    average_score,
    normalize_answer,
    rank_teams,
    rotate_left,
    round_score_to_ten,
    unique_tags,
)
# R-02: Inmutabilidad
def test_r02_inmutabilidad_colecciones():
    lista = [1, 2, 3]
    rotate_left(lista, 2)
    assert lista == [1, 2, 3]

# R-03: Normalización Unicode y espacios
def test_r03_normalize_answer_espacios_y_unicode():
    assert normalize_answer("  python  ") == "python"
    assert normalize_answer("STRAßE") == "strasse"

# R-04: Rotación izquierda, lista vacía y pasos negativos
def test_r04_rotate_left_vacia_y_negativos():
    assert rotate_left([], 5) == []
    assert rotate_left([1, 2, 3, 4], -1) == [4, 1, 2, 3]

# R-05: Redondeo a decena más cercana y mitad hacia arriba
def test_r05_round_score_mitad_hacia_arriba():
    assert round_score_to_ten(15) == 20
    assert round_score_to_ten(25) == 30

# R-06: Ordenar equipos y desempate alfabético case-insensitive
def test_r06_rank_teams_desempate():
    equipos = [("beta", 50), ("Alpha", 50)]
    assert rank_teams(equipos) == [("Alpha", 50), ("beta", 50)]

# R-07: Eliminar duplicados manteniendo orden y case-sensitive
def test_r07_unique_tags_case_sensitive():
    tags = ["code", "Code", "code"]
    assert unique_tags(tags) == ["code", "Code"]

# R-08: Promedio con lista vacía
def test_r08_average_score_vacia():
    assert average_score([]) == 0.0