import random

def main():
    attempts = 0
    secret_num = random.randrange(100)
    print("I have chosen a number between 1 and 100. Can you guess it?")
    while True:
        guess = input("Please guess a number between 1 and 100: ")
        attempts += 1

        #non numeric check
        if guess.isalpha():
            continue

        if int(guess) == secret_num:
            print("Congrats! The secret number was {}, and it took you {} attempts.".format(secret_num, attempts))
            break    

        #if else statement to decide to print the guess too high
        #or guess too low message
        if int(guess) < secret_num:
            print("Too low!")
            continue
        else:
            print("Too high!")
            continue
        
    #congrats message stating the secret number and how many attempts it took
    #print()\

if __name__ == "__main__":
    main()