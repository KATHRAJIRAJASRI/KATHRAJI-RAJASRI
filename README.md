# KATHRAJI-RAJASRI
PROBLEM 1-[The Calculator class takes two numbers (a and b) and an operation type (add, subtract, multiply, or divide) as input during object creation. The class contains a method named calculate() that checks the operation type and performs the corresponding arithmetic operation on the two numbers. If the operation is "add", it adds the numbers; if "subtract", it subtracts the second number from the first; if "multiply", it multiplies them; and if "divide", it divides the first number by the second, while also checking if the divisor is zero to prevent a division error. If an unsupported operation is entered, it prints an error message. In the given example, the values a = 10.0, b = 5.0, and operation = "multiply" are used, so the program calculates and prints the result 50.0. The program demonstrates basic object-oriented principles, clean structure, and simple error handling.]
-LANGUAGE:Python
-Approch:class Calculator:
1. Defines a new class named Calculator to perform arithmetic operations.

def _init_(self, a, b, operation):
Constructor method that initializes the values for a, b, and the chosen operation.

self.a = a
Stores the first number as an instance variable.

self.b = b
Stores the second number as an instance variable.

self.operation = operation
Stores the type of operation as an instance variable.

def calculate(self):
Defines a method to perform the calculation based on the operation type.

if self.operation == "add":
Checks if the operation is addition.

result = self.a + self.b
 Calculates the sum of a and b.

print("Result:", result)
 Prints the result of the operation.

elif self.operation == "subtract":
Checks if the operation is subtraction.

result = self.a - self.b
Calculates the difference between a and b.

elif self.operation == "multiply":
Checks if the operation is multiplication.

result = self.a * self.b
Calculates the product of a and b.

elif self.operation == "divide":
Checks if the operation is division.

if self.b == 0:
Checks for division by zero to prevent an error.

print("Error: Division by zero")
Displays an error if division by zero is attempted.

result = self.a / self.b
Performs division if b is not zero.

else:
Handles cases where the operation is not recognized.

print("Error: Invalid operation")
Displays an error message for unsupported operations.

a = 10.0
Assigns 10.0 to variable a.

b = 5.0
Assigns 5.0 to variable b.

operation = "multiply"
Sets the operation to multiplication.

calc = Calculator(a, b, operation)
Creates an object of the Calculator class with given inputs.

calc.calculate()
Calls the calculate() method to perform the operation and print the result.



PROBLEM 2:[This Python program prints the first a odd numbers in a comma-separated format, where a is a number provided by the user. It starts by taking an integer input from the user and storing it in the variable a. Two variables are initialized: i as a counter to track how many numbers have been printed, and num starting at 1, which represents the first odd number. A while loop runs until i becomes equal to a, ensuring that exactly a odd numbers are printed. In each iteration, the current odd number (num) is printed. If it is not the last number in the sequence, a comma and a space are added for formatting. The variable num is then increased by 2 to move to the next odd number, and i is incremented by 1. This loop continues until all required odd numbers are displayed. The final output is a cleanly formatted list of the first a odd numbers starting from 1.]
LANGUAGE:PYTHON
APPROCH:a = int(input("Enter a number: "))
Takes an integer input from the user and stores it in variable a.

i = 0
 Initializes a counter variable i to 0, used to track how many numbers have been printed.

num = 1
 Initializes the starting number (num) as 1, which is the first odd number.

while i < a:
Starts a loop that runs a times to print the first a odd numbers.

print(num, end="")
Prints the current odd number without moving to a new line.

if i < a - 1:
Checks if it's not the last number to be printed.

print(", ", end="")
If it's not the last number, prints a comma and space for formatting.

num = num + 2
 Increments num by 2 to get the next odd number.

i = i + 1
 Increments the counter i to continue the loop.




PROBLEM3:[This Python program prints a specific number of odd numbers based on a user's input, with special handling for even and odd inputs. It begins by asking the user to enter an integer, which is stored in the variable a. The program then checks whether a is even or odd using the modulo operator (a % 2). If a is even, it reduces the count by 1 to ensure only the previous odd number of values are considered; if a is odd, it keeps the count unchanged. This adjusted value is stored in the variable count, which determines how many odd numbers will be printed. The program initializes two variables: i as a loop counter starting at 0, and num as the first odd number, initialized to 1. A while loop runs until i reaches count, printing odd numbers in sequence. After each number is printed, if it's not the last in the list, a comma and space are added for proper formatting. The value of num increases by 2 in each iteration to generate the next odd number, and i is incremented by 1 to continue the loop. As a result, the program outputs a comma-separated list of odd numbers based on the nearest smaller odd number to the input.]
LANGUAGE:PYTHON
APPROCH:a = int(input("Enter a number: "))
Takes an integer input from the user and stores it in variable a.

if a % 2 == 0:
Checks if the input number a is even.

count = a - 1
If a is even, sets count to one less than a to make it odd.

else:
Executes if a is odd.

count = a
If a is already odd, uses it directly as the count.

i = 0
Initializes a loop counter i to 0.

num = 1
Sets the starting number num to 1 (the first odd number).

while i < count:
Runs a loop to print odd numbers until i reaches count.

print(num, end="")
Prints the current odd number without moving to the next line.

if i < count - 1:
Checks if the current number is not the last in the sequence.

print(", ", end="")
If it's not the last number, prints a comma and space for formatting.

num = num + 2
Increments num by 2 to get the next odd number.

i = i + 1
Increments the counter i to move to the next iteration.



PROBLEM4:[This Python program counts how many numbers in a given list are divisible by each number from 1 to 9. It begins with a predefined list of integers stored in the variable numbers. Two while loops are used to perform the task without using built-in functions like len() or list methods. The outer loop runs with the variable i from 1 to 9, representing each divisor. For every value of i, a counter variable count is initialized to zero. The inner loop, controlled by the variable j, iterates through each element in the numbers list (which contains exactly 11 elements). For each element, it checks whether it is divisible by i using the modulo operator (%). If the result is zero, it increments the count by one. After checking all numbers for a particular i, it prints the divisor and the count of numbers divisible by it in the format i : count. This process continues until all values from 1 to 9 have been used as divisors. The final output shows how many numbers in the list are divisible by each number from 1 to 9.]
LANGUAGE:PYTHON
APPROCH:numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
Defines a list of integers to be checked for divisibility.

i = 1
Initializes the outer loop counter i to 1, representing the current divisor.

while i <= 9:
 Starts a loop to check divisibility for each number from 1 to 9.

count = 0
Initializes a counter to keep track of how many numbers are divisible by i.

j = 0
 Initializes the inner loop counter j to 0, used to iterate through the list.

while j < 11:
 Starts a loop to go through all 11 elements in the numbers list.

num = numbers[j]
 Retrieves the current number from the list.

if num % i == 0:
 Checks if the current number is divisible by i.

count = count + 1
 If divisible, increments the count by 1.

j = j + 1
 Moves to the next number in the list.

print(i, ":", count)
 Prints the divisor i and the count of numbers divisible by it.

i = i + 1
 Increments the divisor to check the next number from 1 to 9.



