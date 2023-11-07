NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
GRAUS = 'I II III IV V VI VII'.split()
ESCALAS = {
    'maior': {'intervalo': (0, 2, 4, 5, 7, 9, 11), 'grau': GRAUS},
    'minor': {'intervalo': (0, 2, 3, 5, 7, 8, 10), 'grau': GRAUS},
    'pentatonica': {
        'intervalo': (0, 2, 4, 7, 9),
        'grau': 'I II III V VI'.split(),
    },
    'pentatonica menor': {
        'intervalo': (0, 3, 5, 7, 10),
        'grau': 'I III IV V VII'.split(),
    },
}

DOZE_NOTAS = len(NOTAS)


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tônica e uma tonalidade

    Parameters:
        tonica: Nota que será a tonica da escala
        tonalidade: Tonalidade da escala

    Returns:
        Um dicionário com as notas da escala e o graus

    escala('c', 'maior')
    {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

    escala('a', 'maior')
    {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

    Examples:
        >>> escala('D', 'pentatonica')
        {'notas': ['D', 'E', 'F#', 'A', 'B'], 'graus': ['I', 'II', 'III', 'V', 'VI']}

        >>> escala('C', 'pentatonica menor')
        {'notas': ['C', 'D#', 'F', 'G', 'A#'], 'graus': ['I', 'III', 'IV', 'V', 'VII']}
    """
    intervalo_escala = ESCALAS[tonalidade]['intervalo']
    notas = list()
    tonica_posicao = NOTAS.index(tonica.upper())

    for intervalo in intervalo_escala:
        posicao_nota = (intervalo + tonica_posicao) % DOZE_NOTAS
        notas.append(NOTAS[posicao_nota])

    return {'notas': notas, 'graus': ESCALAS[tonalidade]['grau']}
