def run_exercise_one():
    print("Exercise one: ")

    def is_vowel(letter):
        vowels_en = ("a", "e", "i", "o", "u")
        vowels_bg = ("а", "ъ", "о", "у", "е", "и")

        return True if letter in vowels_en \
                       or letter in vowels_bg else False

    string = input("Enter a string: ")
    result = list(string)

    for index, l in enumerate(result):
        if is_vowel(l.lower()):
            result[index] = l * 4

    print(f"{string} -> {''.join(result)}")


def run_exercise_two():
    print("\nExercise two: ")

    number = input("Enter a number: ")
    number_len = 0

    for _ in number:
        number_len += 1

    print(f"Len of {number} is {number_len}")


def run_exercise_three():
    print("\nExercise three: ")

    number = int(input("Enter a number: "))
    number_cpy = number

    count = 0

    while number_cpy >= 2:
        number_cpy **= 0.5
        count += 1

    print(f"{number} -> {count}")


def run_exercise_four():
    print("\nExercise four: ")

    def is_prime(number):
        for n in range(2, number):
            if number % n == 0:
                return False
        return True

    number = int(input("Enter a number: "))
    result = [num for num in range(2, number + 1) if is_prime(num)]

    print(f"{number} -> {sum(result)}")


run_exercise_one()
run_exercise_two()
run_exercise_three()
run_exercise_four()
