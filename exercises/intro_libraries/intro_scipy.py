"""
intro_scipy.py

Ejercicios prácticos para resolver problemas numéricos y estadísticos usando SciPy.
─────────────────────────────────────────────────────────────
Requisitos:
    - numpy
    - scipy
─────────────────────────────────────────────────────────────
"""
# Librerías necesarias
import numpy as np
from scipy import linalg, stats, optimize, signal
# Adjust the import path to include the parent directory for py_utils
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

set_logging(log_file="intro_scipy.log")

################################################################################
# NOTE: Revisa la API de SciPy en https://docs.scipy.org/doc//scipy/index.html #
################################################################################

# Ejercicio 1: Resolver un sistema lineal Ax = b
# 
# TODO: Define A y b como arreglos NumPy y encuentra x. Los valores son: A = [[3, 1], [1, 2]], b = [9, 8]
#
linear_system = None

# Impresion de la salida linear_system
plog(f"linear_system: {linear_system}", level=ERROR if linear_system is None else DEBUG, eol=True)

# Ejercicio 2: Calcular determinante y matriz inversa
#
# TODO: Obten el determinante y la inversa de la matriz A del ejercicio anterior
#
determinant = None
inverse = None

# Impresion de la salida determinant e inverse
plog(f"determinant: {determinant}, inverse:\n{inverse}", level=ERROR if None in (determinant, inverse) else DEBUG, eol=True)

# Ejercicio 3: Estadísticas básicas sobre una muestra
# 
# TODO: Obtén la media, desviación estándar y moda sobre un arreglo de datos [1, 2, 2, 3, 4, 4, 4, 5]
# 
data = None
mean = None
tstd = None
mode = None

# Impresion de la salida mean, tstd, mode
plog(f"media: {mean}, desviación estándar:\n{tstd}, moda:\n{mode}", level=ERROR if None in (mean, tstd, mode) else DEBUG, eol=True)

# Ejercicio 4: Ajuste de una función cuadrática
# 
# TODO: Encuentra el mínimo de una función f(x) = (x - 3)^2 + 2
#
f_min = None

# Impresion de la salida f_min
plog(f"Mínimo encontrado en x = {f_min}", level=ERROR if f_min is None else DEBUG, eol=True)

# Ejercicio 5: Transformada de Fourier de una señal
#
# TODO: Obten el espectro de una señal compuesta. Señal: sin(2π5t) + sin(2π20t)
#
t = np.linspace(0, 1, 500) # tiempo
t_fourier = None

# Impresion de la salida t_fourier
plog(f"F.T. = {t_fourier}", level=ERROR if t_fourier is None else DEBUG, eol=True)

# Ejercicio 6: Filtrado de señal con Butterworth
#
# TODO: Usa signal.butter y signal.filtfilt para aplicar un filtro pasa-bajas. Nyquist = 0.5 * fs, low = 10 / Nyquist. Ruido: sin(2π5t) + 0.5sin(2π50t)")
#
fs = 100.0  # frecuencia de muestreo
lp_filter = None

# Impresion de la salida lp_filter
plog(f"Filtro Pasa-Bajas = {lp_filter}", level=ERROR if lp_filter is None else DEBUG, eol=True)

# 🧠 Preguntas interpretativas (responde en comentarios):
# - ¿Qué representa la solución de Ax = b en términos geométricos?
# - ¿Por qué es útil conocer la moda y la desviación estándar de una muestra?
# - ¿Qué información nos da la transformada de Fourier de una señal?
# - ¿Qué efecto tiene un filtro Butterworth sobre una señal compuesta?