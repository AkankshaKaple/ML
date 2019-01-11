# You toss a fair coin three times write a program to find following:
# What is the probability of three heads, HHHHHH?
# What is the probability that you observe exactly one heads?
# Given that you have observed at least one heads, what is the probability that you observe at least two heads?

sample_set = ["HHH", "HHT", "HTH", "THH", "THT", "TTH","TTT", "HTT"]
total_possible_events = len(sample_set)
required_event = [event for event in range(total_possible_events) if sample_set[event] == "HHH"]
# required_event = [event for event in range(total_possible_events) if "HHH" in sample_set]

# number_of_required_events = len(required_event)
# print(len(required_event))
# probability = number_of_required_events / total_possible_events
# print("probability of three heads = ",number_of_required_events, '/', total_possible_events, "=", probability)
#
# exactly_one_head = [event for event in range(total_possible_events) if sample_set[event].count("H") == 1]
# event = len(exactly_one_head)
# probability_of_one_head = event / total_possible_events
# print("probability of exactly one heads = ",event, '/', total_possible_events, "=", probability)

required_event1 = [sample_set[event] for event in range(total_possible_events) if sample_set[event].count("H") >= 1]
# print(required_event2)
event1 = set()
# a |= set(l)
event1 |= set(required_event1)
print(event1)
# event1 = len(required_event2)

required_event2 = [required_event1[item] for item in range(len(required_event1)) if required_event1[item].count("H") >= 2]
event2 = set()
event2 |= set(required_event2)
print(event2)

event1_and_event2 = event1 & event2
print(event1_and_event2)

probability_of_event1_and_event2 =  len(event1_and_event2) / len(sample_set)
print("probability_of_event1_and_event2", len(event1_and_event2), "/", len(sample_set), " = ", probability_of_event1_and_event2)
probability_of_event2 = len(event1) / len(sample_set)
print("probability_of_event2 = ", len(event1) , " / " , len(sample_set), " = ", probability_of_event2)


total_probability = probability_of_event1_and_event2 / probability_of_event2
print(total_probability)