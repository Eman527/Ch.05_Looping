'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
done = False
while not done:
    PLR = input("Enter 1 for Rock 2 for Paper and 3 for Scissors or 4 if you want to quit? ")
    if PLR == 1:
        PLR = "Rock"
    elif PLR == 2:
        PLR = "Paper"
    else:
        PLR = "Scissor"
    import random
    RPS = int(random.randrange(1, 4))
    if RPS == 1:
        print("Rock")
    elif RPS == 2:
        print("Paper")
    else:
        print("Scissors")














'''
G = False
Quit = input("Would you like to quit? ")
if Quit.lower() == "yes":
    G = True
else:
while G is False:
    PLR = input("Rock, Paper, Scissors? ")
    if PLR.lower() == "rock":
        PLR = "Rock" 
    
    
    import random
    RPS = random.randrange(1, 4)
    if RPS == 1:
        RPS = "Scissors"
    elif RPS == 2:
        RPS = "Rock"
    else:
        RPS = "Paper"
'''




