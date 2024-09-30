# Filtrador de palavras
Este script em Python é um script simples para filtrar palavras de um arquivo, removendo aquelas que já existem em outro arquivo. O resultado é salvo em um novo arquivo.

## Funcionalidade
O código realiza as seguintes operações:

1. Leitura de Arquivos:
- Lê duas listas de palavras a partir de arquivos de texto:
  - `teste.txt` (Arquivo_A): Contém a lista de palavras a serem filtradas.
  - `teste2.txt` (Arquivo_B): Contém a lista de palavras que já existem e que não devem ser incluídas no resultado.

2. Filtragem:
- Compara as palavras do Arquivo_A com as palavras do Arquivo_B e cria uma nova lista que contém apenas as palavras que não estão presentes no Arquivo B.

3. Saída:
- Salva a lista filtrada em um novo arquivo chamado Subtraído.txt.

## Estrutura do Código

- Uso de Conjuntos: Utiliza um conjunto (`set`) para armazenar as palavras existentes, permitindo uma verificação rápida durante a filtragem.

## Como Usar

1. Preparação:
- Certifique-se de que os arquivos `teste.txt` e `teste2.txt` estão na mesma pasta que o script.

2. Execução:
- Execute o script:

```
python a-b.py
```

## Conclusão
   Este script é útil para gerenciar listas de palavras, garantindo que palavras já existentes sejam removidas de uma nova lista. É uma solução prática para situações em que você precisa lidar com palavras duplicadas. Ele é
bastante útil quando se trata de arquivos muito extensos...