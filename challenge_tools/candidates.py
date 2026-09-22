"""Funciones iniciales de Campus Challenge.

Revisa su comportamiento según los requisitos de la actividad.
"""


def normalize_answer(answer):
    """Normaliza una respuesta para compararla sin distinguir mayúsculas."""
    return answer.strip().casefold()


def rotate_left(items, steps):
    """Devuelve una lista nueva rotada a la izquierda."""
    # (R-04): Se eliminó .rotate() (no existe en listas) y se usó slicing con modulo
    # para soportar colecciones vacías y pasos negativos.
    if not items:
        return []
    k = steps % len(items)
    return list(items[k:]) + list(items[:k])


def round_score_to_ten(score):
    """Redondea una puntuación no negativa a la decena más cercana."""
    # (R-05): Se reemplazó round() por división entera para evitar el redondeo al par (banker's rounding)
    # y garantizar que el .5 siempre redondee hacia arriba.
    return ((score + 5) // 10) * 10


def rank_teams(entries):
    """Ordena pares (equipo, puntuación) para la clasificación."""
    # (R-06): Se añadió item[0].casefold() a la clave de ordenamiento para
    # resolver empates alfabéticamente sin distinguir mayúsculas/minúsculas.
    return sorted(entries, key=lambda item: (-item[1], item[0].casefold()))


def unique_tags(tags):
    """Elimina etiquetas repetidas."""
    # (R-07): Se cambió set() por dict.fromkeys() para mantener el orden
    # de la primera aparición y respetar mayúsculas/minúsculas.
    return list(dict.fromkeys(tags))


def average_score(scores):
    """Devuelve la media aritmética de las puntuaciones."""
    # (R-08): Se añadió validación para listas vacías y evitar ZeroDivisionError.
    if not scores:
        return 0.0
    return float(sum(scores) / len(scores))