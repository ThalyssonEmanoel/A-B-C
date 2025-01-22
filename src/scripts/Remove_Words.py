import re
import os

"""
 Esse script tem como objetivo remover palavras de um arquivo de texto que contenham caracteres especiais e números. Restando apenas palavras com letras e com tamanho entre 4 e 9 caracteres.
"""
def filtrar_senhas(arquivo_entrada, arquivo_saida):
  with open(arquivo_entrada, 'r', encoding='utf-8') as f:
    linhas = f.readlines()

  senhas_filtradas = []

  caracteres_especiais_numeros = re.compile(r'[!@#$%^`\'\"&*=¨%§£;~´(),.¡?":¢¬º+\[\] \-_/{}|<> 0-9\']|\\') #Remover o 0-9 para manter números

  for senha in linhas:
    senha = senha.strip()

    if len(senha) > 3 and len(senha) < 10 and not caracteres_especiais_numeros.search(senha):#Aqui define o tamanho das palavras que serão mantidas, deverão ser entre 4 e 9 caracteres
      senhas_filtradas.append(senha)

  with open(arquivo_saida, 'w', encoding='utf-8') as f:
    for senha in senhas_filtradas:
      f.write(senha + '\n')

  print(f"Senhas filtradas foram salvas em \"SEM_CARACTER_ESPECIAL\".")

base_dir = os.path.dirname(__file__)
arquivo_entrada = os.path.join(base_dir, "../data/test/palavras.txt") 
arquivo_saida = os.path.join(base_dir, "../data/result/SEM_CARACTER_ESPECIAL.txt")

filtrar_senhas(arquivo_entrada, arquivo_saida)
