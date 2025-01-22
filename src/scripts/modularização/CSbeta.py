import itertools
import string
import os

class PasswordGenerator:
    def __init__(self, max_digitos_add=4, max_senhas_geradas=10000):
        self.max_digitos_add = max_digitos_add
        self.max_senhas_geradas = max_senhas_geradas

    def gerar_senha(self, base):
        palavras_array = set()
        digitos = string.digits
        especiais = "@#!%$*¨&\"'()_+-=§¬¢£³²{[}]ºª?/;:.,><|\\^~"

        palavras_array.add(base)

        for i in range(1, self.max_digitos_add + 1):
            for suffix in itertools.product(digitos, repeat=i):
                palavra = base + "".join(suffix)
                if palavra != base and 3 < len(palavra) < 9:
                    palavras_array.add(palavra)

        for i in range(1, self.max_digitos_add + 1):
            for prefix in itertools.product(especiais, repeat=i):
                palavra = "".join(prefix) + base
                if palavra != base and 3 < len(palavra) < 9:
                    palavras_array.add(palavra)

        for i in range(1, self.max_digitos_add + 1):
            for suffix in itertools.product(especiais, repeat=i):
                palavra = base + "".join(suffix)
                if palavra != base and 3 < len(palavra) < 9:
                    palavras_array.add(palavra)

        for i in range(1, self.max_digitos_add + 1):
            for mix in itertools.product(especiais, repeat=i):
                for j in range(1, len(base)):
                    palavra = base[:j] + "".join(mix) + base[j:]
                    if palavra != base and 3 < len(palavra) < 9:
                        palavras_array.add(palavra)

        return palavras_array

    def process_file(self, arquivo):
        with open(arquivo, 'r', encoding="utf8") as file:
            nomes = [line.strip() for line in file if line.strip()]

        Dicionario_Novo = []
        base_dir = os.path.dirname(__file__)
        Dicionario_Destino = os.path.join(base_dir, "../../data/result/Dicionario_Novo.txt")
        os.makedirs(os.path.dirname(Dicionario_Destino), exist_ok=True)
        for nome in nomes:
            palavras_array = self.gerar_senha(nome)

            if len(palavras_array) > self.max_senhas_geradas:
                palavras_array = set(list(palavras_array)[:self.max_senhas_geradas])

            Dicionario_Novo.extend(palavras_array)

        with open(Dicionario_Destino, "w", encoding="utf8") as file:
            for palavra in Dicionario_Novo:
                file.write(f"{palavra}\n")

        print("Todas as senhas foram salvas no arquivo 'Dicionario_Novo.txt'.")

def main():
    base_dir = os.path.dirname(__file__)
    arquivo = os.path.join(base_dir, "../../data/test/uma_palavra.txt")

    if not os.path.exists(arquivo):
        print(f"Arquivo '{arquivo}' não encontrado!")
        return

    max_digitos_add = 4
    max_senhas_geradas = 10000

    generator = PasswordGenerator(max_digitos_add, max_senhas_geradas)
    generator.process_file(arquivo)

if __name__ == "__main__":
    main()