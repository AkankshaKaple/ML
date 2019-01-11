# 6. Given the following statistics, write a program to find the probability that a woman has cancer if she
# has a positive mammogram result?
# 		a. One percent of women over 50 have breast cancer.
# 		b. Ninety percent of women who have breast cancer test positive on mammograms.
# 		c. Eight percent of women will have false positives.

p_cancer = 0.01
p_positive_MMG_give_cancer = 0.9
p_no_cancer = 0.99
p_positive_MMG_no_cancer = 0.08

total_probability = p_cancer * p_positive_MMG_give_cancer + p_no_cancer * p_positive_MMG_no_cancer
probability_cancer_given_positive_MMG = (p_cancer * p_positive_MMG_give_cancer) / total_probability

print(probability_cancer_given_positive_MMG)

