# TT: @ivanitchoo_ | email:ivan.mangunyane@outlook.com | Udemy course - guessing challenge


#Variable creation to save the random number.
import random
random_num = random.randint(1,101)

#Welcome message.
print("WELCOME TO GUESSING GAME!")
print("Try to guess a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

#NewList created to store the guessed values. 
guessed_values=[0]

while True:
    guess = int(input("Guess a number: ")) #The user inputs the guessed value

    if(1 > guess or guess > 100):
        print("OUT OF BOUNDS!")
        continue
    

    if guess == random_num:
        print(f"Congratulations! You got it right after {len(guessed_values)} chances. The Number I was Thinking of is exactly {random_num}")
        break

    guessed_values.append(guess) #The guessed values are added to the list if they're not correct.


    # when testing the first guess, guessed_values[-2]==0, which evaluates to False
    # and brings us down to the second section
    
    if guessed_values[-2]: 
        if abs(random_num-guess) < abs(random_num-guessed_values[-2]):
            print('WARMER!')
        else:
            print('COLDER!')


    else:
        if(abs(random_num-guess)<=10):
            print("WARM!")

        else:
            print("COLD")
