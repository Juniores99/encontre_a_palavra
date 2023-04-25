
import random
palavras = []
with open('words.txt', 'r') as f:
      palavras = f.readlines()
      indice_palavra = random.randint(0, len(palavras) - 1)
      palavra_sorteada = palavras[indice_palavra].replace('\n', '')
      palavra = ['_'] * len(palavra_sorteada)
      while True:
            letra = input('Digite uma letra ').upper()
            for i in range(len(palavra_sorteada)):
                  if letra == palavra_sorteada[i]:
                        palavra[i] = letra
            if ''.join(palavra) == palavra_sorteada:
                  print('Voce acertou!!')
                  print('A palavra eh {0}'.format(palavra_sorteada))
            else:
                  print(' '.join(palavra))
