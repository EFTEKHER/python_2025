'''
Real world example: Multiprocessing in Python. CPU-bound tasks.
scenario: calculating factorials of large numbers.
Factorials of large numbers are CPU-bound tasks, meaning they require significant computational power.
Multiprocessing can help improve performance by distributing the workload across multiple CPU cores.

'''

import math
import multiprocessing
import time
import sys

## increase the maximum number of digits  for integer conversion
sys.set_int_max_str_digits(1000000)

def factorial(n):
    print(f"Calculating factorial of {n}")
    print(f"Factorial of {n} is {math.factorial(n)}")
    return math.factorial(n)

if __name__ == "__main__":
    numbers = [10000, 2000, 3000, 4000, 5000]
    start_time = time.time()
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(factorial, numbers)
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")
    # print("Factorials calculated:", results)     