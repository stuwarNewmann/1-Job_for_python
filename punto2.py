notadesarrollo=float(input(" ingrese la nota de desarrolo de software"))
notamatematicas=float(input("ingrese la nota de matematicA"))
notalogica=float(input("ingrese la nota de logica "))
promedio= (notadesarrollo + notamatematicas + notalogica)/3
if promedio < 3.0:
    print("ud perdio el semestre")
else:
    print("ud gano el semestre")