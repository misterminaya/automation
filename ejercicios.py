#Ingresar el nombre y apellido de un alumno y sus notas de matemática, literatura y física.
#Se pide imprimir el nombre, el apellido y el promedio.
#Si el promedio es mayor a 6 entonces debe aparecer un cartel que diga "Aprobado". Caso contrario, si tiene menos
# de 4 puntos imprimir "Insuficiente" y si tiene entre 4 y 5.99999 imprimir "A recuperatorio".
#En caso de tener 9 puntos o más, imprimir (aparte del aprobado) "Alumno destacado".

name = input("¿cual es tu nombre?")
lastName = input("¿cual es tu apellido?")

Notasmatematica = float(input("Ingrese su nota del curso de Matemática"))
Notasliteratura = float(input("Ingrese su nota del curso de Literatura"))
Notasfisica = float(input("Ingrese su nota del curso de Fisica"))

promedio = ((Notasmatematica + Notasliteratura + Notasfisica) / 3)

if promedio >= 9:
    print(f"nombre y apellidos : {name} {lastName}")
    print(f"Su promedio es {promedio}, alumno destacado")
elif 9 > promedio >= 6:
    print(f"nombre y apellidos : {name} {lastName}")
    print(f"Su promedio es {promedio}, usted esta aprobado")
elif 6 > promedio <= 4:
    print(f"nombre y apellidos : {name} {lastName}")
    print(f"Su promedio es {promedio}, su nota es insuficiente")
else:
    print(f"nombre y apellidos : {name} {lastName}")
    print(f"Su promedio es {promedio}, tiene que ir al recuperatorio")

#fin



