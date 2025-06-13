list = [1, 5, 3, 44, 22]

# sum using built-in function
total = sum(list)
print(total)

t = 0
# sum using loop
for i in list:
    t += i

print(t)

# to find the largest number

# maximum using built-in function
lar = max(list)
print(lar)

# maximum using for loop
largest = list[0]
for i in list:
    if i > largest:
        largest = i

print(largest)