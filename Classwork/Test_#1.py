def run_exercise_one():
    print("Exercise one:")

    def calculate(build_price, sell_price, volume):
        need_sum = build_price * volume
        profit_from_sales = sell_price * volume
        print(f"Total profit: {profit_from_sales - need_sum}")

    build_price = float(input("Enter a build price: "))
    sell_price = float(input("Enter a sell price: "))
    volume = int(input("Enter a volume: "))

    calculate(build_price, sell_price, volume)


def run_exercise_two():
    print("\nExercise two:")

    TIME_TO_WASH = 21
    DAYS_IN_MONTH = 30

    def wash_hands(n, months):
        total_seconds = n * TIME_TO_WASH * months * DAYS_IN_MONTH
        minutes, seconds = str(total_seconds / 60).split(".")
        print(f"Total time: {minutes} minutes and {seconds} seconds")

    n = int(input("Enter number of times: "))
    months = int(input("Enter period of time (months): "))

    wash_hands(n, months)


print("Name: Kristiyan Bogdanov; Number: 16; Group: 1\n")

run_exercise_one()
run_exercise_two()
