nome = [""] * 5
senha = [""] * 5
posi = [""] * 5
qtd = 5
id = -1     # -1 para resolver o bug da posição do usuario inicial.
flag = 0
flag2 = 0
resp = "n"
login = ""
password = ""

for i in range(qtd):
    nome[i] = input(f"\nInforme o nome do usuário ({i+1}): ")
    senha[i] = input(f"Informe o senha do usuário ({i+1}): ")
    id += 1
    posi[i] = id

print("\nBem vindo a nossa plataforma! \n")
print(nome)

while flag != 1:
    login = input("\nInforme o nome do usuario: ")
    for t in range(qtd):
        if (nome[t] == login):
            print("Usuario encontrado!\n")
            flag = 1
            break
    else:
        print("\nUsuario não encontrado, tente novamente!")

while flag2 != 1:
    password = input("\nInforme a senha do usuario: ")
    for e in range(qtd):
        if (senha[e] == password):
            print("Login efetuado com sucesso !!!")
            flag2 = 1
            break
    else:
        print("\nSenha incorreta, tente novamente...")