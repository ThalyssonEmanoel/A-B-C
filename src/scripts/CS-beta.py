import itertools
import string
import os

'''
 CS(Criador de Senhas) - Script que gera senhas a partir de uma lista de palavras.
 ESSE CÓDIGO FOI >>INSPIRADO<< NO CÓDIGO DE GERAÇÃO DE SENHA "cupp" -> LINK: https://github.com/Mebus/cupp
- Cuidado com o a quantidade de palavras presente no arquivo "uma_palavra.txt", pois o número de senhas geradas por palavra é 10 mil.
- Cuidado com gerenciamento de memória do computador.
- O tamanho máximo de uma senha gerada é 8 caracteres. Até mesmo a palavra no arquivo "uma_palavra.txt" não pode ter mais de 8 caracteres.
- O tamanho mínimo de uma senha gerada é 4 caracteres.
- Os caracteres especiais que podem ser adicionados a uma senha gerada estão presentes na variável "especiais".
- A quantidade máxima de dígitos que podem ser adicionados a uma senha gerada é 4.
'''
def gerar_senha(base, max_digitos_add=4):
  palavras_array = set()
  digitos = string.digits
  especiais = "@#!%$*¨&\"'()_+-=§¬¢£³²{[}]ºª?/;:.,><|\\^~"

  palavras_array.add(base)

  for i in range(1, max_digitos_add + 1):
    for suffix in itertools.product(digitos, repeat=i):
      palavra = base + "".join(suffix)
      if palavra != base and 3 < len(palavra) < 9:
        palavras_array.add(palavra)

  for i in range(1, max_digitos_add + 1):
    for prefix in itertools.product(especiais, repeat=i):
      palavra = "".join(prefix) + base
      if palavra != base and 3 < len(palavra) < 9:
        palavras_array.add(palavra)

  for i in range(1, max_digitos_add + 1):
    for suffix in itertools.product(especiais, repeat=i):
      palavra = base + "".join(suffix)
      if palavra != base and 3 < len(palavra) < 9:
        palavras_array.add(palavra)

  for i in range(1, max_digitos_add + 1):
    for mix in itertools.product(especiais, repeat=i):
      for j in range(1, len(base)):
        palavra = base[:j] + "".join(mix) + base[j:]
        if palavra != base and 3 < len(palavra) < 9:
          palavras_array.add(palavra)

  return palavras_array

def process_file(arquivo, max_digitos_add=4, max_senhas_geradas=10000):
  with open(arquivo, 'r',encoding="utf8") as file:
    nomes = [line.strip() for line in file if line.strip()]

  Dicionario_Novo = []
  base_dir = os.path.dirname(__file__)
  Dicionario_Destino = os.path.join(base_dir, "../data/result/Dicionario_Novo.txt")
  os.makedirs(os.path.dirname(Dicionario_Destino), exist_ok=True)
  for nome in nomes:
    palavras_array = gerar_senha(nome, max_digitos_add)

    if len(palavras_array) > max_senhas_geradas:
      palavras_array = set(list(palavras_array)[:max_senhas_geradas])

    Dicionario_Novo.extend(palavras_array)

  with open(Dicionario_Destino, "w",encoding="utf8") as file:
    for palavra in Dicionario_Novo:
      file.write(f"{palavra}\n")

  print("Todas as senhas foram salvas no arquivo 'Dicionario_Novo.txt'.")

def main():
  base_dir = os.path.dirname(__file__)
  arquivo = os.path.join(base_dir, "../data/test/uma_palavra.txt")

  if not os.path.exists(arquivo):
    print(f"Arquivo '{arquivo}' não encontrado!")
    return

  max_digitos_add = 4
  max_senhas_geradas = 10000

  process_file(arquivo, max_digitos_add, max_senhas_geradas)

if __name__ == "__main__":
  main()