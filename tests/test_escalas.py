"""
AAA - A3 - 3A
Arange - Act - Asserts!
Arrumar  - Agir - Garantir!
"""

from notas_musicais.escalas import escala


def test_escala_deve_funcionar_com_notas_minusculas():
    # Arrumar
    tonica = 'c'
    tonalidade = 'maior'

    # Agir
    resultado = escala(tonica, tonalidade)

    # Garantir
    assert resultado
