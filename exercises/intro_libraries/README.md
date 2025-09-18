# 🧠 Ejercicios de análisis técnico con Pandas, NumPy y SciPy

Este repositorio contiene ejercicios prácticos para desarrollar habilidades en manipulación de datos, álgebra lineal, estadística y procesamiento numérico usando Python. Los ejercicios están organizados por módulo (`pandas_exercises.py`, `numpy_exercises.py`, `scipy_exercises.py`, `integrated_exercise.py`) y cada uno genera un archivo de log que será evaluado automáticamente.

---

## 📦 Estructura del trabajo

Cada archivo de ejercicios contiene bloques `TODO` que indican lo que debes implementar. Al ejecutar el archivo, se generarán logs en la carpeta `test/`, uno por ejercicio, con el siguiente formato:
test/ 
├── pandas_exercise_01.log 
├── numpy_exercise_03.log 
├── scipy_exercise_02.log 
├── integrated_exercise_05.log


Cada log comienza con una leyenda fija que describe el objetivo del ejercicio. Tu tarea es completar el código para que el resultado correcto aparezca debajo de esa leyenda.

---

## 🧪 Evaluación automática

Tu entrega será evaluada comparando los logs generados en `test/` contra los logs esperados en `expected/`. Para que la evaluación funcione correctamente:

- **No modifiques el encabezado del log** (la leyenda `TODO`).
- **Solo escribe el resultado debajo**, en formato plano: números, arreglos, matrices, `True/False`, o salidas de `DataFrame`.
- **No uses decorativos, emojis ni formatos extraños**.
- **Si el ejercicio requiere generar un archivo**, asegúrate de:
  - Crear la carpeta si no existe.
  - Guardar el archivo correctamente.
  - Leerlo y mostrar su contenido en el log.
  - Registrar `False` si algo falla.

---

## 📐 Buenas prácticas

- Usa `np.random.seed(0)` cuando trabajes con aleatoriedad para garantizar reproducibilidad.
- Usa `.to_string(index=False)` si necesitas mostrar un `DataFrame` en el log.
- Si un ejercicio involucra álgebra lineal, asegúrate de que las matrices sean compatibles.
- Las preguntas interpretativas deben responderse como comentarios en el código fuente.

---

## 🧠 Preguntas interpretativas

Al final de algunos módulos encontrarás preguntas abiertas. Estas no se evalúan automáticamente, pero son parte de tu reflexión técnica. Respóndelas como comentarios en el archivo `.py`.

---

## 🚀 Cómo empezar

1. Clona el repositorio.
2. Inicializa el entorno virtual en una terminal PowerShell:
```bash
   .\setup_venv.ps1
```
3. Ejecuta cada archivo de ejercicios:
```bash
    python pandas_exercises.py
    python numpy_exercises.py
    python scipy_exercises.py
    python integrated_exercise.py
```

4. Verifica que los logs se generen correctamente en `test/`.
5. Revisa tus resultados antes de entregar. Puedes correr cuantas veces quieras el `test_autograde.py` para validar tus resultados.