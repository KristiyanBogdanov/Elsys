def run_exercise_one():
    print("Exercise one:")

    start_number = 2000
    end_number = 5001

    def is_number_valid(number):
        for digit in number:
            if int(digit) % 2:
                return False
        return True

    valid_numbers = []
    for number in range(start_number, end_number):
        if is_number_valid(str(number)):
            valid_numbers.append(number)

    print(f"Valid numbers: {', '.join(map(str, valid_numbers))}")


def run_exercise_two():
    print("\nExercise two:")

    pattern_input = "Enter your list len: "
    numbers = [int(input(f"Number[{i + 1}]: "))
               for i in range(int(input(pattern_input)))]

    result = abs(min(numbers) - max(numbers))
    print(f"Result: Abs. value of MIN - MAX = {result}")


def run_exercise_three():
    print("\nExercise three:")

    string = input("Enter your string: ")

    count_digits = 0
    count_letters = 0

    for character in string:
        if character.isdigit():
            count_digits += 1
        elif character.isalpha():
            count_letters += 1

    print(f"Number of letters - {count_letters}; digits - {count_digits}")


run_exercise_one()
run_exercise_two()
run_exercise_three()
