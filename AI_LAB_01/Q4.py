import sys

print("1. Add two numbers\n2. Subtract two numbers\n3. Exit")

while True:
    choice = int(input("choice: "))

    if choice > 0 and choice < 4:
        break

# used sys.exit() since no native python alternative for breaking execution
if choice != 1 and choice != 2:
    print("exiting...")
    sys.exit()

n = int(input("first number: "))
m = int(input("second number: "))

if choice == 1:
    print(n + m)
elif choice == 2:
    print(n - m)

