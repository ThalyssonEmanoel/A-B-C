import os

'''
Esse script é responsável por subtrair palavras de um arquivo A que estão contidas em um arquivo B. 
O resultado é salvo em um arquivo de texto chamado "Subtracted.txt".
'''
def main():
  base_dir = os.path.dirname(__file__)
  file_A = os.path.join(base_dir, "../data/test/teste.txt")
  file_B = os.path.join(base_dir, "../data/test/teste2.txt")
  result = os.path.join(base_dir, "../data/result/Subtracted.txt")
  
  palavras_existentes = set()
  
  if not os.path.exists(file_B):
    print(f"Error: The file '{file_B}' does not exist.")
    return

  with open(file_B, 'r', encoding='utf-8') as file:
    for linha in file:
      palavra = linha.strip() 
      palavras_existentes.add(palavra)  
  
  DICIONÁRIO_COMPLETO_ID = []

  with open(file_A, 'r', encoding='utf-8') as file:
    for linha in file:
      palavra = linha.strip()  
      if palavra not in palavras_existentes:  
        DICIONÁRIO_COMPLETO_ID.append(palavra)  
  
  with open(result, 'w', encoding='utf-8') as file:
    for palavra in DICIONÁRIO_COMPLETO_ID:
      file.write(palavra + '\n')  
  
  print(f"As palavras filtradas foram salvas em \"Subtracted.txt\"")

if __name__ == "__main__":
  main()