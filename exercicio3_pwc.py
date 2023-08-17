"""
Encontre a substring palíndroma mais longa na string abaixo:
input = "babad"
output = "bab"
"""

palavra = input("Digite a palavra: ") #Recebe a palavra em uma string.

tam_palavra = len(palavra) #Mede o comprimento da palavra recebida.
maior_palin = "" #Inicializa uma string vazia.

for i in range(tam_palavra): #Percorre do zero até o número anterior ao tamanho da palavra e atribui o número a 'i'.
  for j in range(i, tam_palavra): #Percorre de 'i' até o número anterior ao tamanho da palavra e atribui o número a 'j'.
    teste_palin = palavra[i:j+1] #Cria uma substring da palavra no tamanho determinado.
    if teste_palin == teste_palin[::-1] and len(teste_palin) > len(maior_palin): #Verifica se é um palídromo e se é o maior.
      maior_palin = teste_palin #Atualiza qual é o maior palíndromo encontrado.

print(maior_palin) #Imprime o maior palindromo.