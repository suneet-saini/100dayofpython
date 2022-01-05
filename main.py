rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_choice = random.randint(0, 2)

if user_input == 0:
  print(rock)
  if computer_choice == 0:
    print(rock)
    print ("Draw!!")
  elif computer_choice == 1:
    print(paper)
    print ("You Lose!!")
  else:
    print(scissors)
    print ("You Wins!!")
elif user_input == 1:
  print(paper)
  if computer_choice == 0:
    print(rock)
    print ("You Wins!!")
  elif computer_choice == 1:
    print(paper)
    print ("Draw!!")
  else:
    print(scissors)
    print ("You Lose!!")
elif user_input == 2:
  print(scissors)
  if computer_choice == 0:
    print(rock)
    print ("You Lose!!")
  elif computer_choice == 1:
    print(paper)
    print ("You Wins!!")
  else:
    print(scissors)
    print ("Draw!!")
else:
  print("Invalid Input")
