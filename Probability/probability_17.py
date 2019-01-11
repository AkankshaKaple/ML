# 17. You go to see the doctor about an ingrowing toenail. The doctor selects you at random to have
# a blood test for swine flu, which for the purposes of this exercise we will say is currently suspected
# to affect 1 in 10,000 people in Australia. The test is 99% accurate, in the sense that the probability
# of a false positive is 1%. The probability of a false negative is zero. You test positive. What is the
# new probability that you have swine flu?
# Now imagine that you went to a friend’s wedding in Mexico recently, and (for the purposes of this
# exercise) it is know that 1 in 200 people who visited Mexico recently come back with swine flu.
# Given the same test result as above, what should your revised estimate be for the probability you
# have the disease?


p_flu = 1/10000
p_no_flu = 1 - p_flu
p_positive_given_flu = 1
p_positive_given_no_flu = 0.01

p_flu_given_positive__for_one_from_ten_thousand = (p_flu * p_positive_given_flu) / \
                                                  (p_flu * p_positive_given_flu + p_no_flu * p_positive_given_no_flu)

print(p_flu_given_positive__for_one_from_ten_thousand)
p_flu = 1/200
p_no_flu = 1 - p_flu
p_positive_given_flu = 1
p_flu_given_positive_for_one_person = (p_flu * p_positive_given_flu) / \
                                                  (p_flu * p_positive_given_flu + p_no_flu * p_positive_given_no_flu)

print(p_flu_given_positive_for_one_person)