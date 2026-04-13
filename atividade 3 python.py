nome = (input("Digite seu nome: "))
sobrenome = (input("Digite seu sobrenome: "))
nome_completo = nome + " " + sobrenome
print(f"Nome digitado: {nome_completo}")
print(f"Quantidade de caracteres: {len(nome_completo)}")
print(f"Primeira letra: {nome_completo[0]}")
print(f"Ultima letra: {nome_completo[-1]}")
print(f"Nome completo em maiúsculas: {nome_completo.upper()}")
