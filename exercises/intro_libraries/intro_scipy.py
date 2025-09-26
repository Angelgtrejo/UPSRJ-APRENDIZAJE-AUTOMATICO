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
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
linear_system = linalg.solve(A, b)

# Impresion de la salida linear_system
plog(f"linear_system: {linear_system}", level=ERROR if linear_system is None else DEBUG, eol=True)

# Ejercicio 2: Calcular determinante y matriz inversa
#
# TODO: Obten el determinante y la inversa de la matriz A del ejercicio anterior
#
determinant = linalg.det(A)
inverse = linalg.inv(A)

# Impresion de la salida determinant e inverse
plog(f"determinant: {determinant}, inverse:\n{inverse}", level=ERROR if determinant is None or inverse is None else DEBUG, eol=True)

# Ejercicio 3: Estadísticas básicas sobre una muestra
# 
# TODO: Obtén la media, desviación estándar y moda sobre un arreglo de datos [1, 2, 2, 3, 4, 4, 4, 5]
# 
data = np.array([1, 2, 2, 3, 4, 4, 4, 5])
mean = np.mean(data)  # También se puede usar stats.tmean(data)
tstd = np.std(data, ddof=1)  # ddof=1 para desviación estándar de muestra
mode = stats.mode(data, keepdims=True)

# Impresion de la salida mean, tstd, mode
plog(f"media: {mean}, desviación estándar:\n{tstd}, moda:\n{mode}", level=ERROR if mean is None or tstd is None or mode is None else DEBUG, eol=True)

# Ejercicio 4: Ajuste de una función cuadrática
# 
# TODO: Encuentra el mínimo de una función f(x) = (x - 3)^2 + 2
#
def func_cuadratica(x):
    return (x - 3)**2 + 2

# Usar minimize para encontrar el mínimo, empezando desde x0=0
resultado = optimize.minimize(func_cuadratica, x0=0)
f_min = resultado.x[0]  # Obtener el valor de x donde está el mínimo

# Impresion de la salida f_min
plog(f"Mínimo encontrado en x = {f_min}", level=ERROR if f_min is None else DEBUG, eol=True)

# Ejercicio 5: Transformada de Fourier de una señal
#
# TODO: Obten el espectro de una señal compuesta. Señal: sin(2π5t) + sin(2π20t)
#
t = np.linspace(0, 1, 500) # tiempo
# Crear la señal compuesta
señal = np.sin(2*np.pi*5*t) + np.sin(2*np.pi*20*t)
# Calcular la transformada de Fourier
t_fourier = np.fft.fft(señal)
# Solo tomar la magnitud para simplificar
t_fourier = np.abs(t_fourier)

# Impresion de la salida t_fourier
plog(f"F.T. = {t_fourier}", level=ERROR if t_fourier is None else DEBUG, eol=True)

# Ejercicio 6: Filtrado de señal con Butterworth
#
# TODO: Usa signal.butter y signal.filtfilt para aplicar un filtro pasa-bajas. Nyquist = 0.5 * fs, low = 10 / Nyquist. Ruido: sin(2π5t) + 0.5sin(2π50t)")
#
fs = 100.0  # frecuencia de muestreo
# Crear señal con ruido
t_filter = np.linspace(0, 1, int(fs))
señal_ruido = np.sin(2*np.pi*5*t_filter) + 0.5*np.sin(2*np.pi*50*t_filter)

# Parámetros del filtro
nyquist = 0.5 * fs
low = 10 / nyquist

# Diseñar filtro Butterworth pasa-bajas de orden 5
b, a = signal.butter(5, low, btype='low')
# Aplicar el filtro
lp_filter = signal.filtfilt(b, a, señal_ruido)

# Impresion de la salida lp_filter
plog(f"Filtro Pasa-Bajas = {lp_filter}", level=ERROR if lp_filter is None else DEBUG, eol=True)

# 🧠 Preguntas interpretativas (responde en comentarios):
# - ¿Qué representa la solución de Ax = b en términos geométricos?
# Respuesta: Geométricamente, resolver Ax = b significa encontrar el punto x donde 
# la transformación lineal A mapea al vector b. Es la intersección de hiperplanos
# en el espacio n-dimensional.

# - ¿Por qué es útil conocer la moda y la desviación estándar de una muestra?
# Respuesta: La moda indica el valor más frecuente (tendencia central), mientras que
# la desviación estándar mide la dispersión de los datos. Juntas nos dan información
# sobre la distribución y variabilidad de nuestros datos.

# - ¿Qué información nos da la transformada de Fourier de una señal?
# Respuesta: La transformada de Fourier descompone una señal temporal en sus 
# componentes de frecuencia, permitiendo identificar qué frecuencias están presentes
# y con qué amplitud, revelando patrones periódicos ocultos.

# - ¿Qué efecto tiene un filtro Butterworth sobre una señal compuesta?
# Respuesta: Un filtro Butterworth pasa-bajas elimina las frecuencias altas (ruido)
# mientras preserva las frecuencias bajas de interés, suavizando la señal y 
# reduciendo el ruido de alta frecuencia.