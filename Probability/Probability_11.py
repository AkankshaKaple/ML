# 11. A radar unit is used to measure speeds of cars on a motorway. The speeds are normally distributed with
# a mean of 90 km/hr and a standard deviation of 10 km/hr. Write a program to find the probability that a car
# picked at random is travelling at more than 100 km/hr?

mean = 90
Standard_Deviation = 10
Normal_Distribution = 100

speed = (Normal_Distribution - mean) / Standard_Deviation
print("z-score of speed greater than 100 = ", speed)
print("Probability of Normal Distribution of speed greater than 100  = 0.8413")