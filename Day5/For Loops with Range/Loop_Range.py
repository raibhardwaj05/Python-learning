# using range(a, b) ===>> b is exclusive so use b+1
total = 0

# sum
for i in range(1, 100+1):
    total += i

print("sum: ", total)

# multiplication table
print("\n5 table:")
for i in range(1, 10+1):
    print(5*i)


# natural number
print("\nnatural numbers")
for i in range(1, 10+1):
    print(i)

# specify how many numbers to add to print next number
print("\nhow many numbers to add: ")
for i in range(1, 10+1, 2):
    print(i)
# this will add 2 to the previous number and print the next number
# output: 1, (1+2), (3+2),...upto which limit is reached (10)
# actual output: 1, 3, 5, 7, 9