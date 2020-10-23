def run_exercise_one():
    print("First exercise:")

    result = 0
    number = int(input("Enter your number: "))

    for num in range(number + 1):
        result += num

    print(f"Result: {result}")


def run_exercise_two():
    print("\nSecond exercise:")

    numbers = [1, 5, 4, 16, 0, 52, 17]
    odd_numbers_count = 0
    even_numbers_count = 0

    for number in numbers:
        if number != 0:
            if number % 2:
                even_numbers_count += 1
            else:
                odd_numbers_count += 1

    print(f"Odd numbers (count): {odd_numbers_count},"
          f" Even numbers (count): {even_numbers_count}")


def run_exercise_three():
    print("\nThird exercise:")

    n = int(input("Enter your number: ")) - 1
    prime_numbers = [2]
    current_number = 2

    while n:
        if is_prime(current_number):
            prime_numbers.append(current_number)
            n -= 1
        current_number += 1

    print(f"Prime numbers to n: {', '.join(map(str, prime_numbers))}")


def is_prime(number):
    for num in range(2, number):
        return False if number % num == 0 else True


def run_exercise_four():
    print("\nForth exercise:")

    age = int(input("Enter dog age: "))
    person_age = 0.0

    for x in range(1, age + 1):
        person_age += 10.5 if x <= 2 else 4.0

    print(f"Dog age - {age} || Person age - {int(person_age)}")


print("Classwork - 23.10.2020\n")

run_exercise_one()
run_exercise_two()
run_exercise_three()
run_exercise_four()
