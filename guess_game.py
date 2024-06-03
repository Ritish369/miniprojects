from random import choice

def main():
    initializer()
    user_guess()


def initializer():
    global animals, secret_word, guess
    animals = ["Cow", "Dog", "Cat", "Lion"]
    secret_word = choice(animals)
    guess = ""
    print("Let's play a guessing game!")


def user_guess():
    lives = 3
    while True and lives:
        guess = input("Enter your guessed animal: ").title()
        if guess == secret_word:
            print("Got the animal correctly!")
            break
        else:
            lives -= 1
    if not lives:
        print("You lost!")


if __name__ == "__main__":
    main()
