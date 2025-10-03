# Challenge 1: Number Sequence Generator
print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: "))
steps_count = 0

print("Sequence:", end=" ")
while current_number != 1:
    print(current_number, end=" ")
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        current_number = 3 * current_number + 1
    steps_count += 1

print(1)
print("Steps:", steps_count, "\n")

# Challenge 2: Prime Number Checker
print("=== Challenge 2: Prime Number Checker ===")
n = int(input("Enter a number: "))

# Challenge 3: Multiplication Table Grid
print(f"Testing divisors from 2 to {n - 1}...")
divisor_found = None
for d in range(2, n):
    if n % d == 0:
        divisor_found = d
        break

if divisor_found is None and n >= 2:
    print(f"{n} is prime!\n")
else:
    print(f"{n} is not prime (divisible by {divisor_found})\n")

#  Challenge 3: Multiplication Table Grid
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")

print("    ", end="")
for col in range(1, 11):
    print(f"{col:4}", end="")
print()

for row in range(1, 11):
    print(f"{row:2} ", end="")
    for col in range(1, 11):
        product = row * col
        print(f"{product:4}", end="")
    print()