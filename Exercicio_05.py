A = [""] * 10
M = [""] * 10
x = 0

for i in range(10):
    A[i] = int(input(f"Digite o valor ({i + 1}) que você deseja armazenar: "))

print(f"Os valores armazenados foram: {A}")

x = int(input("Informe o valor da multiplicação: "))
for t in range(10):
    M[t] = A[t] * x

print(M)