"""
📊 scipy_exercises.py

Ejercicios prácticos para resolver problemas numéricos y estadísticos usando SciPy.
─────────────────────────────────────────────────────────────
🔧 Requisitos:
    - numpy
    - scipy
─────────────────────────────────────────────────────────────
"""

import numpy as np
import logging
import os
from scipy import linalg, stats, optimize, signal

def setup_logger(index, todo_text):
    log_path = f"test/scipy_exercise_{index:02}.log"
    logger = logging.getLogger(f"scipy_{index}")
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

# 🧪 Ejercicio 1: Resolver un sistema lineal Ax = b
log1 = setup_logger(1, "Define A y b como arreglos NumPy y usa linalg.solve para encontrar x. Los valores son: A = [[3, 1], [1, 2]], b = [9, 8]")

# 🧪 Ejercicio 2: Calcular determinante y matriz inversa
log2 = setup_logger(2, "Usa linalg.det y linalg.inv sobre la matriz A")
log2.info(f"Determinante: {0}")
log2.info(f"Inversa:\n{0}")

# 🧪 Ejercicio 3: Estadísticas básicas sobre una muestra
log3 = setup_logger(3, "Usa stats.tmean, stats.tstd y stats.mode sobre un arreglo de datos")
# NOTE: Primero debes cambiar el arreglo de ejemplo a un arreglo NumPy
data = [1, 2, 2, 3, 4, 4, 4, 5]
log3.info(f"Media truncada: {0}")
log3.info(f"Desviación estándar truncada: {0}")
log3.info(f"Moda: {0}")

# 🧪 Ejercicio 4: Ajuste de una función cuadrática
log4 = setup_logger(4, "Usa optimize.minimize para encontrar el mínimo de una función f(x) = (x - 3)^2 + 2")
log4.info(f"Mínimo encontrado en x = {0}")

# 🧪 Ejercicio 5: Transformada de Fourier de una señal
log5 = setup_logger(5, "Usa signal.fft para obtener el espectro de una señal compuesta. Señal: sin(2π5t) + sin(2π20t)")
t = np.linspace(0, 1, 500) # tiempo

# 🧪 Ejercicio 6: Filtrado de señal con Butterworth
log6 = setup_logger(6, "Usa signal.butter y signal.filtfilt para aplicar un filtro pasa-bajas. Nyquist = 0.5 * fs, low = 10 / Nyquist. Ruido: sin(2π5t) + 0.5sin(2π50t)")
fs = 100.0  # frecuencia de muestreo

# 🧠 Preguntas interpretativas (responde en comentarios):
# - ¿Qué representa la solución de Ax = b en términos geométricos?
# - ¿Por qué es útil conocer la moda y la desviación estándar de una muestra?
# - ¿Qué información nos da la transformada de Fourier de una señal?
# - ¿Qué efecto tiene un filtro Butterworth sobre una señal compuesta?