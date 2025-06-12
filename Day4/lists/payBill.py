# Who will pay the bill
import random

friends = ["Rudra", "Bhardwaj", "Tanu", "Huh"]

# mathod 1
index = random.randint(0, 4)
print(friends[index] + " will give the party and pay the bills too")

# method 2
print(random.choice(friends) + " and others will enjoy")
