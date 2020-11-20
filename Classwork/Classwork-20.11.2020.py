def run_exercise():
    def sqr_count(number):
        count = 0
        while number >= 2:
            number **= 0.5
            count += 1
        return count

    number = int(input("Enter a number: "))
    print(f"{number} -> {sqr_count(number)}")


run_exercise()
