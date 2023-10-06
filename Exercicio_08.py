nome = [""] * 5
senha = [""] * 5
posi = [""] * 5
id = -1
for i in range(5):
    nome[i] = input(f"Informe o nome do usuário ({i+1}): ")
    senha[i] = input(f"Informe o senha do usuário ({i+1}): ")
    id += 1
    posi[i] = id

for t in range(5):
    print(f"O nome do usuário é: {nome[t]}, sua senha é: {senha[t]} e sua posição é: {posi[t]}.")