'''
______
PART 1
______
The code below prompts the user to enter two numbers, and then prints out the smaller of the numbers entered. Modify so that it prompts the user to enter THREE numbers, and then prints the smallest of the three numbers entered in a sentence.

(Hint: You'll need to be careful for the cases when the user enters the same number twice or all three times.)

An example of what should appear on the console when the code is run:

Enter a number: 11
Enter another number: 2
Enter another number: 5

The smallest number is 2
'''

n = int(input('Enter first number  : '))
n1 = int(input('Enter second number : '))
n2 = int(input('Enter third number  : '))

smallest = 0

if n < n1 and n < n2:
    smallest = n
elif n1 < n2:
    smallest = n1
else :
    smallest = n2
print("The smallest number is:",smallest)