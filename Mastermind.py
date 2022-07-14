import random


def create_secret(colors):
    secret = ""
    for i in range(4):
        secret += colors[random.randrange(6)]
    return secret


def get_guess():
    guess = input("Make your guess: ").upper()
    return guess.upper()


def display_board(history):
        print()
        for row in history:
            for color in row[0]:
                print(f" {color}", end="")
            print(f" | {row[1]} {row[2]}")
        print()


def guess_check(guess, secret):
    guess_is_invalid = True
    while guess_is_invalid:
        if len(guess) == 4:
                for letter in guess:
                    if letter not in "YORPGB":
                        guess_is_invalid = True
                        print("- Please write 4-letter words using the characters Y, O, R, P, G, B!")
                        guess = get_guess()
                guess_is_invalid = False
        else:
            guess_is_invalid = True
            print("- Please write 4-letter words using the characters Y, O, R, P, G, B!")
            guess = get_guess()

    hits = 0
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            hits += 1
    close = 0
    for color in guess:
        close += min(secret.count(color), guess.count(color))
    close = close - hits
    return hits, close


def play_mastermind(colors, code_length, number_of_rounds):
    secret = create_secret(colors)
    history = []
    round = 1
    while round <= number_of_rounds:
        print(f"Round {round}")
        guess = get_guess()
        if guess == 'BOARD':
            display_board(history)
        else:
            hits, close = guess_check(guess, secret)
            print(f"Hits: {hits} Close: {close}\n")
            history.append((guess, hits, close))
            if hits == code_length:
                break
            round += 1
    if hits == code_length:
        print(f"Congratulations, you broke the code! The secret was {secret}.")
    else:
        print(f"You have run out of attempts, you lost the game. The secret was {secret}.")


if __name__ == "__main__":
    play_mastermind("YORPGB", 4, 12)
