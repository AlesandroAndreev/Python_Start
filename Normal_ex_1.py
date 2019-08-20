numeric = int(input("Введите число: "))
max = numeric%10
while (numeric // 10 != 0):
    if max < numeric%10:
        max = numeric%10
    numeric = numeric//10
if max < numeric%10:
    max = numeric%10
print (max)
