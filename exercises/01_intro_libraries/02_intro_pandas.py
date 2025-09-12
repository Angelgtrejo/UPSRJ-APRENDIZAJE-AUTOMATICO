"""
📊 pandas_exercises.py

Ejercicios prácticos para manipular datos de estudiantes usando Pandas.
─────────────────────────────────────────────────────────────
🔧 Requisitos:
    - pandas
    - pyyaml
─────────────────────────────────────────────────────────────
"""

import pandas as pd
import yaml
import logging
import os 

input_csv  = 'inputs/estudiantes.csv'
input_json = 'inputs/estudiantes.json'
input_yaml = 'inputs/estudiantes.yaml'

def setup_logger(index, todo_text):
    log_path = f"test/pandas_exercise_{index:02}.log"
    logger = logging.getLogger(f"ejercicio_{index}")
    logger.handlers.clear()
    handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.info(f"🧪 Ejercicio {index:02}")
    logger.info("--------------------------------------------------")
    logger.info(f"TODO: {todo_text}")
    logger.info("")  # Espacio para que el alumno agregue su resultado debajo
    return logger

# Ejercicio 01
log1 = setup_logger(1, "Cargar el archivo CSV y registrar la cantidad de registros")
log1.info("1000")

# Ejercicio 02
log2 = setup_logger(2, "Cargar el archivo JSON y registrar la cantidad de registros")

# Ejercicio 03
log3 = setup_logger(3, "Cargar el archivo YAML y registrar la cantidad de registros")

# Ejercicio 04
log4 = setup_logger(4, "Mostrar los primeros 5 registros del CSV")

# Ejercicio 05
log5 = setup_logger(5, "Filtrar estudiantes con promedio > 9")

# Ejercicio 06
log6 = setup_logger(6, "Agrupar por carrera y calcular promedio general")

# Ejercicio 07
log7 = setup_logger(7, "Contar estudiantes por género")

# Ejercicio 08
log8 = setup_logger(8, "Exportar estudiantes con promedio >= 9 a 'outputs/excelentes.csv'")
try:
    if os.path.exists('outputs/excelentes.csv'):
        # NOTE: Lee el contenido del archivo y despliegalo en log8
        pass
    else:
        log8.info(False)
except Exception:
    log8.info(False)
    
# Ejercicio 09
setup_logger(9, "Verificar que los tres formatos tengan el mismo número de registros")