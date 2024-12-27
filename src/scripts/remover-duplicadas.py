from collections import OrderedDict
import os
'''
@remove_duplicates - Função que remove palavras duplicadas de um arquivo de texto.
'''
def remove_duplicates(arquivo_base, arquivo_final):
  
  palavras_unicas = OrderedDict()

  with open(arquivo_base, 'r', encoding='utf-8') as file:
    for line in file:
      palavra = line.strip()
      palavras_unicas[palavra] = None

  with open(arquivo_final, 'w', encoding='utf-8') as file:
    for palavra in palavras_unicas:
      file.write(palavra + '\n')

  print(f"Palavras únicas foram escritas no arquivo: {arquivo_final}")

base_dir = os.path.dirname(__file__)
arquivo_base = os.path.join(base_dir, "../data/test/dicionario-1.txt")
arquivo_final = os.path.join(base_dir, "../data/result/dicionario-1-sem-duplicadas.txt")

remove_duplicates(arquivo_base, arquivo_final)
