"""
Coloque em maiúscula a primeira letra de cada frase na string. Exemplo:
input = "hello. how are you? i'm fine, thank you."
output = "Hello. How are you? I'm fine, thank you."
"""

frase = input("Digite a frase: ").split() #Recebe a frase e separa cada palavra em uma lista.

tam_frase = len(frase) #Mede o comprimento da lista.
frase_nova = "" #Inicializa uma string vazia.

for i in range(tam_frase): #Percorre a lista de acordo com seu tamanho.
  if i == 0 or frase[i-1].endswith('.') or frase[i-1].endswith('!') or frase[i-1].endswith('?'): #Verifica se a primeira letra da palavra precisa ser maiúscula.
    frase[i] = frase[i].capitalize() #Deixa a letra maiúscula.

frase_nova = ' '.join(frase) #Transforma a lista em uma string.

print(frase_nova) #Imprime a string.