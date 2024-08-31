#Desafio 1 
nome = input('digite seu nome: ')
print(nome.upper())
print(nome.lower())

nome_strip = nome.strip()
print(f'A palavra {nome_strip} tem {len(nome_strip)} caracteres')

troca_palavra = nome.replace(' ' , '')
print(troca_palavra)

#Desafio 2
palavra = 'Santo'
posicao_palavra = palavra.find(palavra)
print(f"A palavra {palavra} inicia na posição {posicao_palavra}")
cidade = input('digite sua cidade: ')

#Desafio 3
nome = input('digite seu nome: ')
palavra = 'Silva'
verifica_palavra = palavra in nome
print(f"A palavra {palavra} esta no texto ? {verifica_palavra}")

#Desafio 4
frase = input('digite uma frase : ')
letra = "a"
qtd_letras_a = frase.count("a")
