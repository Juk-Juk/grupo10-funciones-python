from funciones.dividir_mirna import dividir_mirna

def test_dividir_mirna():
    assert dividir_mirna(10, 2) == 5
    assert dividir_mirna(5, 0) is None
    assert dividir_mirna(-9, 3) == -3
