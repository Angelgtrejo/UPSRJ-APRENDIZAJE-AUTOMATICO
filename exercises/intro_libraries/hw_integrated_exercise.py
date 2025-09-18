"""
📊 hw_integrated_exercise.py

Ejercicio integrado que combina Pandas, NumPy y SciPy para analizar datos estudiantiles.
─────────────────────────────────────────────────────────────
🔧 Requisitos:
    - pandas
    - numpy
    - scipy
─────────────────────────────────────────────────────────────
"""
# Librerías necesarias
import pandas as pd
import numpy as np
from scipy import stats, linalg
# Adjust the import path to include the parent directory for py_utils
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

set_logging(log_file="integrated_exercise.log")

# Paso 1: Cargar datos desde CSV
#
# TODO: Cargar el archivo 'estudiantes.csv' en un DataFrame llamado df
#
df = None

# Impresion de la salida df
plog(f"data: {df}", level=ERROR if df is None else DEBUG, eol=True)

# Paso 2: Conversión de datos
#
# TODO: Convertir la columna 'promedio' a un arreglo NumPy
#
promedio = None

# Impresion de la salida promedio
plog(f"promedio: {promedio}", level=ERROR if promedio is None else DEBUG, eol=True)

# Paso 3: Manipulación de datos
# 
# TODO: Normalizar los promedios entre 0 y 1
#
# NOTE: Aplicar la fórmula de normalización: (x - min) / (max - min)
#
normalized = None

# Impresion de la salida avg
plog(f"normalización: {normalized}", level=ERROR if normalized is None else DEBUG, eol=True)

# Paso 4: Calcular estadísticas
#
# TODO: Usar stats.tmean, stats.tstd y stats.mode sobre el arreglo de promedios
#
mean = None
tstd = None
mode = None

# Impresion de la salida mean, tstd, mode
plog(f"media: {mean}, desviación estándar:\n{tstd}, moda:\n{mode}", level=ERROR if None in (mean, tstd, mode) else DEBUG, eol=True)

# Paso 5: Filtrar estudiantes con promedio normalizado > 0.8
#
# TODO: Crear un nuevo DataFrame con estudiantes destacados
#
destacados = None

# Impresion de la salida destacados
plog(f"data: {destacados}", level=ERROR if destacados is None else DEBUG, eol=True)

# Paso 6: Crear matriz de características para álgebra lineal
# 
# TODO: Usar columnas numéricas como 'edad', 'cuatrimestre' y 'promedio_normalizado'
#
mat = None

# Impresion de la salida mat
plog(f"matriz:\n{mat}", level=ERROR if mat is None else DEBUG, eol=True)

# Paso 6.1: Calculo de matrices
#
# TODO: Calcular la matriz de covarianza
#
covarianza = None 

# Impresion de la salida covarianza
plog(f"covarianza:\n{covarianza}", level=ERROR if covarianza is None else DEBUG, eol=True)

# Paso 6.2: Calculo de matrices
#
# TODO: Calcular la inversa de la matriz
#
inversa = None 

# Impresion de la salida inversa
plog(f"inversa:\n{inversa}", level=ERROR if inversa is None else DEBUG, eol=True)


# 🧠 Preguntas interpretativas (responde en comentarios):
# - ¿Qué representa la matriz de covarianza en este contexto?
# - ¿Qué variables parecen estar más relacionadas entre sí?
# - ¿Qué significa que un estudiante tenga promedio normalizado > 0.8?
# - ¿Cómo podrías extender este análisis para incluir variables categóricas como carrera o género?