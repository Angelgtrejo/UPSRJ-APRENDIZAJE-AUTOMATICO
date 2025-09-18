# 🧠 Ejercicios de análisis técnico con Pandas, NumPy y SciPy

**Instructor:** Jesus Salvador Lopez Ortega ([LinkedIn](https://www.linkedin.com/in/jesus-salvador-lopez-ortega/) | [GitHub](https://github.com/chucholoport))

- [🧠 Ejercicios de análisis técnico con Pandas, NumPy y SciPy](#-ejercicios-de-análisis-técnico-con-pandas-numpy-y-scipy)
  - [Introduccion](#introduccion)
  - [Fecha de Entrega](#fecha-de-entrega)
  - [Estructura del trabajo](#estructura-del-trabajo)
  - [Buenas prácticas](#buenas-prácticas)
  - [Preguntas interpretativas](#preguntas-interpretativas)
  - [Cómo empezar](#cómo-empezar)


---

## Introduccion

Este proyecto contiene ejercicios prácticos para desarrollar habilidades en manipulación de datos, álgebra lineal, estadística y procesamiento numérico usando Python. Los ejercicios están organizados por módulo (`intro_numpy.py`, `intro_pandas.py`, `intro_scipy.py`, `integrated_exercise.py`) y cada uno genera un archivo de log que será evaluado automáticamente.

---

## Fecha de Entrega
- **Fecha de Inicio:** Septiembre 18, 2025
- <span style="color:gold"><b>Fecha de Entrega:</b> Septiembre 25, 2025 ⏰</span>

---

## Estructura del trabajo

Cada archivo de ejercicios contiene bloques `TODO` que indican lo que debes implementar. Al ejecutar el archivo, se generarán logs en el root, uno por ejercicio.

---

## Buenas prácticas

- Usa `np.random.seed(0)` cuando trabajes con aleatoriedad para garantizar reproducibilidad.
- Usa `.to_string(index=False)` si necesitas mostrar un `DataFrame` en el log.
- Si un ejercicio involucra álgebra lineal, asegúrate de que las matrices sean compatibles.
- Las preguntas interpretativas deben responderse como comentarios en el código fuente.

---

## Preguntas interpretativas

Al final de algunos módulos encontrarás preguntas abiertas. Estas no se evalúan automáticamente, pero son parte de tu reflexión técnica. Respóndelas como comentarios en el archivo `.py`.

---

## Cómo empezar

1. Clona el repositorio.
2. Inicializa el entorno virtual en una terminal PowerShell:
```bash
   .\setup_venv.ps1
```
3. Ejecuta cada archivo de ejercicios:
```bash
    .\intro_pandas.ps1
    .\intro_numpy.ps1
    .\intro_scipy.ps1
    .\integrated_exercise.ps1
```

1. Verifica que los logs se generen correctamente.
2. Revisa tus resultados antes de entregar. Puedes correr cuantas veces quieras el `test_autograde.py` para validar tus resultados.