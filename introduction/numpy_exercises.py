"""
📊 numpy_exercises.py

Ejercicios prácticos para manipular arreglos y operaciones numéricas usando NumPy.
─────────────────────────────────────────────────────────────
🔧 Requisitos:
    - numpy
─────────────────────────────────────────────────────────────
"""

import numpy as np
import logging
import os

def setup_logger(index, todo_text):
    log_path = f"test/numpy_exercise_{index:02}.log"
    logger = logging.getLogger(f"numpy_{index}")
    logger.handlers.clear()
    handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.info(f"Ejercicio {index:02}")
    logger.info("--------------------------------------------------")
    logger.info(f"TODO: {todo_text}")
    logger.info("")  # Espacio para que el alumno agregue su resultado debajo
    return logger

# 🧪 Ejercicio 1: Crear un arreglo de 10 ceros
log1 = setup_logger(1, "Usar np.zeros para crear un arreglo de 10 elementos con valor 0")

# 🧪 Ejercicio 2: Crear un arreglo de números del 10 al 49
log2 = setup_logger(2, "Usar np.arange para generar los números del 10 al 49")

# 🧪 Ejercicio 3: Invertir el arreglo anterior
log3 = setup_logger(3, "Usar slicing para invertir el orden del arreglo")

# 🧪 Ejercicio 4: Crear una matriz 3x3 con valores del 0 al 8
log4 = setup_logger(4, "Usar np.arange y .reshape para crear una matriz 3x3")

# 🧪 Ejercicio 5: Encontrar índices de elementos mayores a 5
log5 = setup_logger(5, "Usar np.where para encontrar posiciones donde el valor > 5")

# 🧪 Ejercicio 6: Calcular la media, mediana y desviación estándar
log6 = setup_logger(6, "Usar np.mean, np.median y np.std sobre un arreglo de ejemplo")
# NOTE: Primero debes cambiar el arreglo de ejemplo a un arreglo NumPy
arr6 = [1, 2, 3, 4, 5, 6]
log6.info(f"Media: {0}")
log6.info(f"Mediana: {0}")
log6.info(f"Desviación estándar: {0}")

# 🧪 Ejercicio 7: Crear una matriz identidad de tamaño 4x4
log7 = setup_logger(7, "Usar np.eye para generar la matriz identidad")

# 🧪 Ejercicio 8: Multiplicar dos matrices compatibles
log8 = setup_logger(8, "Crear dos matrices 2x2 y llenarla con numeros sucesivos; usar np.dot o el operador @ para multiplicarlas")

# 🧪 Ejercicio 9: Normalizar un arreglo (valores entre 0 y 1)
log9 = setup_logger(9, "Usar fórmula de normalización: (x - min) / (max - min)")
# NOTE: Primero debes cambiar el arreglo de ejemplo a un arreglo NumPy
arr9 = [10, 20, 30, 40, 50]

# 🧪 Ejercicio 10: Crear un arreglo aleatorio de 100 elementos y contar cuántos están entre 0.3 y 0.7
log10 = setup_logger(10, "Generar un arreglo 1x100 de numeros aleatorios con una semilla de 0. Contar cuántos valores están entre 0.3 y 0.7 usando np.logical_and")

# 🧠 Preguntas interpretativas (responde en comentarios):
# - ¿Qué diferencia hay entre np.array y np.arange?
# - ¿Por qué es útil la matriz identidad en álgebra lineal?
# - ¿Qué significa normalizar un arreglo y cuándo se usa?