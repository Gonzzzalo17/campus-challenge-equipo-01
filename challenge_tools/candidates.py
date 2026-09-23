"""Funciones iniciales de Campus Challenge.

Revisa su comportamiento según los requisitos de la actividad.
"""


def normalize_answer(answer):
    """Normaliza una respuesta para compararla sin distinguir mayúsculas"""
    return answer.strip().casefold()


def rotate_left(items, steps):
    """La rotación izquierda debe ser circular, admitir una lista vacía e interpretar los pasos negativos como una rotación hacia la derecha."""
    if not items:
        return list(items)

    shift = steps % len(items)
    return list(items[shift:]) + list(items[:shift])


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
    """Elimina etiquetas duplicadas conservando la primera aparición y el orden.

    R-07: la comparación distingue mayúsculas y minúsculas,
    y se conserva el orden original de la primera aparición.
    R-02: se construye una lista nueva; 'tags' no se modifica.
    """
    seen = set()
    result = []
    for tag in tags:
        if tag not in seen:
            seen.add(tag)
            result.append(tag)
    return result


def average_score(scores):
    """Devuelve la media aritmética de las puntuaciones.

    R-08: para una colección vacía devuelve 0.0.
    """
    if not scores:
        return 0.0
    return sum(scores) / len(scores)