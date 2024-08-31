#Trocando uma palavra dentro de um texto
texto = 'Pedro Miho'
troca_palavra = texto.replace('Miho' ,'Silva')
print(troca_palavra)

#Deixando todos os caracteres em maiúsculos
texto = 'PeDRoMiho@outLOOk.com'
print(texto.upper())


#Deixando todos os caracteres em minúsculos
texto_minusculo = texto.lower()
print(texto_minusculo)

#Deixando a primeira letra de cada palavra em Maiúsculo
texto = 'Meu primeiro curso no senai'
texto_title = texto.title()
print(texto_title)

#Deixando a primeira letra do texto em Maiúsculo
texto_capitalize = texto.capitalize()
print(texto_capitalize)

#Elimina espaços inúteis
texto = '     SENAI       '
print(f'A palavra {texto} tem {len(texto)} caracteres')

texto_strip = texto.strip()
print(f'A palavra {texto_strip} tem {len(texto_strip)} caracteres')