def analisar_sentimento(texto):
    texto_lower = texto.lower()

    positivo = ["bom", "ótimo", "excelente", "melhor", "positivo", "ganhou", "recorde"]
    negativo = ["ruim", "péssimo", "crise", "queda", "negativo", "perdeu", "fraude"]

    score = 0

    for p in positivo:
        if p in texto_lower:
            score += 1

    for n in negativo:
        if n in texto_lower:
            score -= 1

    if score > 0:
        return "POSITIVO"
    elif score < 0:
        return "NEGATIVO"
    else:
        return "NEUTRO"
