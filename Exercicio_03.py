qtd = int(input("Informe a quantidade de alunos presente em sala: "))
alunos = [" "] * qtd
proc = ""

for i in range(qtd):
    alunos[i] = input(f"Informe o nome do aluno {i}: ")

proc = input("Digite o nome do aluno para descobrir sua posição: ")
for t in range(qtd):
    if proc == alunos[t]:
        print(f"O {alunos[t]} se encontra na posição {t}.")
        break
else:
    #if proc != alunos[t]:
        print("Aluno não encontrado em nossa Bases de Dados.")