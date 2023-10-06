n = [""] * 5

for i in range(5):
    n[i] = int(input(f"Digite o valor {i+1} que deseja armazenar: "))

print(n)
for t in range(4, -1, -1):
    print(n[t])