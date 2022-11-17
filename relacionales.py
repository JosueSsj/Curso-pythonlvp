precio =100
IVA = 0.12
impuesto = precio *IVA
print(impuesto)


altura = 100
altura_minima =150
#<=
print(altura <= altura_minima)

def abrir_puerta(altura,edad):
    ALTURA_MINIMA = 150
    EDAD_MINIMA = 15
    if altura <= ALTURA_MINIMA:
        print("NO ALCANZA")
    if edad <=EDAD_MINIMA:
         print("muy joven")

    print("PASE ADELANTE")



abrir_puerta(150,14)