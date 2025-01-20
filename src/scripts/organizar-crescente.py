import re
import os

"""
 Esse script lê um arquivo de palavras e organiza as palavras na seguinte ordem:
  - palavras sem sufixo numérico;
  - palavras com sufixo numérico entre 0 e 100;
  - palavras com sufixo numérico entre 1930 e 2030;
  - O resto das palavras ele descarta.
"""

def ler_arquivo(nome_arquivo):
  with open(nome_arquivo, 'r',encoding='utf8') as arquivo:
    palavras = arquivo.readlines()
  return [palavra.strip() for palavra in palavras]

def organizar_por_sufixos(palavras):
  sem_sufixo = []
  sufixos_0_a_100 = []
  sufixos_1930_a_2030 = []

  for palavra in palavras:
    encontrou = re.search(r'(\d+)$', palavra)
    if encontrou:
      sufixo = int(encontrou.group(1))
      if 0 <= sufixo <= 100:
        sufixos_0_a_100.append(palavra)
      elif 1930 <= sufixo <= 2030:
        sufixos_1930_a_2030.append(palavra)
    else:
      sem_sufixo.append(palavra)

  sem_sufixo.sort()
  sufixos_0_a_100.sort()
  sufixos_1930_a_2030.sort()

  return sem_sufixo, sufixos_0_a_100, sufixos_1930_a_2030

def salvar_resultados(nome_arquivo, resultados):
  with open(nome_arquivo, 'w',encoding='utf8') as arquivo:
    for palavra in resultados[0]:
      arquivo.write(palavra + '\n')
    for palavra in resultados[1]:
      arquivo.write(palavra + '\n')
    for palavra in resultados[2]:
      arquivo.write(palavra + '\n')

def main():
  base_dir = os.path.dirname(__file__)
  nome_arquivo_entrada = os.path.join(base_dir, '../data/test/palavras-sufixos-numerados.txt')
  nome_arquivo_saida = os.path.join(base_dir, "../data/result/organizado-crescente.txt")

  palavras = ler_arquivo(nome_arquivo_entrada)
  resultados = organizar_por_sufixos(palavras)
  salvar_resultados(nome_arquivo_saida, resultados)

if __name__ == '__main__':
  main()
