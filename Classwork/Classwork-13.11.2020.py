from math import sqrt


def is_vowel(letter):
    vowels_en = ("a", "e", "i", "o", "u")
    vowels_bg = ("а", "ъ", "о", "у", "е", "и")

    return True if letter in vowels_en \
                   or letter in vowels_bg else False


def run_exercise_one():
    print("Exercise one: ")

    string = input("Enter a string: ")
    result = []

    for l in string:
        if is_vowel(l):
            result.append(l * 4)
            continue
        result.append(l)

    print(f"Result: {''.join(result)}")


def run_exercise_two():
    print("\nExercise two: ")

    number = input("Enter a number: ")
    count = 0

    for _ in number:
        count += 1

    print(f"Len of {number} is {count}")


def run_exercise_three():
    print("\nExercise three: ")

    number = int(input("Enter a positive number: "))
    number_cpy = number

    count = 0

    while True:
        number_cpy = sqrt(number_cpy)
        count += 1

        if number_cpy < 2:
            print(f"{number} -> {count}")
            break


def run_exercise_four():
    print("\nExercise four: ")

    def is_prime(number):
        for num in range(2, number):
            if number % num == 0:
                return False
        return True

    number = int(input("Enter a number: "))
    result = 0

    for num in range(number + 1):
        if num > 1 and is_prime(num):
            result += num

    print(f"{number} -> {result}")


run_exercise_one()
run_exercise_two()
run_exercise_three()
run_exercise_four()
