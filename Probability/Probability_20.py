# 20. An aircraft emergency locator transmitter (ELT) is a device designed to transmit a signal
# in the case of a crash. The Altigauge Manufacturing Company makes 80% of the ELTs,
# the Bryant Company makes 15% of them, and the Chartair Company makes the other
# 5%. The ELTs made by Altigauge have a 4% rate of defects, the Bryant ELTs have a 6%
# rate of defects, and the Chartair ELTs have a 9% rate of defects (which helps to explain
# why Chartair has the lowest market share).
# a. If an ELT is randomly selected from the general population of all ELTs, find the
# probability that it was made by the Altigauge Manufacturing Company.
# b. If a randomly selected ELT is then tested and is found to be defective, find the
# probability that it was made by the Altigauge Manufacturing Company.

def probability_symptoms_given_flu(value1, value2, value3, value4, value5, value6):
    total_probability = (value1 * value2)+ (value3*value4)+ (value5*value6)
    probability = (value1 * value2) / total_probability
    return  probability


p_AMC = 0.8
p_BC = 0.15
p_CC = 0.05
p_defect_given_AMC = 0.04
p_defect_given_BC = 0.06
p_defect_given_CC = 0.09
print(probability_symptoms_given_flu(p_AMC, p_defect_given_AMC, p_BC, p_defect_given_BC, p_CC, p_defect_given_CC))

