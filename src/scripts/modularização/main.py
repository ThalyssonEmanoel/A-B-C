from CSbeta import PasswordGenerator
from CaracteresEspeciais import SpecialCharacterGenerator
import os

def main():
    base_dir = os.path.dirname(__file__)
    arquivo_senhas = os.path.join(base_dir, "../../data/test/uma_palavra.txt")
    arquivo_combinacoes = os.path.join(base_dir, "../../data/test/teste.txt")

    if not os.path.exists(arquivo_senhas):
        print(f"Arquivo '{arquivo_senhas}' não encontrado!")
        return

    if not os.path.exists(arquivo_combinacoes):
        print(f"Arquivo '{arquivo_combinacoes}' não encontrado!")
        return

    max_digitos_add = 4
    max_senhas_geradas = 10000

    password_generator = PasswordGenerator(max_digitos_add, max_senhas_geradas)
    password_generator.process_file(arquivo_senhas)

    special_char_generator = SpecialCharacterGenerator()
    dicionario_saida = os.path.join(base_dir, "../data/result/specialCombination.txt")
    special_char_generator.processar_arquivo(arquivo_combinacoes, dicionario_saida)

if __name__ == "__main__":
    main()
