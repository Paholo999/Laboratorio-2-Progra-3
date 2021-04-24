
n1 = int(input("Ingrese Numero 1: "))
n2 = int(input("Ingrese Numero 2: "))
n3 = int(input("Ingrese Numero 3: "))

if (n1<n2)and(n3>n2):
    print("Es verdadero")
else:
    print("Es falso")

if (n1<n2)or(n2>n3):
    print("Es verdadero")
else:
    print("Es falso")


print(not n1 < n2)




