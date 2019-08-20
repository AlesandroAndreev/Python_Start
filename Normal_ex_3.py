Koof_a = int(input("Введите коофициента a: "))
Koof_b = int(input("Введите коофициента b: "))
Koof_c = int(input("Введите коофициента c: "))

d = (Koof_b)^2-4*Koof_a*Koof_c

print(d)

if d > 0:
    x1 = ((-Koof_b)+ math.sqrt(d))/2*Koof_a
    x2 = ((-Koof_b)- math.sqrt(d))/2*Koof_a
    print("x1:",x1)
    print("x2:",x2)
elif d == 0:
         x = -Koof_b/2*Koof_a
         print ( "x1 = x2 =",x)
else:
             x1 = ((-Koof_b)+ (d)**0.5)/2*Koof_a
             x2 = ((-Koof_b)- (d)**0.5)/2*Koof_a
             print("x1:",x1)
             print("x2:",x2)
             
               
