def user_input():
    """
    Return proper value provided by the user.

    :rtype: str
    :return: value provided by the user from ["too small", "too big", "you won"]
    """

    possible_input = ["too small", "too big", "you won"]

    while True:
        user_answer = input().lower()
        if user_answer in possible_input:
            break
        print("Your answer must be: 'too small', 'too big' or 'you won'!")
    return user_answer


def guess_the_number():
    """Main function for our program."""

    print("Think about a number in range 0-1000 and I'll guess it in max. 10 tries!")
    print("Press 'Enter' to continue")
    input()

    min_number = 0
    max_number = 1000

    user_answer = ""

    while user_answer != "you won":
        guess = (max_number - min_number) // 2 + min_number
        print(f"Your number is: {guess}")
        user_answer = user_input()

        if user_answer == "too big":
            max_number = guess
        elif user_answer == "too small":
            min_number = guess

    print("Yaaaaay! I won!")


if __name__ == '__main__':
    guess_the_number()
