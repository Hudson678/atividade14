# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
# Média ≥ 7: Aprovado
# 5 ≤ Média < 7: Recuperação
# Média < 5: Reprovado
nota1 = float(input("primeira nota do aluno: "))
nota2 = float(input("segunda nota do aluno: "))
nota3 = float(input("terceira nota do aluno: "))

media = nota1 + nota2 + nota3/3
if media >= 7:
	print("aprovado")
else:
		if media > 5 and media < 7:
			print ("recuperação")
if media < 5:
	print ("reprovado")

