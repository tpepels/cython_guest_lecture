import numpy as np
cimport numpy as np

# Define a function that takes two memoryviews of long long integers
cpdef long long dot_product(np.ndarray[long long, ndim=1] a, 
                            np.ndarray[long long, ndim=1] b):
    cdef long long i, result = 0
    cdef long long[:] a_view = a  # Create a memoryview for array a
    cdef long long[:] b_view = b  # Create a memoryview for array b

    # Ensure that both arrays are of the same length
    if a_view.shape[0] != b_view.shape[0]:
        raise ValueError("Arrays must have the same length.")

    # Loop through the arrays and compute the dot product
    for i in range(a_view.shape[0]):
        result += a_view[i] * b_view[i]

    return result



