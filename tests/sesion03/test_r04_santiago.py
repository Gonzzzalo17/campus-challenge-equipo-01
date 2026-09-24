from challenge_tools import rotate_left


def test_rotate_left_negative_steps_rotates_right():
    # R-04: un número de pasos negativo se interpreta como rotación
    # hacia la derecha. Rotar [1,2,3,4,5] -1 a la izquierda equivale
    # a rotar 1 paso a la derecha: el último elemento pasa al frente.
    assert rotate_left([1, 2, 3, 4, 5], -1) == [5, 1, 2, 3, 4]