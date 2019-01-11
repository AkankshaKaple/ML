# 14. The patients were tested thrice before the oncologist concluded that they had cancer.
# The general belief is that 1.48 out of a 1000 people have breast cancer in the US at that particular time
# when this test was conducted. The patients were tested over multiple tests. Three sets of test were done
# and the patient was only diagnosed with cancer if she tested positive in all three of them.True positive Rate –
# 93% True negative Rate – 99%


def probability_of_positive_given_cancer(value1, value2, value3, value4):
    total_probability = value1 * value2 + value3 * value4
    probability = (value1 * value2) / total_probability
    return probability


p_cancer = 1.48 / 1000
p_not_cancer = 1 - p_cancer
p_cancer_given_positive = 0.93
p_not_cancer_given_positive = 0.99
print(probability_of_positive_given_cancer(p_cancer,p_cancer_given_positive,p_not_cancer,p_not_cancer_given_positive))