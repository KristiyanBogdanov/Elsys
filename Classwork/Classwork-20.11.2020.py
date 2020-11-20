def run_exercise():
    def sqrt_count(number):
        count = 0
        while number >= 2:
            number **= 0.5
            count += 1
        return count

    number = int(input("Enter a number: "))
    print(f"{number} -> {sqrt_count(number)}")


run_exercise()
