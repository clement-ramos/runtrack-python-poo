def pui(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pui(x, n//2) ** 2
    else:
        return x * pui(x, n-1)


x = int(input("Entrer un nombre: "))
n = int(input("Entrer un entier: "))
print(x, "^", n, "=", pui(x, n))
