lista = [1, 2, 3, 4, 5, 9, 89]
print(f"la longitud de la lista es: {len(lista)}")

suma = 0
for i in lista :
    suma += i

print(f"\nla suma de los valores de la lista es : {suma}")    

multiplicacion = 1

for i in lista :
    multiplicacion *= i

print(f"\nmultiplicacion elementos lista :{multiplicacion}")    


lista.append(4)
print(f"\nla longitud actualizada es :{len(lista)}")