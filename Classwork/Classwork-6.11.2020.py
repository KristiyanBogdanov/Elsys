def run_exercise_one():
    print("Exercise one")

    number = int(input("Enter a number: "))

    num1, num2 = 0, 1
    count = 0

    if number <= 0:
        print("Wrong - integer is not positive")
    elif number == 1:
        print(f"Fibonacci sequence: {num1}")
    else:
        print("Fibonacci sequence:", end=" ")
        while count < number:
            print(num1, end=" ")

            x = num1 + num2
            num1 = num2
            num2 = x

            count += 1


def run_exercise_two():
    print("\n\nExercise two")

    string = input("Enter string: ")
    number = int(input("Enter a number: "))

    step = round(len(string) / number)
    counter = 0

    result = []

    for i in range(0, len(string), step):
        if counter + 1 == number:
            result.append(string[i::])
            break
        else:
            result.append(string[i:step + i])
        counter += 1

    print(f"String |{string}| split into {number} parts: {result}")


run_exercise_one()
run_exercise_two()
