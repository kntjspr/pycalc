import random

def generate_data(n):
    return [random.randint(1, 1000000) for _ in range(n)]