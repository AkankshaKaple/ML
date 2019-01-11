# 23. A diagnostic test has a probability 0.95 of giving a positive result when applied to a person suffering
# from a certain disease, and a probability 0.10 of giving a (false) positive when applied to a non-sufferer. It is
# estimated that 0.5 % of the population are sufferers. Suppose that the test is now administered to a person about
# whom we have no relevant information relating to the disease (apart from the fact that he/she comes from this
# population). Calculate the following probabilities:
# (a) that the test result will be positive;
# (b) that, given a positive result, the person is a sufferer;
# (c) that, given a negative result, the person is a non-sufferer;
# (d) that the person will be misclassified.


p_positive_given_suffering = 0.95
p_negative_given_suffering = 0.10
p_positive_given_not_suffering = 0.9
p_negative_given_not_suffering = 0.05
p_suffering = 0.5
p_not_suffering = 0.5

p_positive = p_suffering * p_positive_given_suffering + p_not_suffering * p_positive_given_not_suffering
print(p_positive)
p_negative = p_suffering * p_negative_given_suffering + p_not_suffering * p_negative_given_not_suffering
p_suffering_given_positive = (p_suffering * p_positive_given_suffering)/p_positive
print(p_suffering_given_positive)
p_not_suffering_given_negative = (p_not_suffering * p_negative_given_not_suffering)/p_negative
print(p_not_suffering_given_negative)
p_misclassified = (p_not_suffering * p_positive_given_not_suffering) + (p_not_suffering * p_negative_given_not_suffering)
print(p_misclassified)