"""
AAA - A3 - 3A
Arange - Act - Asserts!
Arrumar  - Agir - Garantir!
"""

from notas_musicais.escalas import NOTAS, escala


def test_deve_funcionar_com_notas_minusculas():
    # Arrumar
    tonica = 'c'
    tonalidade = 'maior'

    # Agir
    resultado = escala(tonica, tonalidade)

    # Garantir
    assert resultado


def test_deve_retornar_erro():
    # Arrumar
    tonica = 'x'
    tonalidade = 'maior'
    mensassem_erro = f'Essa nota não existe, tente uma dessas {NOTAS}'

    # Agir
    resultado = escala(tonica, tonalidade)

    # Garantir
    assert mensassem_erro in resultado
