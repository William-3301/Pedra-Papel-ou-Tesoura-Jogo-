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

import random

My_choice = int(input("Escolha 0 para pedra, 1 para papel, e 2 para tesoura: "))

choices = [rock, paper, scissors]

Random_Computer = random.randint(0, len(choices) - 1)



if My_choice >= 0 and My_choice <= 2:
	
	print(choices[My_choice])

	print("O computador escolheu:")
	
	if My_choice == 0 and Random_Computer == 0:
		print(choices[Random_Computer])
		print("Foi empate!")

	elif My_choice == 0 and Random_Computer == 1:
		print(choices[Random_Computer])
		print("O Bot ganhou!")

	elif My_choice == 0 and Random_Computer == 2:
		print(choices[Random_Computer])
		print("Você ganhou!")

	elif My_choice == 1 and Random_Computer == 0:
		print(choices[Random_Computer])
		print("Você ganhou!")

	elif My_choice == 1 and Random_Computer == 1:
		print(choices[Random_Computer])
		print("Foi empate!")

	elif My_choice == 1 and Random_Computer == 2:
		print(choices[Random_Computer])
		print("O Bot ganhou!")


	elif My_choice == 2 and Random_Computer == 0:
		print(choices[Random_Computer])
		print("O Bot ganhou!")

	elif My_choice == 2 and Random_Computer == 1:
		print(choices[Random_Computer])
		print("Você ganhou!")

	elif My_choice == 2 and Random_Computer == 2:
		print(choices[Random_Computer])
		print("Foi empate!")

else:
	print("Você escolheu um número invalido!")