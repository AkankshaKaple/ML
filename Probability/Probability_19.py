# 19.In Orange County, 51% of the adults are males. (It doesn't take too much advanced mathematics to deduce that the other
# 49% are females.) One adult is randomly selected for a survey involving credit card usage. a. Find the prior probability
# that the selected person is a male. b. It is later learned that the selected survey subject was smoking a cigar. Also, 9.5%
# of males smoke cigars, whereas 1.7% of females smoke cigars (based on data from the Substance Abuse and Mental Health Services
# Administration). Use this additional information to find the probability that the selected subject is a male.


def probability_male_given_somker(value1, value2, value3,value4):
    probability = (value1 * value2) / (value1 * value2 + value3 * value4)
    return probability


p_male = 0.51
p_female = 0.49
p_smoker_given_male = (9.5*0.51)/100
p_smoker_given_female = (1.7*0.49)/100
print(probability_male_given_somker(p_male,p_smoker_given_male,p_female,p_smoker_given_female))