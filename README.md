# Desafio de Código PWC
Manipulação de Strings. Solucionado em Python.

# Exercício 1
## Código que recebe uma frase e reverte a ordem das palavras nas frases, mantendo a ordem das palavras
### Exemplo:
Input = "Hello, World! OpenAI is amazing."

Output = "amazing. is OpenAI World! Hello,"

## Testes realizados e seus resultados, além do exemplo fornecido
Input = "Augusta Ada Byron Kin, atualmente conhecida como Ada Lovelace."

Output = "Lovelace. Ada como conhecida atualmente Kin, Byron Ada Augusta"

Input = "Shall I compare thee to a summer’s day?"

Output = "day? summer’s a to thee compare I Shall"

Input = "No meio do caminho tinha uma pedra"

Output = "pedra uma tinha caminho do meio No"

# Exercício 2
## Código que recebe uma frase e remove todos os caracteres duplicados da string
### Exemplo:
Input = "Hello, World!"

Output = "Helo, Wrd!"
## Testes realizados e seus resultados, além do exemplo fornecido
Input = "América Latina."

Output = "América Ltn."

Input = "Oi, meu nome é Fernanda."

Output = "Oi, meunoéFrad." 

É possível perceber que como o programa foi feito para retirar todos os caracteres duplicados, também retira os espaços entre as palavras. Para que isso não aconteça, seria possível inserir na condicional IF da décima primeira linha do código: "or i == ' '".
Dessa forma, o resultado seria:

Input = "Oi, meu nome é Fernanda."

Output = "Oi, meu no é Frad."

# Exercício 3
## Código que recebe uma palavra e encontra a substring palíndroma mais longa na string.
### Exemplo:
Input = "babad"

Output = "bab"

### Testes realizados e seus resultados, além do exemplo fornecido
Input = "mussum"

Output = "mussum"

Input = "umovo"

Output = "ovo"

Input = "arevivero"

Output = "reviver"

# Exercício 4
## Código que coloca em maiúscula a primeira letra de cada frase na string.
### Exemplo:
Input = "hello. how are you? i'm fine, thank you."

Output = "Hello. How are you? I'm fine, thank you."

## Testes realizados e seus resultados, além do exemplo fornecido
Input = "a lua é um satélite natural. plutão não é mais planeta! o sol é uma estrela."

Output = "A lua é um satélite natural. Plutão não é mais planeta! O sol é uma estrela."

Input = "eu? você! eu não. você sim!"

Output = "Eu? Você! Eu não. Você sim!"

# Exercício 5
## Código que verifica se a string é um anagrama de um palíndromo.
### Exemplo:
Input = "racecar"

Output = "true"

## Testes realizados e seus resultados, além do exemplo fornecido
Input = "arara"

Output = "true"

Input = "mmusus"

Output = "true"

Input = "computador"

Output = "false"
