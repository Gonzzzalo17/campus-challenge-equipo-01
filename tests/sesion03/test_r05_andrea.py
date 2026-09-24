from challenge_tools.candidates import round_score_to_ten

def test_r05_round_score_to_ten_redondeo_estandar_y_mitad_exacta():
    """Requisito: Redondear puntuaciones enteras no negativas a la decena más cercana. Cuando el valor esté exactamente a mitad de camino, redondear hacia arriba."""
    assert round_score_to_ten(0) == 0
    assert round_score_to_ten(4) == 0
    assert round_score_to_ten(5) == 10
    assert round_score_to_ten(15) == 20
    assert round_score_to_ten(23) == 20
    assert round_score_to_ten(87) == 90
