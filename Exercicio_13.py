# Criar um vetor para armazenar os 30 números
qtd = 3
n = [0] * qtd
# Ler os 30 números e armazenar no vetor
for i in range(qtd):
    n[i] = int(input(f"Digite o {i+1}º número: "))


# (I) Encontrar e exibir todos os números pares
print("")
for e in range(qtd):
    if n[e] % 2 == 0:
        print(f"Números pares no vetor: {n[e]}", end=' ')

# (II) Encontrar o menor e o maior valor no vetor
menor = n[0]
maior = n[0]
for t in range(qtd):
    if n[t] < menor:
        menor = n[t]

    if n[t] > maior:
        maior = n[t]

print(f"\nMenor valor no vetor: {menor}")
print(f"Maior valor no vetor: {maior}\n")

# (III) Calcular a média dos valores no vetor
soma = 0
for f in range(qtd):
    soma += n[f]

media = soma / qtd

# (IV) Contar quantos valores são maiores que a média
maiores_medias = 0

for z in range(qtd):
    if n[z] > media:
        maiores_medias += 1

print(f"Quantidade de valores maiores que a média ({media:.2f}): {maiores_medias}")