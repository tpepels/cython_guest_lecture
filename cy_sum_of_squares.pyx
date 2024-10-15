
cpdef long long sum_of_squares(long long n):
    cdef long long i
    cdef long long result = 0

    # Loop through and calculate sum of squares
    for i in range(n):
        result += i * i

    return result





