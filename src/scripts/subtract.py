import os

def main():
    base_dir = os.path.dirname(__file__)
    file_A = os.path.join(base_dir, "../data/test/teste.txt")
    file_B = os.path.join(base_dir, "../data/test/teste2.txt")
    file_C = os.path.join(base_dir, "../data/result/Subtracted.txt")
    
    palavras_existentes = set()
    
    '''
    1 - Lê o Arquivo B e adiciona suas palavras ao conjunto;
    2 - Remove espaços em branco;
    3 - Adiciona a palavra ao conjunto;
    4 - Adiciona à lista filtrada
    '''
    if not os.path.exists(file_B):
        print(f"Error: The file '{file_B}' does not exist.")
        return

    with open(file_B, 'r', encoding='utf-8') as file:
        for linha in file:
            palavra = linha.strip() 
            palavras_existentes.add(palavra)  
    
    DICIONÁRIO_COMPLETO_ID = []

    '''
    1 - Lê o Arquivo A e filtra as palavras;
    2 - Remove espaços em branco;
    3 - Verifica se a palavra está no conjunto;
    4 - Adiciona à lista filtrada
    '''
    with open(file_A, 'r', encoding='utf-8') as file:
        for linha in file:
            palavra = linha.strip()  
            if palavra not in palavras_existentes:  
                DICIONÁRIO_COMPLETO_ID.append(palavra)  
    
    with open(file_C, 'w', encoding='utf-8') as file:
        for palavra in DICIONÁRIO_COMPLETO_ID:
            file.write(palavra + '\n')  
    
    print(f"As palavras filtradas foram salvas em '{file_C}'.")

if __name__ == "__main__":
    main()