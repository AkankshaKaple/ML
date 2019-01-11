# 5. In my town, it's rainy one third of the days. Given that it is rainy, there will be heavy traffic with
# probability 1212, and given that it is not rainy, there will be heavy traffic with probability 1414.
# If it's rainy and there is heavy traffic, I arrive late for work with probability 1212. On the other hand,
# the probability of being late is reduced to 1818 if it is not rainy and there is no heavy traffic.
# In other situations (rainy and no traffic, not rainy and traffic) the probability of being late is 0.250.25.
# You pick a random day.
# Write a program to find following
# What is the probability that it's not raining and there is heavy traffic and I am not late?
# What is the probability that I am late?
# Given that I arrived late at work, what is the probability that it rained that day?


p_rain = 1/3
p_not_rain = 2/3
p_traffic_rain = 1/2
p_traffic_no_rain = 1/4
p_rain_tarffic_late = 1/2
p_not_rain_no_traffic_late = 1/8
p_rain_no_traffic_late = p_no_rain_traffic_late = 0.25

prob1 = p_not_rain * p_traffic_no_rain * (1-p_traffic_no_rain)
print(prob1)


prob2 = p_rain_tarffic_late + p_no_rain_traffic_late + p_rain_no_traffic_late + p_not_rain_no_traffic_late
print(prob2)

prob_rain_and_late = p_rain_no_traffic_late + p_rain_tarffic_late

prob3 = prob_rain_and_late / p_rain_tarffic_late
# print(prob_rain_and_late, "/", p_rain_tarffic_late)
print(prob3)
