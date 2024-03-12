"""
Ejercicios basicos para practicar Python.
"""

"""
1. Definir una funcion max() que tome como argumento dos numeros y devuelva el mayor de ellos. (Es cierto
que python tiene una funcion max() incorporada, pero hacerla nosotros mismos es un buen ejercicio).
"""

def num_max(a, b):
    if a > b:
        return a 
    else:
        return b 

print(num_max(2,5))     # max 5
print(num_max(10,3))    # max 10   
print(num_max(-1,-4))   # max -1
print("-------------------------")

"""
2. Definir una funcion max_de_tres(), que tome tres numeros como argumento y devuelva el mayor de ellos.
"""

def mayor_de_tres(a, b, c):
    if (a > b) & (a > c):
        return a 
    elif (b > a) & (b > c):
        return b
    else:
        return c 

print(mayor_de_tres(1,2,3)) # mayor 3
print(mayor_de_tres(9,8,7)) # mayor 9
print(mayor_de_tres(4,6,5)) # mayor 6
print("-------------------------")

"""
3. Definir una funcion que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene
la funcion len() incorporada, pero escribirla por nosotros mismo resulta un muy buen ejercicio.)
"""
my_lista = ["python", "clase", "a", "carro", "java", "universidad", "ciudad"]

def calc_longitud(my_lista):
    longitud = 0
    for elementos in my_lista:
        longitud += 1
        
    return longitud
        
print(calc_longitud(my_lista))
print("-------------------------")

"""
4. Escribir una funcion que tome un caracter y devuelva True si es una vocal, de los contrario
devuelve False.
"""

vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def is_vocal(vocales, char):
    if char in vocales:
        return True
    else:
        return False

print(is_vocal(vocales, "A"))   # True
print(is_vocal(vocales, "m"))   # False
print(is_vocal(vocales, "2"))   # False
print(is_vocal(vocales, "o"))   # True
print("-------------------------")

"""
5. Escribir una funcion sum() y una funcion multip() que sumen y multipliquen respectivamente todos los
numeros de una lista. Por ejemplo: sum([1,2,3,4]) deberia devolver 10 y multip([1,2,3,4]) deberia devolver 24.
"""

num_lista = [1,2,3,4]

def sum(lista):
    result = 0
    for n in lista:
        result += n
    return result
    
print(sum(num_lista))       # 10

def multip(lista):
    result = 1              # elemento neutro
    for n in lista:
        result *= n
    return result

print(multip(num_lista))    # 24

print("-------------------------")

"""
6. Definir una funcion inversa() que calcule la inversion de una cadena. Por ejemplo,
la cadena "estoy probando" deberia devolver la cadena "odnaborp yotse"
"""

def inversa(cadena):        # algoritmo estandar
    cadena_reverse = str()
    for char in cadena:
        cadena_reverse = char + cadena_reverse
    return cadena_reverse

print(inversa("estoy probando"))

print("-------------------------")

"""
7. Definir una funcion es_palindromo() que reconoce palindromos(es decir, palabras que tienen
el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar) tendria que devolver True.
"""

def es_palindromo(cadena):
    cadena_reverse = str()
    for n in cadena:
        cadena_reverse = n + cadena_reverse
    if cadena == cadena_reverse:
        return True
    else:
        return False

print(es_palindromo("radar"))  # True
print(es_palindromo("house"))  # False
print(es_palindromo("ala"))    # True

print("-------------------------")

"""
8. Definir una funcion superposicion() que tome dos listas y devuelva True si tienen al menos 
1 miembro comun o devuelva False de lo contrario. Escribir la funcion usando el bucle for anidado.
"""

def superposicion(lista1, lista2):
    for elemt1 in lista1:
        for elemt2 in lista2:
            if elemt1 == elemt2:
                return True

    return False
            
    # for elem in lista1:
    #     if elem in lista2:
    #         return True
    # return False
        
print(superposicion([1,2,3],[4,5,6]))   # False
print(superposicion([0,5,10],[1,5,9]))  # True

print("-------------------------")

"""
9. Definir una funcion generar_n_caracteres() que tome un entrero n y devuelva el caracter
multiplicado por n. Por ejemplo: generar_caracteres(5,"x") deberia devolver "xxxxx"
"""

def generar_n_caracteres(n, letra):
    for i in letra:
        return(letra * n)

print(generar_n_caracteres(5, "x"))
print(generar_n_caracteres(3, "abc"))
print(generar_n_caracteres(6, "1"))
print(generar_n_caracteres(0, "A"))     # try case

print("-------------------------")

"""
10. Definir un histograma procedimiento() que tome una lista de numeros enteros e imprima
un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) deberia imprimir lo siguiente:
****
*********
*******
"""

def procedimiento(lista):
    print("\tHistograma:")
    for i in lista:
        histograma = "*" * i
        print(histograma)

procedimiento([4, 9, 7])

print("-------------------------")

