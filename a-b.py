def main():
    file_A = "teste.txt"
    file_B = "teste2.txt"
    
    # Cria um conjunto para armazenar palavras existentes
    palavras_existentes = set()
    
    '''
    1 - Lê o Arquivo B e adiciona suas palavras ao conjunto;
    2 - Remove espaços em branco;
    3 - Adiciona a palavra ao conjunto;
    4 - Adiciona à lista filtrada
    '''
    with open(file_B, 'r', encoding='utf-8') as file:
        for linha in file:
            palavra = linha.strip() 
            palavras_existentes.add(palavra)  
    
    # Lista para armazenar as palavras que não estão no Arquivo B
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
    
    file_C = "Subtracted.txt"
    
    # Salva as palavras filtradas em um novo arquivo
    with open(file_C, 'w', encoding='utf-8') as file:
        for palavra in DICIONÁRIO_COMPLETO_ID:
            file.write(palavra + '\n')  
    
    print(f"As palavras filtradas foram salvas em '{file_C}'.")

if __name__ == "__main__":
    main()  
