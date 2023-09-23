import random


def generate_password(words, symbols):
    password = ""
    word = random.choice(words)
    words_copy = words.copy()
    words_copy.remove(word)

    symbol = random.choice(symbols)

    number = random.randint(0, 9999)

    arr = [word, str(number), symbol]
    random.shuffle(arr)

    for e in arr:
        password += e

    return password


def main():
    words = ["OWASP", "Shop", "Juice", "team", "password", "Support", "login", "admin", "original"]
    symbols = "!@#$%^&*()_+"

    with open("generated_passwords.txt", "w") as file:
        for i in range(10000000):
            password = generate_password(words, symbols)
            file.write(f"{password}\n")
            print(i)

    print("Passwords generated and saved to 'generated_passwords.txt'")


if __name__ == "__main__":
    main()
