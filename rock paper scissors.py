import random

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
select = int(input("\n Let's play!!!\n What will you choose?\n(0 - rock)\n(1 -paper)\n(2- scissors)\nType your choice:"))
if select >= 3 or select < 0:
    print("You typed an invalid number, you lose!")
else:
    choices = [rock, paper, scissors]
    print(choices[select])
    computer = random.randint(0, 2)
    print("Computer choice:")
    print(choices[computer])
    if select == 0 and computer == 2:
        print("You win!")
    elif computer == 0 and select == 2:
        print("You lose")
    elif computer > select:
        print("You lose")
    elif select > computer:
        print("You win!")
    elif computer == select:
        print("It's a draw")
