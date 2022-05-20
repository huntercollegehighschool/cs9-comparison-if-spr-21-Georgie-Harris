'''
______
PART 4
______
Write a program that prompts the user to enter two integer inputs. The program prints a string stating if the inputs are both positive, negative, if one of the inputs is zero, or if they have opposite signs. (Hint: this code can be written using only four code blocks, but you may find ways to do this using more.)

Four examples of what should appear on the console when this program runs (note: the test driver is case sensitive):

Enter a number:  3
Enter another number:  7
positive

Enter a number:  -5
Enter another number:  -2
negative

Enter a number:  7
Enter another number:  0
zero

Enter a number:  2
Enter another number:  -2
opposite
'''

#start writing your code below
n = int(input("enter a number:"))
n2 = int(input("enter another number:"))

if(n > 0) and (n2 > 0):
  print("Positive")
elif(n < 0) and (n2 < 0):
  print("Negative")
elif (n == 0) or (n2 == 0):
  print("Zero")
elif (n == n2 * -1) or (n2 == n * -1):
  print("opposite")
else:
  print("no")