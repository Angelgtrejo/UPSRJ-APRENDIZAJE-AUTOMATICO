"""
📊 integrated_exercise.py

Ejercicio integrado que combina Pandas, NumPy y SciPy para analizar datos estudiantiles.
─────────────────────────────────────────────────────────────
🔧 Requisitos:
    - pandas
    - numpy
    - scipy
─────────────────────────────────────────────────────────────
"""

import pandas as pd
import numpy as np
import logging
import os
from scipy import stats, linalg

def setup_logger(index, todo_text):
    log_path = f"test/integrated_exercise_{index:02}.log"
    logger = logging.getLogger(f"integrated_{index}")
    logger.handlers.clear()
    handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.info(f"Paso {index:02}")
    logger.info("--------------------------------------------------")
    logger.info(f"TODO: {todo_text}")
    logger.info("")
    return logger

# 📁 Paso 1: Cargar datos desde CSV
log1 = setup_logger(1, "Cargar el archivo 'estudiantes.csv' en un DataFrame llamado df")

# 🧠 Paso 2: Convertir la columna 'promedio' a un arreglo NumPy
log2 = setup_logger(2, "Extraer la columna 'promedio' y convertirla con .to_numpy()")

# 📐 Paso 3: Normalizar los promedios entre 0 y 1
log3 = setup_logger(3, "Aplicar la fórmula de normalización: (x - min) / (max - min)")

# 🔬 Paso 4: Calcular estadísticas con SciPy
log4 = setup_logger(4, "Usar stats.tmean, stats.tstd y stats.mode sobre el arreglo de promedios")
log4.info(f"Media truncada: {0}")
log4.info(f"Desviación estándar truncada: {0}")
log4.info(f"Moda: {0}")

# 🎯 Paso 5: Filtrar estudiantes con promedio normalizado > 0.8
log5 = setup_logger(5, "Crear un nuevo DataFrame con estudiantes destacados")

# 🧮 Paso 6: Crear matriz de características para álgebra lineal
log6 = setup_logger(6, "Usar columnas numéricas como 'edad', 'cuatrimestre' y 'promedio_normalizado'")

# TODO: Calcular la matriz de covarianza con np.cov
log7 = setup_logger(7, "Calcular la matriz de covarianza con np.cov")

# TODO: Calcular la inversa de la matriz con linalg.inv
log8 = setup_logger(8, "Calcular la inversa de la matriz con linalg.inv")

# 🧠 Preguntas interpretativas (responde en comentarios):
# - ¿Qué representa la matriz de covarianza en este contexto?
# - ¿Qué variables parecen estar más relacionadas entre sí?
# - ¿Qué significa que un estudiante tenga promedio normalizado > 0.8?
# - ¿Cómo podrías extender este análisis para incluir variables categóricas como carrera o género?