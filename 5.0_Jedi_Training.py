  #Sign your name: Evan Redenius

'''
 1. Make the following program work.
   '''
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    x = int(input("Enter a number: "))
    total = x + total
print("The total is:",total)



'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(99):
    i+=2
    print(i)


'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
for i in range(10,-1,-1):
    print(i)
print("Blast OFF!")





'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
for i in range(10):
    print(i)




'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
print("This program takes seven numbers and returns the sum.")
total = 0
Pos=0
Neg=0
Zero=0
for i in range(7):
    x = int(input("Enter a number: "))
    if x>0:
        Pos= Pos+1
    elif x<0:
        Neg= Neg+1
    else:
        Zero= Zero+1
    total = x + total
print("The total is:",total)
print("The total number of positives is:",Pos)
print("The total number of Negitaves is:",Neg)
print("The total number of Zeros is:",Zero)