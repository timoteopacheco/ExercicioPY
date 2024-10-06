# Solicitar o nome do aluno
nome_aluno = input("Digite o nome do aluno: ")

# Criar uma lista vazia para armazenar as notas
notas = []

# Solicitar as três notas ao usuário e adicioná-las à lista
nota1 = float(input("Digite a primeira nota: "))
notas.append(nota1)

nota2 = float(input("Digite a segunda nota: "))
notas.append(nota2)

nota3 = float(input("Digite a terceira nota: "))
notas.append(nota3)

# Calcular a média das notas
media = sum(notas) / len(notas)

# Exibir a média calculada com duas casas decimais
print(f"A média de {nome_aluno} é {media:.2f}")

# Verificar se o aluno foi aprovado ou reprovado
if media >= 7.0:
    print(f"{nome_aluno} foi aprovado.")
else:
    print(f"{nome_aluno} foi reprovado.")
