NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
GRAUS = 'I II III IV V VI VII VIII IX X XI'.split()
ESCALAS = {
    'maior': {
        'intervalo': (0, 2, 4, 5, 7, 9, 11),
        'skip_grau': [],
    },
    'minor': {
        'intervalo': (0, 2, 3, 5, 7, 8, 10),
        'skip_grau': [],
    },
    'pentatonica': {
        'intervalo': (0, 2, 4, 7, 9),
        'skip_grau': [3, 6],
    },
    'pentatonica menor': {
        'intervalo': (0, 3, 5, 7, 10),
        'skip_grau': [1, 5],
    },
}


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
    grau = 0
    graus = list()
    notas = list()

    for intervalo in ESCALAS[tonalidade]['intervalo']:
        i = (intervalo + NOTAS.index(tonica.upper())) % len(NOTAS)
        notas.append(NOTAS[i])

        if grau in ESCALAS[tonalidade]['skip_grau']:
            graus.append(GRAUS[grau + 1])
            grau += 2
        else:
            graus.append(GRAUS[grau])
            grau += 1

    return {'notas': notas, 'graus': graus}
