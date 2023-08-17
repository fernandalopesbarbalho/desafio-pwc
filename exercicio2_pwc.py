"""
Remova todos os caracteres duplicados da string abaixo:
input = "Hello, World!"
output = "Helo, Wrd!"
"""

frase = input("Digite a frase: ") #Recebe a frase em uma string.
frase_nova = "" #Inicializa uma string vazia.

for i in frase: #Percorre cada caractere na frase.
  if i not in frase_nova: #Verifica se o caractere já está na nova string.
    frase_nova += i #Adiciona o caractere na nova string.

print(frase_nova) #Imprime a frase sem caracteres duplicados.