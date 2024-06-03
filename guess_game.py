from random import choice


def main():
    initializer()
    user_guess()


def initializer():
    global animals, secret_word, guess
    animals = ["Cow", "Dog", "Cat"]
    secret_word = choice(animals)
    guess = ""
    print("Let's play a guessing game!")


def user_guess():
    while True:
        guess = input("Enter your guessed animal: ").title()
        if guess == secret_word:
            print("Got the animal correctly!")
            break
        else:
            print("Nah! Take another chance.")


if __name__ == "__main__":
    main()
