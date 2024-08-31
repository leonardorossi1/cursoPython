texto = "Curso de Python"

setima_posicao_texto = texto[6:]
print(f"setima_posicao_texto = texto")

texto_curso = texto[:5]
print(texto_curso)

texto_python = texto[9:]
print[texto_python]

#Contar o número de caracteres dentro do texto
qtd_char = len(texto)
print(f"Na frase temos {qtd_char} caracteres")

#Contar um número específico de caracteres dentro do texto
letra = "o"
qtd_letras_o = texto.count("o")
print(f"Na frase temos {qtd_letras_o} letras {letra}")

#Identifica onde inicia uma palavra
palavra = "python"
posicao_palavra = texto.find(palavra)
print(f"A palavra {palavra} inicia na posição {posicao_palavra}")

#Identificar se existe palavra no texto
verifica_palavra = palavra in texto
print(f"A palavra {palavra} esta no texto ? {verifica_palavra}")

