
from transformers import AutoTokenizer

class MonitorDeTokens:
    def __init__(self, modelo="gpt2"):
        self.tokenizer = AutoTokenizer.from_pretrained(modelo)

    def contar(self, texto):
        return len(self.tokenizer.encode(texto))

    def atualizar(self, entrada, saida):
        tokens_entrada = self.contar(entrada)
        tokens_saida = self.contar(saida)

        print("\n--- USO DE TOKENS (via HuggingFace) ---")
        print(f"Tokens na entrada: {tokens_entrada}")
        print(f"Tokens na saída:   {tokens_saida}")
        print(f"Total:             {tokens_entrada + tokens_saida}")
