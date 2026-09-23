from challenge_tools.candidates import normalize_answer

def test_normalize_answer_strips_outer_whitespace():
    """Requisito: Recortar los espacios en blanco exteriores (espacios, saltos de linea y tabulaciones)."""
    assert normalize_answer("\n\t  texto con espacios  \t\n") == "texto con espacios"


def test_normalize_answer_unicode_case_insensitive():
    """Requisito: Normalizar respuestas para comparaciones sin distinción de mayúsculas/minúsculas compatibles con Unicode."""
    assert normalize_answer("  MÜNCHEN  ") == "münchen"