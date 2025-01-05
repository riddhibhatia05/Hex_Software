TASK 1:-
Fibonacci Series in Python
This program generates the Fibonacci series, a sequence of numbers where each number is the sum of the two preceding numbers. The sequence begins with 0 and 1. For example, the first 10 Fibonacci numbers are:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

How the Program Works
1. Understanding the Fibonacci Series
The Fibonacci sequence is defined by the recurrence relation:
F(n) = F(n-1) + F(n-2),
with the initial conditions:
F(0) = 0 and F(1) = 1.

2. Algorithm
To generate the series up to n terms:
Start with the initial values a = 0 and b = 1.
Use a loop to calculate the next term as a + b while updating a and b.
Append each term to a list for storage.
Stop after n terms.

4. Code Implementation

# Function to generate Fibonacci series
def fibonacci_series(n):
    # Initial two numbers of the series
    a, b = 0, 1
    series = []  # List to store the series
    
    # Generate series up to n terms
    for _ in range(n):
        series.append(a)  # Add the current term to the list
        a, b = b, a + b   # Update 'a' and 'b' for the next term
    
    return series

# Input from the user
num_terms = int(input("Enter the number of terms for the Fibonacci series: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci series up to {num_terms} terms:")
    print(fibonacci_series(num_terms))
4. Detailed Explanation
Function fibonacci_series(n)
Inputs:
n (integer) - The number of terms in the Fibonacci series.

Logic:
Start with two variables: a = 0 and b = 1, which represent the first two terms of the Fibonacci sequence.
Create an empty list series to store the generated numbers.
Use a for loop that runs n times. During each iteration:
Append the value of a to series.
Calculate the next Fibonacci number by updating a to b and b to a + b.
Return the list series containing the Fibonacci sequence.

Input Validation
Before calling the fibonacci_series function, the program checks if the input (num_terms) is greater than 0. If not, it prints an error message and exits.
Input and Output

The user is prompted to enter the number of terms.
If the input is valid, the program calculates and prints the Fibonacci sequence.

5. Sample Outputs
Example 1:
Enter the number of terms for the Fibonacci series: 7
Output:
Fibonacci series up to 7 terms:
[0, 1, 1, 2, 3, 5, 8]

Example 2:
Enter the number of terms for the Fibonacci series: -5
Please enter a positive integer.

6. Key Features
User Input Validation: Ensures the user enters a valid positive integer.
Dynamic Series Generation: The program can generate the Fibonacci series for any positive number of terms.
Scalability: The code can easily be extended to handle larger numbers using techniques like memoization or generators.

How to Run the Program
Install Python (if not already installed) from python.org.
Copy the above code into a Python file, e.g., fibonacci.py.
Open a terminal or command prompt, navigate to the file's directory, and run the program:
python fibonacci.py
Enter the number of terms as prompted.
