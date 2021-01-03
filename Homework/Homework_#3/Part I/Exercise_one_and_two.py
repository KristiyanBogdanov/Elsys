def run_exercise_one():
    print("Exercise one:")

    def is_prime(number):
        for n in range(2, number):
            if number % n == 0:
                return False
        return True

    def next_prime(number):
        while True:
            if number > 1 and is_prime(number):
                return number
            number += 1

    number = int(input("Enter a number: "))
    print(f"Next prime number is {next_prime(number)}")


def run_exercise_two():
    print("\nExercise two:")

    def is_disarium(number):
        digits_power = [int(digit) ** (idx + 1) for idx, digit in enumerate(number)]
        return True if sum(digits_power) == int(number) else False

    number = input("Enter a number: ")
    print(f"Is number {number} disarium -> {is_disarium(number)}")


run_exercise_one()
run_exercise_two()
