n = int(input("Masukkan bilangan positif: "))

while n <= 0:
    n = int(input("Masukkan bilangan positif: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(2 * (n - i) + 2):
        print(" ", end="")

    for j in range(i, 0, -1):
        print(j, end="")

    print()
