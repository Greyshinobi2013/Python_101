import random

    

def play(choice):
    choices = [ 'Rock' , ' Paper' , 'Scissor']
    random_index = random.randint(0,2)
    #       player         Computer
    #       Rock            Rock
    if choices[choice] == choices[random_index] :
        print(f'{choices[choice]} Vs {choices[random_index]}')
        print('it is a tie')
        #  Rock             Paper
    elif choices[choice] == choices[random_index] :
        print(f'{choices[choice]} Vs {choices[random_index]}')
        print('You have won. congratulations')
        #   Rock            Scissor
    elif choices[choice] == choices[random_index]:
        print(f"{choices[choice]} Vs {choices[random_index]}")
        print('It is a tie, play again?')
        #   Paper           Rock            
    elif choices[choice] == choices[random_index]:
        print(f"{choices[choice]} Vs {choices[random_index]}")
        print('You have won, play again?')
        #   Paper           Paper
    elif choices[choice] == choices[random_index]:
        print(f"{choices[choice]} Vs {choices[random_index]}")
        print('It is a tie, play again?')
        #   Paper           Scissor
    elif choices[choice] == choices[random_index]:
        print(f"{choices[choice]} Vs {choices[random_index]}")
        print('You have lost, play again?')
        #   Scissor         Rock
    elif choices[choice] == choices[random_index]:
        print(f"{choices[choice]} Vs {choices[random_index]}")
        print('You have lost, play again?')
        #   Scissor         Paper
    elif choices[choice] == choices[random_index]:
        print(f"{choices[choice]} Vs {choices[random_index]}")
        print('You have won,  play again?')
        #   Scissor         Scissor
    elif choices[choice] == choices[random_index]:
        print(f"{choices[choice]} Vs {choices[random_index]}")
        print('It is tie, play again?')

print('************************************Welcome to Rock-Paper-Scissor Game*******************************************')
print('Please enter your choice:')
print('0 for Rock')
print('1 for Paper')
print('2 for Scissor')
user_input = int(input('choose:'))
play(user_input)



