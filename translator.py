def main():
    print(translate(input("Enter a phrase: ")))


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            if letter.isupper():
                translation = translation + "R"
            else:
                translation = translation + "r"
        else:
            translation = translation + letter
    return translation


if __name__ == "__main__":
    main()
