# Write a program to find the probability of drawing an ace after drawing a king on the first draw

number_of_kings = 4
total_cards = 52
probability_of_king = number_of_kings/total_cards
print("Probability of king = ", probability_of_king)
print("Now number of cards in deck = ", total_cards-1)
new_number_of_cards = total_cards-1
number_of_aces = 4
probability_of_ace = number_of_aces/new_number_of_cards
print("Probability of getting aces = ", number_of_aces, "/", new_number_of_cards, "=", probability_of_ace)