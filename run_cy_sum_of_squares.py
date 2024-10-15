import time
from py_sum_of_squares import sum_of_squares


# Measure the time taken for integer addition
start_time = time.time()
sum_of_squares(10**7)
end_time = time.time()

print(f"Time taken: {end_time - start_time} seconds")
