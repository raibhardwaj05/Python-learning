import random

def draw_cards():
    return random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

def score_count(cards):
    total = sum(cards)

    while 11 in cards and total > 21:
        cards[cards.index(11)] = 1
        total = sum(cards)

    return total

your_cards = [draw_cards(), draw_cards()]
comp_cards = [draw_cards(), draw_cards()]

your_score = score_count(your_cards)
comp_score = score_count(comp_cards)

print("Your cards: ", your_cards, "Total: ", your_score)
print("Computer Cards: [", comp_cards[0], "X]")

while your_score < 21:
    draw = input("Do you want to draw a card? (y/n): ").lower()

    if draw == 'y':
        your_cards.append(draw_cards())
        your_score = score_count(your_cards)
        print("Your cards: ", your_cards, "Total: ", your_score)
    else:
        break

while comp_score < 17:
    comp_cards.append(draw_cards())
    comp_score = score_count(comp_cards)

print("\nFinal Hands:")
print("Your cards:", your_cards, "Total:", your_score)
print("Computer cards:", comp_cards, "Total:", comp_score)


if your_score > 21:
    print("You Lose! You went over 21.")
elif comp_score > 21:
    print("You Win! Computer went over 21.")
elif your_score > comp_score:
    print("You Win!")
elif your_score < comp_score:
    print("You Lose!")
else:
    print("It's a Draw!")