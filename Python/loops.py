# loops

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

for fruit in fruits:
    print(f"Current fruit: {fruit}")

for i in range(5):
    print(f"Current number: {i}")

# Using a while loop
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1

# Nested loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# Loop with break statement
for i in range(5):
    if i == 3:
        print("Breaking the loop at i = 3")
        break
    print(f"Current number: {i}")