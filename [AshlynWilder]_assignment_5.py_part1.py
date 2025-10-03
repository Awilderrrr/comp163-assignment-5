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