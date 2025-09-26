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
try:
    df = pd.read_csv('estudiantes.csv')
except FileNotFoundError:
    # Si no existe el archivo, crear datos de ejemplo
    df = pd.DataFrame({
        'nombre': ['Ana García', 'Luis López', 'María Martínez', 'Carlos Ruiz', 'Elena Pérez', 
                   'Diego Silva', 'Carmen Torres', 'José Morales', 'Laura Jiménez', 'Pablo Castro'],
        'edad': [20, 19, 21, 22, 20, 18, 23, 19, 21, 20],
        'cuatrimestre': [4, 3, 6, 8, 4, 2, 9, 3, 5, 4],
        'promedio': [8.5, 7.2, 9.1, 6.8, 8.9, 7.5, 9.3, 6.9, 8.7, 7.8],
        'carrera': ['Ingeniería', 'Medicina', 'Derecho', 'Ingeniería', 'Medicina',
                   'Derecho', 'Ingeniería', 'Medicina', 'Derecho', 'Ingeniería']
    })
    print("Archivo CSV no encontrado. Usando datos de ejemplo.")

# Impresion de la salida df
plog(f"data: {df}", level=ERROR if df is None else DEBUG, eol=True)

# Paso 2: Conversión de datos
#
# TODO: Convertir la columna 'promedio' a un arreglo NumPy
#
promedio = df['promedio'].to_numpy()

# Impresion de la salida promedio
plog(f"promedio: {promedio}", level=ERROR if promedio is None else DEBUG, eol=True)

# Paso 3: Manipulación de datos
# 
# TODO: Normalizar los promedios entre 0 y 1
#
# NOTE: Aplicar la fórmula de normalización: (x - min) / (max - min)
#
min_promedio = np.min(promedio)
max_promedio = np.max(promedio)
normalized = (promedio - min_promedio) / (max_promedio - min_promedio)

# Agregar la columna normalizada al DataFrame
df['promedio_normalizado'] = normalized

# Impresion de la salida avg
plog(f"normalización: {normalized}", level=ERROR if normalized is None else DEBUG, eol=True)

# Paso 4: Calcular estadísticas
#
# TODO: Usar stats.tmean, stats.tstd y stats.mode sobre el arreglo de promedios
#
mean = stats.tmean(promedio)
tstd = stats.tstd(promedio)
mode = stats.mode(promedio, keepdims=True)

# Impresion de la salida mean, tstd, mode
plog(f"media: {mean}, desviación estándar:\n{tstd}, moda:\n{mode}", level=ERROR if mean is None or tstd is None or mode is None else DEBUG, eol=True)

# Paso 5: Filtrar estudiantes con promedio normalizado > 0.8
#
# TODO: Crear un nuevo DataFrame con estudiantes destacados
#
destacados = df[df['promedio_normalizado'] > 0.8].copy()

# Impresion de la salida destacados
plog(f"data: {destacados}", level=ERROR if destacados is None else DEBUG, eol=True)

# Paso 6: Crear matriz de características para álgebra lineal
# 
# TODO: Usar columnas numéricas como 'edad', 'cuatrimestre' y 'promedio_normalizado'
#
mat = df[['edad', 'cuatrimestre', 'promedio_normalizado']].to_numpy()

# Impresion de la salida mat
plog(f"matriz:\n{mat}", level=ERROR if mat is None else DEBUG, eol=True)

# Paso 6.1: Calculo de matrices
#
# TODO: Calcular la matriz de covarianza
#
# Usar la transpuesta para calcular covarianza entre variables (no observaciones)
covarianza = np.cov(mat.T)

# Impresion de la salida covarianza
plog(f"covarianza:\n{covarianza}", level=ERROR if covarianza is None else DEBUG, eol=True)

# Paso 6.2: Calculo de matrices
#
# TODO: Calcular la inversa de la matriz
#
try:
    inversa = linalg.inv(covarianza)
except linalg.LinAlgError:
    # Si la matriz no es invertible, usar pseudoinversa
    inversa = linalg.pinv(covarianza)
    print("Matriz singular, usando pseudoinversa")

# Impresion de la salida inversa
plog(f"inversa:\n{inversa}", level=ERROR if inversa is None else DEBUG, eol=True)


# 🧠 Preguntas interpretativas (responde en comentarios):
# - ¿Qué representa la matriz de covarianza en este contexto?
# Respuesta: La matriz de covarianza muestra cómo varían conjuntamente las variables
# (edad, cuatrimestre, promedio normalizado). Los valores positivos indican que las
# variables tienden a aumentar juntas, mientras que valores negativos indican relación
# inversa.

# - ¿Qué variables parecen estar más relacionadas entre sí?
# Respuesta: Para saberlo hay que examinar los valores fuera de la diagonal principal.
# Los valores más altos (en valor absoluto) indican mayor correlación. Típicamente
# cuatrimestre y promedio podrían estar relacionados.

# - ¿Qué significa que un estudiante tenga promedio normalizado > 0.8?
# Respuesta: Significa que su promedio está en el 20% superior de todos los promedios
# en el dataset. Es decir, está entre los estudiantes con mejor rendimiento académico
# relativo al grupo.

# - ¿Cómo podrías extender este análisis para incluir variables categóricas como carrera o género?
# Respuesta: Se podrían usar técnicas como:
# 1) Codificación one-hot para convertir categorías a variables binarias
# 2) Label encoding para variables ordinales
# 3) Análisis de grupos (groupby) para comparar estadísticas entre categorías
# 4) Pruebas estadísticas (ANOVA, chi-cuadrado) para evaluar diferencias significativas
