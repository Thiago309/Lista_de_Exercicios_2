qtd = 30
n = [""] * qtd
cont = 0

for i in range(qtd):
    n[i] = float(input(f"Digite o {i+1}º número: "))

n_busca = float(input("Digite o número que deseja buscar: "))

for e in range(qtd):
    if (n[e] == n_busca):
        cont += 1

print(f"O número {n_busca} aparece {cont} vezes no vetor.")
