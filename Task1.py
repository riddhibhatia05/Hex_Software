# Function to generate Fibonacci series
def fibonacci_series(n):
    # Initial two numbers of the series
    a, b = 0, 1
    series = []
    
    # Generate series up to n terms
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    
    return series

# Input from the user
num_terms = int(input("Enter the number of terms for the Fibonacci series: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci series up to {num_terms} terms:")
    print(fibonacci_series(num_terms))