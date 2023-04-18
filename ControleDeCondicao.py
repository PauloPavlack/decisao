import random

nota1 = random.randint(0, 10)
nota2 = random.randint(0, 10)
nota3 = random.randint(0, 10)
nota4 = random.randint(0, 10)

media = (nota1 + nota2 + nota3 + nota4) // 4

print(f"Notas: {nota1}, {nota2}, {nota3}, {nota4}")
print(f"Média: {media}")

if media >= 7:
    print("Aluno Aprovado")
else:
    print("Aluno Reprovad")
