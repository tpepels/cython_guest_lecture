import time


# Simple loop that adds integers
def sum_of_integers(limit):
    total = 0
    for i in range(limit):
        total += i
    return total


# Measure the time taken for integer addition
start_time = time.time()
sum_of_integers(10_000_000)
end_time = time.time()

print(f"Time taken to add 10 million integers: {end_time - start_time} seconds")
