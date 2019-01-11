# 21. HIV The New York State Health Department reports a 10% rate of the HIV virus
# for the “at-risk” population. Under certain conditions, a preliminary screening test
# for the HIV virus is correct 95% of the time. (Subjects are not told that they are
# HIV infected until additional tests verify the results.) If someone is randomly
# selected from the at-risk population, what is the probability that they have the
# HIV virus if it is known that they have tested positive in the initial screening?


def probability_HIV_given_positive(value1, value2, value3,value4):
    probability = (value1 * value2) / (value1 * value2 + value3 * value4)
    return probability

p_HIV = 0.1
p_no_HIV = 0.9
p_pisotive_given_HIV = 0.95
p_negative_given_HIV = 0.05
print(probability_HIV_given_positive(p_HIV, p_pisotive_given_HIV, p_no_HIV, p_negative_given_HIV))