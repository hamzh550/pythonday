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


print("welcom to Rock -paper scissors Game?\n")

userchoose=int(input("What do you choose ? type 0 for Rcok ,1 for paper or 2 for scissors."))
pcchoose=random.randint(0,2)



print (f'cumputer choose {pcchoose}\n')

if userchoose==pcchoose:
    print("Please try again\n")
    if userchoose==0:
        print(f'PC choose {rock}\n')
        print(f'You choose {rock}\n')
    if userchoose==1:
        print(f'PC choose {paper}\n')
        print(f'You choose {paper}\n')
    if userchoose==2:
        print(f'PC choose {scissors}\n')
        print(f'You choose {scissors}\n')


if userchoose==0 and pcchoose==1:
    print("Please try again")
    print(f'PC choose {paper}\n')
    print(f'You choose {rock}\n')

if userchoose==1 and pcchoose==0:
    print("Please try again")
    print(f'PC choose {paper}\n')
    print(f'You choose {rock}\n')



if userchoose==2 and pcchoose==1:
    print("You win")
    print(f'PC choose {paper}\n')
    print(f'You choose {scissors}\n')
    

if userchoose==1 and pcchoose==2:
    print("You lost")
    print(f'PC choose {scissors}\n')
    print(f'You choose {paper}\n')
