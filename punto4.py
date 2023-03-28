print("Aqui podra combinar colores primarios.")
print("Selecciona dos colores de la siguiente tabla: ")
print("1.Amarillo")
print("2.Azul")
print("3.Rojo")
print("4.Blanco")
print("5.Negro")

col1 = input("Escribe el numero del primer color seleccionado: ")
col2 = input("Escribe el numero del segundo color seleccionado: ")

if col1 == "1" and col2 == "2" or col1 == "2" and col2 == "1":
    print("La combinacion lograda es: Verde")
elif col1 == "1" and col2 == "3" or col1 == "3" and col2 == "1":
    print("La combinacion lograda es: Naranja")
elif col1 == "2" and col2 == "3" or col1 == "3" and col2 == "2":
    print("La combinacion lograda es: Morado")
elif col1 == "1" and col2 == "4" or col1 == "4" and col2 == "1":
    print("La combinacion lograda es: Amarillo")
elif col1 == "1" and col2 == "5" or col1 == "5" and col2 == "1":
    print("La combinacion lograda es: Amarillo")
elif col1 == "2" and col2 == "4" or col1 == "4" and col2 == "2":
    print("La combinacion lograda es: Azul")
elif col1 == "2" and col2 == "5" or col1 == "5" and col2 == "2":
    print("La combinacion lograda es: Negro")
elif col1 == "3" and col2 == "4" or col1 == "4" and col2 == "3":
    print("La combinacion lograda es: Rojo")
elif col1 == "3" and col2 == "5" or col1 == "5" and col2 == "3":
    print("La combinacion lograda es: Negro")
elif col1 == "4" and col2 == "5" or col1 == "5" and col2 == "4":
    print("La combinacion lograda es: Negro")
else:
    print("Selecciones Invalidas.")