#punto 6
import random

# Crear matriz M(50,5): id, calificación1, calificación2, calificación3, calificaciónFinal
M = []
for i in range(1, 51):
    cal1 = round(random.uniform(1.0, 5.0), 1)
    cal2 = round(random.uniform(1.0, 5.0), 1)
    cal3 = round(random.uniform(1.0, 5.0), 1)
    cal_final = round((cal1 + cal2 + cal3) / 3, 1)
    M.append([i, cal1, cal2, cal3, cal_final])

# A) Cantidad de alumnos que aprobaron (3.0 a 5.0)
aprobados = sum(1 for x in M if 3.0 <= x[4] <= 5.0)

# B) Cantidad de alumnos a recuperación (2.0 a 2.9)
recuperacion = sum(1 for x in M if 2.0 <= x[4] <= 2.9)

# C) Alumnos con calificación máxima (5.0)
maximos = sum(1 for x in M if x[4] == 5.0)

print(f"Cantidad de alumnos que aprobaron: {aprobados}")
print(f"Cantidad de alumnos que deben ir a recuperación: {recuperacion}")
print(f"Cantidad de alumnos con calificación máxima: {maximos}")
