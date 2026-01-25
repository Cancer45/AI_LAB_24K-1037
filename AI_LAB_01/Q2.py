n = int(input("Number: "))
even_nums = []

i = 0
while 2 * i <= n:
    even_nums.append(2 * i)
    i += 1
print(even_nums)
print("even numbers: ", i)

