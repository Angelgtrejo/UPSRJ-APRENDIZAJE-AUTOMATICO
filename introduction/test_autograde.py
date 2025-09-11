"""
test_autograde.py

Valida los logs generados por el alumno contra los logs esperados por ejercicio.
"""

import os
import difflib

expected_dir = "expected"
test_dir = "test"

# 🧠 Detectar todos los archivos esperados
expected_files = sorted([
    f for f in os.listdir(expected_dir)
    if f.startswith("pandas_exercise_") and f.endswith(".log") or\
        f.startswith("numpy_exercise_") and f.endswith(".log") or\
        f.startswith("scipy_exercise_") and f.endswith(".log") or\
        f.startswith("integrated_exercise_") and f.endswith(".log")
])

# 📋 Resultados por ejercicio
passed = []
failed = []

for filename in expected_files:
    expected_path = os.path.join(expected_dir, filename)
    test_path = os.path.join(test_dir, filename)

    print(f"\n🔍 Evaluando {filename}...")

    if not os.path.exists(test_path):
        print("❌ No se encontró el archivo generado por el alumno.")
        failed.append(filename)
        continue

    with open(expected_path, encoding="utf-8") as f_exp, open(test_path, encoding="utf-8") as f_test:
        expected_lines = f_exp.readlines()
        test_lines = f_test.readlines()

    diff = list(difflib.unified_diff(expected_lines, test_lines, fromfile='esperado', tofile='alumno', lineterm=''))

    if diff:
        print("❌ Diferencias encontradas. Revisa el formato y los valores.")
        # for line in diff:
        #    print(line)
        failed.append(filename)
    else:
        print("✅ Coincide con el esperado.")
        passed.append(filename)

# 📊 Resumen final
print("\n─────────────────────────────────────────────")
print(f"✅ Ejercicios aprobados: {len(passed)}")
print(f"❌ Ejercicios con errores: {len(failed)}")

if failed:
    print("\n💡 Revisa los ejercicios fallidos y asegúrate de que el formato y los valores coincidan exactamente.")