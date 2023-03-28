numero = int(input("Introduce el numero entero: "))

if numero % 2 != 0:
    numer_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            numer_primo = False
            break

    if numer_primo:
        print("El numero", numero, "Es impar y primo.")
    else:
        print("El numero", numero, "Es impar mas no es primo.")
else:
    print("El numero", numero, "Es impar.")