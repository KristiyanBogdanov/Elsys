def is_vowel(letter):
    vowels_en = ("a", "e", "i", "o", "u")
    vowels_bg = ("а", "ъ", "о", "у", "е", "и")

    return True if letter in vowels_en \
                   or letter in vowels_bg else False


def run_exercise_one():
    print("Exercise one:")

    number = int(input("Enter a number: "))
    count = int(input("Enter a count: "))

    result = [num for num in range(number, number * count + 1, number)]
    print(f"Result: {', '.join(map(str, result))}")


def run_exercise_two():
    print("\nExercise two:")

    string = input("Enter a string: ")

    vowels_found = [l for l in string.lower() if is_vowel(l)]
    print(f'Number of vowels in "{string}": {len(vowels_found)}')


def run_exercise_three():
    print("\nExercise three:")

    given_list = ["my", 1, "turtle", "explain", 3.14, "1", "3.14"]

    # Не бях сигурен какво сте имали предвид по-точно, затова написах два варианта:
    # [1] Проверява дали е число като цяло(т.е. може да е str[пр. "1"], int или float)
    def is_number_v1(element):
        try:
            float(element)
            return True
        except (ValueError, TypeError):
            return False

    # [2] Проверява дали е от тип int или float
    def is_number_v2(element):
        return True if isinstance(element, (int, float)) else False

    result_v1 = [el for el in given_list if not is_number_v1(el)]
    result_v2 = [el for el in given_list if not is_number_v2(el)]

    print(f"Given list: {given_list}")
    print(f"Result version one: {result_v1}\n"
          f"Result version two: {result_v2}")


def run_exercise_four():
    print("\nExercise four:")

    number = input("Enter a number: ")

    is_palindrome = number == number[::-1]
    print(f"Is the number {number} palindrome -> {is_palindrome}")


def run_exercise_bonus():
    print("\nExercise bonus:")

    string = input("Enter a string: ").split()

    for index, word in enumerate(string):
        for l in word:
            if is_vowel(l.lower()):
                string[index] = word.replace(l, "*", 1)
                break

    print(f"Censored: {' '.join(string)}")


run_exercise_one()
run_exercise_two()
run_exercise_three()
run_exercise_four()
run_exercise_bonus()
