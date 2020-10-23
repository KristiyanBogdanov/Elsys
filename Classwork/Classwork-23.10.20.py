# не работи задачата с простите числа

def is_prime(n):
	if n <= 1 or n % 1 > 0:
		return False
	for i in range(2, n//2):
		if n % 1 == 0:
			return False
	return True


result = 0
for x in range(int(input()) + 1):
	result += x
	
print(result)

ll = [1, 5, 4, 16, 0, 52, 17]
odd_numbers = 0
even_numbers = 0

for number in ll:
	if number != 0:	
		if number % 2 == 0:
			odd_numbers += 1
		else:
			even_numbers += 1
		
print(f"Odd count: {odd_numbers}, Even count: {even_numbers}")

age = int(input())
person_age = 0.0

for x in range(1, age + 1):
	person_age += 10.5 if x <= 2 else 4.0
		
print(person_age)

n = int(input())
number = 2
prime_number = []

while True:
	if number == n:
		break
	if is_prime(number):
		prime_number.append(number)
	else:
		number += 1
		
print(prime_number)
	
	
