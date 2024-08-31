nome_completo = 'Leonardo Rossi Barbosa'

primeiro_nome = nome_completo[:8]
print(f"Meu primeiro nome é {primeiro_nome}")

ultimo_nome = nome_completo [-7:]
print(ultimo_nome)

texto = "Leonardo Rossi Barbosa"

qtd_char = len(primeiro_nome)
print(f"Na frase temos {qtd_char} caracteres")

letra = "o"
qtd_letras_o = texto.count("o")
print(f"Na frase temos {qtd_letras_o} letras {letra}")

qtd_char = len(texto)
print(f"Na frase temos {qtd_char} caracteres")

palavra = "Barbosa"
posicao_palavra = texto.find(palavra)
print(f"A palavra {palavra} inicia na posição {posicao_palavra}")

verifica_palavra = palavra in texto
print(f"A palavra {palavra} esta no texto ? {verifica_palavra}")