import random
import os

def rand_num(difficulty_choice):
    match difficulty_choice:
        case 1:
            rand_num = random.randint(1, 50)
            print('Range: 1 - 50')
            print(rand_num)
            first_guess(rand_num)
        case 2:
            rand_num = random.randint(1, 100)
            print('Range: 1 - 100')
            print(rand_num)
            first_guess(rand_num)
        case 3:
            rand_num = random.randint(1, 500)
            print('Range: 1 - 500')
            print(rand_num)
            first_guess(rand_num)
        case 4:
            rand_num = random.randint(1, 1000)
            print('Range: 1 - 1000')
            print(rand_num)
            first_guess(rand_num)
            
def first_guess(rand_num):
    input_num = input('Guess the number: ')
    if input_num.isdigit():
        input_num = int(input_num)
        difference = abs(rand_num - input_num)
    else:
        print('Invalid input')
        first_guess(rand_num)
        
        if difference == 0:
            print('You won!')
            exit()
        else:
            prev_difference = difference
            if difference < 20: #scale
                print('Hot')
            elif difference < 50: #scale
                print('Cold')

        guess(rand_num, prev_difference)
        
def guess(rand_num, prev_difference):
    guess_num = input('Guess the number: ')
    if guess_num.isdigit():
        guess_num  = int(guess_num)
        difference = abs(rand_num - guess_num)
    else:
        print('Invalid input')
        guess(rand_num, prev_difference)
        
        if difference == 0:
            print('You won!')
            exit()

    if difference < prev_difference:
        print('Warmer')
        prev_difference = difference
        guess(rand_num, prev_difference)
    elif difference > prev_difference:
        print('Colder')
        prev_difference = difference
        guess(rand_num, prev_difference)
    else:
        print('Same distance')
        prev_difference = difference
        guess(rand_num, prev_difference)
    
        
def main():
    
    os.system('cls')
    print('Easy: 1')
    print('Medium: 2')
    print('Hard: 3')
    print('Extreme: 4')
    print('Exit: 5')
    
    difficulty_choice = input('Choice: ')
    if difficulty_choice .isdigit():
        difficulty_choice = int(difficulty_choice)
        if difficulty_choice not in range(1, 6):
            print('Invalid choice')
            main()
            
        if difficulty_choice == 5:
            print('You have chosen to exit')
            exit()
        else:
            rand_num(difficulty_choice)
    else:
        print('Invalid choice')
        main()        

if __name__ == "__main__":
    main()
