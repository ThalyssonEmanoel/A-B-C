import os
'''
Esse script é responsável por gerar combinações especiais de palavras de um arquivo de texto. Fazendo substituições de vogais por números e caracteres especiais.
'''
def gerar_combinacoes_palavra(palavra):
  substituicoes = {'A': ['@', '4'], 'I': ['1'], 'O': ['0'], 'E': ['3']}#Aqui é onde é definido quais vogais serão substituídas por quais caracteres especiais.
  combinacoes = set()
  
  combinacoes.add(palavra)
  
  for i in range(len(palavra)):
    letra = palavra[i]
    if letra.upper() in substituicoes:
      vogal = letra.upper()
      substitutos = substituicoes[vogal]
      
      novas_combinacoes = set()
      for comb in combinacoes:
        for substituto in substitutos:
          nova_combinacao = comb[:i] + substituto + comb[i+1:]
          novas_combinacoes.add(nova_combinacao)
      combinacoes.update(novas_combinacoes)
  
  return combinacoes

def processar_arquivo(dicionario, dicionario_saida):
  with open(dicionario, 'r', encoding='utf-8') as file:  
    palavras = file.read().split()

  with open(dicionario_saida, 'w', encoding='utf-8') as file:
    for palavra in palavras:
      combinacoes = gerar_combinacoes_palavra(palavra)
      file.write('\n'.join(combinacoes) + '\n')
      
base_dir = os.path.dirname(__file__)
dicionario = os.path.join(base_dir, "../data/test/teste.txt")
dicionario_saida = os.path.join(base_dir, "../data/result/specialCombination.txt") 

processar_arquivo(dicionario, dicionario_saida)
print("As palavras com combinações especiais foram salvas em \"specialCombination.txt\"")