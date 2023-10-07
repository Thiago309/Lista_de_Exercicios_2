nome = [""] * 5

for i in range(5):
    nome[i] = input(f"Informe o {i + 1}º nome que deseja armazenar: ")

print(nome)
for t in range(4, -1, -1):
    print(nome[t])