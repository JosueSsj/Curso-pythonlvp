numero =1
while numero <=10:
    print(numero)
    numero +=2

perros =["boby","rex","max","avellana"]

for perro in perros:
    print(perro)

numero =1
while numero <=10:
    if numero ==5:
        break
    print(numero)
    numero +=1

perros =["boby","rex","max","avellana","max"]

for perro in perros:
    if perro =="max":
        print("ESTE ES EL PERRO QUE BUSCO")
        continue
    print("ESTE NO ES EL PERRO")
