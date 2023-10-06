nome = [""] * 5
senha = [""] * 5
posi = [""] * 5
id = -1
resp = "n"
login = ""
password = ""
for i in range(5):
    nome[i] = input(f"\nInforme o nome do usuário ({i+1}): ")
    senha[i] = input(f"Informe o senha do usuário ({i+1}): ")
    id += 1
    posi[i] = id

print("\nBem vindo a nossa plataforma\n !")

while resp in "sS":
    login = input("Por favor, informe o login do usuário: ")
    while nome != login:
        print("Senha incorreta, por favor tente novamente...")

    print("\nLogin encontrado!\n")
    password = input("Por favor, informe a senha do usuário: ")
    while senha != password:
        print("Senha incorreta, por favor tente novamente...")

print("Login efetuado com sucesso !!!")

resp = input("Deseja sair do nosso sistema ? (s/n):")