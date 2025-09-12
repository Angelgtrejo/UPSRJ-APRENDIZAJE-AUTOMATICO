"""
📊 01_intro_numpy.py

Ejercicios prácticos para manipular arreglos y operaciones numéricas usando NumPy.
─────────────────────────────────────────────────────────────
🔧 Requisitos:
    - numpy
─────────────────────────────────────────────────────────────

autor: https://github.com/chucholoport
fecha: 11/09/2025
"""

import numpy as np

# 🧪 Ejercicio 1: Crear un arreglo de 10 ceros
#
# TODO: Crea un arreglo 'arg' de 10 elementos con valor 0. 
#
# NOTE: https://numpy.org/doc/1.21/reference/generated/numpy.zeros.html
#
arg = np.zeros(10)

# 🧪 Ejercicio 2: Crear un arreglo de números del 10 al 49
#
# TODO: Genera los números del 10 al 49 en un arreglo 'arg'. 
#
# NOTE: https://numpy.org/doc/1.21/reference/generated/numpy.arange.html
#
pass 

# 🧪 Ejercicio 3: Invertir el arreglo anterior
#
# TODO: Invierte el orden del arreglo 'arg', guardando el resultado en 'arg'. 
#
# NOTE: https://numpy.org/doc/1.21/user/basics.indexing.html#slicing-and-striding
#
pass 

# 🧪 Ejercicio 4: Crear una matriz 3x3 con valores del 0 al 8
#
# TODO: Crea una matriz 3x3 llamada 'mat' con valores del 0 al 8
#
# NOTE: https://numpy.org/doc/1.21/reference/generated/numpy.arange.html
#       https://numpy.org/doc/1.21/reference/generated/numpy.reshape.html
#
pass 

# 🧪 Ejercicio 5: Encontrar índices de elementos mayores a 5
#
# TODO: Encuentra posiciones donde el valor > 5 en 'mat', guardando los índices en 'indices'
#
# NOTE: https://numpy.org/doc/1.21/reference/generated/numpy.where.html
#
pass

# 🧪 Ejercicio 6: Calcular la media, mediana y desviación estándar
#
# TODO: Calcula la media, mediana y desviaciación estándar sobre el arreglo 'arg', guardando los resultados en 'mean', 'median' y 'std'
#
# NOTE: https://numpy.org/doc/1.21/reference/generated/numpy.mean.html
#       https://numpy.org/doc/1.21/reference/generated/numpy.median.html
#       https://numpy.org/doc/1.21/reference/generated/numpy.std.html
#
pass

# 🧪 Ejercicio 7: Crear una matriz identidad de tamaño 4x4
#
# TODO: Genera la matriz identidad 4x4 llamada 'identity'
#
# NOTE: https://numpy.org/doc/1.21/reference/generated/numpy.eye.html
#
pass 

# 🧪 Ejercicio 8: Multiplicar dos matrices compatibles
#
# TODO: Crea dos matrices 2x2 llamadas 'A' y 'B', llénalas con numeros sucesivos del 1 al 8, 
#       multiplícalas y guarda el resultado en 'product'
#
# NOTE: https://numpy.org/doc/1.21/reference/generated/numpy.dot.html
#       https://numpy.org/doc/stable/reference/generated/numpy.matmul.html
#
pass 

# 🧪 Ejercicio 9: Normalizar un arreglo (valores entre 0 y 1)
#
# TODO: Declara una función 'normalize 'que normalice un arreglo 'arg' usando la fórmula: (x - min) / (max - min), 
#       llamala sobre el arreglo 'arg' y guarda el resultado en 'normalized'
#
# NOTE: https://numpy.org/doc/1.21/reference/generated/numpy.min.html
#       https://numpy.org/doc/1.21/reference/generated/numpy.max.html
#
pass 

# 🧪 Ejercicio 10: Crear un arreglo aleatorio de 100 elementos y contar cuántos están entre 0.3 y 0.7
#
# TODO: Genera un arreglo 1x100 de numeros aleatorios con una semilla de 0. 
#       Cuenta cuántos valores están entre 0.3 y 0.7 usando np.logical_and, guardando el conteo en 'count'
#
# NOTE: https://numpy.org/doc/1.21/reference/random/generated/numpy.random.seed.html
#       https://numpy.org/doc/1.21/reference/generated/numpy.random.rand.html
#       https://numpy.org/doc/1.21/reference/generated/numpy.logical_and.html
#       https://numpy.org/doc/1.21/reference/generated/numpy.sum.html
#       
pass

# 🧠 Preguntas interpretativas (responde en comentarios):
# - ¿Qué diferencia hay entre np.array y np.arange?
# - ¿Por qué es útil la matriz identidad en álgebra lineal?
# - ¿Qué significa normalizar un arreglo y cuándo se usa?