a = input("Введите число a:")
b = input("Введите число b:")

a=(a,)
b=(b,)
a,b = b,a
a=int(a[0])
b=int(b[0])

print("a = ", a, "b = ", b)
