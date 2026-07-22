"""
En Jurassic Park, los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. En este ejercicio, se nos proporciona una lista de números enteros que representan la cantidad de huevos puestos por diferentes dinosaurios en el parque.

Objetivo
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros, es decir, la suma de todos los números pares en la lista.
"""

def count_eggs(numbers): 
    suma_total = 0
    
    for number in numbers:
        if number % 2 == 0:
            suma_total += number
    
    return suma_total        
    
print(count_eggs([3, 4, 7, 5, 8]))