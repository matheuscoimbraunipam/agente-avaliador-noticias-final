def analisar_sentimento(texto):
    texto_lower = texto.lower()

    # Palavras simples, mas funciona p/ atividade
    positivo = ["bom", "ótimo", "excelente", "melhor", "positivo", "ganhou", "recorde", "sucesso"]
    negativo = ["ruim", "péssimo", "crise", "queda", "negativo", "perdeu", "fraude", "derrota"]

    score = 0

    for p in positivo:
        if p in texto_lower:
            score += 1

    for n in negativo:
        if n in texto_lower:
            score -= 1

    if score >= 0:
        return "POSITIVO"
    else:
        return "NEGATIVO"
