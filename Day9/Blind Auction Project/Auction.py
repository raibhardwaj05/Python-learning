# Blind auction
import os

auction = {
    "name": [],
    "bid": []
}

more_bidders = "yes"

while more_bidders == "yes":
    name = input("Name: ")
    bid = int(input("Bid Amount: $"))

    auction["name"].append(name)
    auction["bid"].append(bid)

    more_bidders = input("Are there more bidders? (yes/no):\n").lower()

    if more_bidders == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')

place = 0
highest = auction["bid"][0]

for i in range(0, len(auction["bid"])):

    if auction["bid"][i] > highest:
        highest = auction["bid"][i]
        place = i


print(f'Hightest bidder name: {auction["name"][place]}')
print(f"highest bid: ${highest}")

