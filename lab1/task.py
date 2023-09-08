from vectors import *

class Task:
    def __init__(self):
        self.vector_x = []
        self.vector_y = []
        self.vector_z = []
        self.weights = []
    def task2(self):
        self.vector_x = list(range(-10, 6))
        self.vector_y = list(range(-5, 11))
        print("TASK 2:")
        print("Vector X:", self.vector_x)
        print("Vector Y:", self.vector_y)
    
    def task3(self):
        self.vector_z = fill_vector_from_vectors(self.vector_x, self.vector_y)
        print("TASK 3:")
        print("Vector Z:", self.vector_z)

    def task4(self):
        print("TASK 4:")
        self.weights = generate_weights(len(self.vector_x))
        print("X vector's first norm:", first_norm(self.vector_x))
        print("X vector's second norm:", second_norm(self.vector_x))
        print("X vector's infinty norm:", infinite_norm(self.vector_x))
        print("X vector's weighted norm:", weighted_norm(self.vector_x, self.weights))

        self.weights = generate_weights(len(self.vector_y))
        print("Y vector's first norm:", first_norm(self.vector_y))
        print("Y vector's second norm:", second_norm(self.vector_y))
        print("Y vector's infinty norm:", infinite_norm(self.vector_y))
        print("Y vector's weighted norm:", weighted_norm(self.vector_y, self.weights))

        self.weights = generate_weights(len(self.vector_z))
        print("Z vector's first norm:", first_norm(self.vector_z))
        print("Z vector's second norm:", second_norm(self.vector_z))
        print("Z vector's infinty norm:", infinite_norm(self.vector_z))
        print("Z vector's weighted norm:", weighted_norm(self.vector_z, self.weights))

    def task6(self):
        print("TASK 6:")
        num = int(input("Enter integer to calculate factorial:"))
        result = factorial(num)
        if result is not None:
            print(f"Factorial of {num}:", result)

    def task7(self):
        print("TASK 7:")
        vector = fill_vector_from_keyboard()
        sum_v, min_v, max_v = find_sum_and_min_max(vector)
        f_norm = first_norm(vector)
        s_norm = second_norm(vector)
        i_norm = infinite_norm(vector)
        self.weights = fill_weights_from_keyboard(len(vector))
        w_norm = weighted_norm(vector, self.weights)
        print("Source vector", vector)
        print("Sum of vector", sum_v)
        print("Minimum of vector", min_v)
        print("Maximum of vector", max_v)
        print("First norm", f_norm)
        print("Second norm", s_norm)
        print("Infinty norm", i_norm)
        print("Weighted norm", w_norm)

