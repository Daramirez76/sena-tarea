#punto 5
import random

vector_original = [random.randint(1, 100) for _ in range(500)]
vector_cuadrado = [num ** 2 for num in vector_original]

print("Vector original:", vector_original)
print("Vector al cuadrado:", vector_cuadrado)
