# 10.  X is a normally normally distributed variable with mean μ = 30 and standard deviation σ = 4. Write
# a program to find
# a. P(x < 40)
# b. P(x > 21)
# c. P(30 < x < 35)

def probability(value):
    z_value = (value - mean) / variance
    return  z_value


mean = 30
variance = 4
x = 40
score = probability(x)
print("z-score of x < 40 = ", score)
print("Probability of Normal Distribution of x < 40 = 0.9938")

mean = 30
variance = 4
x = 21
score = probability(x)
print("z-score of x > 21  = ", score)
print("Probability of  Normal Distribution of x > 21 = 0.9878")

mean = 30
variance = 4
x = 35
score = probability(x)
print("z-score of 30 < x < 35 = ", score)
print("Probability of  Normal Distribution of 30 < x < 35 = 0.9878")


