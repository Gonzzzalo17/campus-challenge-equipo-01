from challenge_tools import (
    average_score,
    normalize_answer,
    rank_teams,
    rotate_left,
    round_score_to_ten,
    unique_tags,
)


# ==========================================
# REQUISITO R-07: unique_tags
# ==========================================

def test_r07_unique_tags_mayusculas_y_orden():
    """
    R-07: Comprueba que unique_tags no elimine elementos con distinta
    capitalización (Unicode) y conserve el orden de primera aparición.
    """
    etiquetas = ["python", "git", "Python", "git", "GIT"]
    esperado = ["python", "git", "Python", "GIT"]

    assert unique_tags(etiquetas) == esperado


def test_r07_tu_caso_adicional():
    """
    Agrega aquí tu propio caso de prueba para R-07.
    Ejemplo: probar cadenas vacías o caracteres especiales.
    """
    # Escribe aquí tu lista de entrada y el resultado esperado
    etiquetas = ["dev", "DEV", "dev"]
    esperado = ["dev", "DEV"]

    assert unique_tags(etiquetas) == esperado
# R-07: Eliminar duplicados manteniendo orden y case-sensitive
def test_r07_unique_tags_case_sensitive():
    tags = ["code", "Code", "code"]
    assert unique_tags(tags) == ["code", "Code"]
