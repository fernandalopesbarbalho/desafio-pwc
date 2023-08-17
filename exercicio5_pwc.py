"""
Verifique se a string é um anagrama de um palíndromo. Exemplo:
input = "racecar"
output = "true"
"""

palavra = input("Digite a palavra: ") #Recebe a palavra em uma string.

contar_letras = {} #Cria um dicionário vazio que irá armazenar o número de vezes que cada letra se repete.

for i in palavra: #Percorre cada caractere na frase.
  contar_letras[i] = contar_letras.get(i, 0) + 1 #Adiciona na chave da letra o seu valor.

contador = 0 #Inicializa um contador zerado.

for i in contar_letras.values(): #Percorre os valores do dicionário.
  if i % 2 != 0: #Verifica se o valor é ímpar.
    contador += 1 #Se sim, adiciona 1 ao contador.

if contador <= 1: #Verifica se o contador é menor ou igual a 1.
  print("true") #Imprime que é um anagrama de um palíndromo.
  
else: #Caso o contador for maior que 1.
  print("false") #Imprime que não é um anagrama de um palíndromo.