# Write a program to find the probability of drawing an ace after drawing an ace on the first draw


number_of_aces = 4
total_cards = 52
prbability_of_getting_aces = number_of_aces / total_cards
print("Probability of getting an ace in deck of 52 cards is = ", prbability_of_getting_aces)

print("Now number of aces = ", number_of_aces-1)
new_number_of_aces = number_of_aces-1
new_total_cards = total_cards-1

probability = new_number_of_aces / new_total_cards

print("Probability of getting ace after drawing an ace = ", new_number_of_aces , '/', new_total_cards, "=", probability)