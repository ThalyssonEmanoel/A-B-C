import re
import os

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as arquivo:
        senhas = arquivo.readlines()
    return [senha.strip() for senha in senhas]

def classificação(senha):
    senha = senha.strip()
    
    # Nível 1: Apenas letras
    if re.fullmatch(r'[a-zA-Z]+', senha):
        return 1
    
    # Nível 2: Letras seguidas por números entre 0 e 100
    match = re.fullmatch(r'([a-zA-Z]*)(\d{1,3})$', senha)
    if match:
        letras, num = match.groups()
        if num.isdigit() and int(num) <= 100:
            return 2
    
    # Nível 3: Letras seguidas por anos entre 1930 e 2030
    match = re.fullmatch(r'([a-zA-Z]*)(\d{4})$', senha)
    if match:
        letras, ano = match.groups()
        if ano.isdigit() and 1930 <= int(ano) <= 2030:
            return 3
    
    # Nível 4: Letras seguidas por números e depois letras novamente, exemplo: asd231dsa
    if re.fullmatch(r'[a-zA-Z]+\d+[a-zA-Z]+', senha):
        return 4
    
    # Nível 5: Contém caracteres especiais: !@#$%¨&*_+=-.;,?
    if re.search(r'[^a-zA-Z0-9]', senha):
        return 5
    
    # Nível 7: Senhas que começam com números
    if re.fullmatch(r'\d+', senha):
        return 7

    # Caso não se encaixe em nenhum nível
    return None

def selecionar_arquivo(nome_arquivo_entrada, nome_arquivo_saida):
    try:
        senhas = ler_arquivo(nome_arquivo_entrada)
        senhas_classificadas = [(senha, classificação(senha)) for senha in senhas]

        # Filtrar senhas sem classificação (None)
        senhas_classificadas = [(senha, dificuldade) for senha, dificuldade in senhas_classificadas if dificuldade is not None]

        # Ordenar usando a classificação
        senhas_classificadas.sort(key=lambda x: x[1])

        with open(nome_arquivo_saida, 'w', encoding='utf8') as arquivo_saida:
            for senha, dificuldade in senhas_classificadas:
                arquivo_saida.write(f'{senha}\n')

        print(f'As senhas foram adicionadas e salvas em {nome_arquivo_saida}.')
    
    except FileNotFoundError:
        print(f'O arquivo {nome_arquivo_entrada} não foi encontrado.')

base_dir = os.path.dirname(__file__)
nome_arquivo_entrada =  os.path.join(base_dir, '../data/test/dicionario-2.txt')
nome_arquivo_saida = os.path.join(base_dir, "../data/result/dicionario-final.txt")
selecionar_arquivo(nome_arquivo_entrada, nome_arquivo_saida)
