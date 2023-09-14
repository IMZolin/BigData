import math
import random

def fill_vector_from_keyboard():
    vector = []
    n = int(input("Enter the length of the vector (default is 5): ") or 5)
    for i in range(n):
        element = float(input(f"Enter element {i + 1}: "))
        vector.append(element)
    return vector

def fill_weights_from_keyboard(num_elements):
    weights = []
    while abs(sum(weights) - 1.0) > 0.001:
        weights = []
        for i in range(num_elements):
            weight = float(input(f"Enter weight {i + 1}: "))
            if weight < 0 or weight > 1:
                print("Weight must be >= 0 and <= 1.")
                break
            weights.append(weight)
        
        if abs(sum(weights) - 1.0) > 0.001:
            print("Weights must sum to 1.0. Please try again.")
    return weights

def generate_weights(num_elements):
    if num_elements <= 0:
        raise ValueError("Number of elements must be greater than 0")
    
    weights = [random.uniform(0, 1) for _ in range(num_elements)]
    total_weight = sum(weights)
    weights = [weight / total_weight for weight in weights]
    print(total_weight)
    return weights


def fill_vector_from_vectors(vector1, vector2):
    result = []
    for i in range(max(len(vector1), len(vector2))):
        if i < len(vector1):
            result.append(vector1[i])
        if i < len(vector2):
            result.append(vector2[i])
    return sorted(result)

def first_norm(vector):
    return sum(abs(x) for x in vector)

def second_norm(vector):
    return math.sqrt(sum(x**2 for x in vector))

def infinite_norm(vector):
    return max(abs(x) for x in vector)

def weighted_norm(vector, weights):
    if len(vector) != len(weights):
        raise ValueError("Vector and weights must have the same length.")
    return math.sqrt(sum(abs(w * x) for x, w in zip(vector, weights)))

def find_sum_and_min_max(vector):
    if not vector:
        return None, None, None 
    return sum(vector), min(vector), max(vector)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)