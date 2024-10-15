#include <stdio.h>
#include <time.h>
#include <math.h>

// Function to sum squares up to a limit
long long sum_of_squares(long long limit)
{
    long long total = 0;
    for (int i = 0; i < limit; i++)
    {
        total += i * i;
    }
    return total;
}

int main()
{
    // Set the limit
    int limit = pow(10, 7);
    // Get the start time
    clock_t start_time = clock();
    // Call the function to sum integers
    long long result = sum_of_squares(limit);
    // Get the end time
    clock_t end_time = clock();
    // Calculate the time taken in seconds
    double time_taken = (double)(end_time - start_time) / CLOCKS_PER_SEC;
    // Print the results
    printf("Sum of first %d integers: %lld\n", limit, result);
    printf("Time taken: %f seconds\n", time_taken);
    return 0;
}
