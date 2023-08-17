"""
Reverta a ordem das palavras nas frases, mantendo a ordem das palavras. Exemplo:
input = "Hello, World! OpenAI is amazing."
output = "amazing. is OpenAI World! Hello,"
"""

frase = input("Digite a frase: ").split() #Recebe a frase e separa cada palavra em uma lista.

frase.reverse() #Reverte a ordem da lista.
frase_nova = ' '.join(frase) #Transforma a lista em uma string novamente.

print(frase_nova) #Imprime a string.