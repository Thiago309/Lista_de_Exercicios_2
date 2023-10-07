N = int(input("Digite o tamanho dos vetores (N): "))

A = [""] * N
B = [""] * N
Soma = [""] * N
r = [""] * N

for i in range(N):
    A[i] = float(input(f"Digite o {i+1}º elemento do vetor A: "))

for e in range(N):
    B[e] = float(input(f"Digite o {i+1}º elemento do vetor B: "))

for t in range(N):
    r[t] = A[t] + B[t]

print(f"A soma dos vetores são: {r}")
