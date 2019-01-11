# 22. In a TV Game show, a contestant selects one of three doors; behind one of the doors there is a prize, and behind
# the other two there are no prizes. After the contestant selects a door, the game-show host opens one of the remaining
# doors, and reveals that there is no prize behind it. The host then asks the contestant whether they want to SWITCH their
# choice to the other unopened door, or STICK to their original choice. Is it probabilistically advantageous for the contestant
# to SWITCH doors, or is the probability of winning the prize the same whether they STICK or SWITCH? (Assume that the host
# selects a door to open, from those available, with equal probability).


p_d1 = p_d2 = p_d3 = 1/3
p_open_d3_given_car_d2 = 1
p_open_d3_given_car_d3 = 0

p_car = 1/2
p_car_d3_given_open_in_d1 = 1/2
p_car_d3_given_open_in_d2 = 1

p_open_d1_given_car_d3 = ( p_car_d3_given_open_in_d1 * p_d1 ) / p_car
p_open_d2_given_car_d3 = ( p_car_d3_given_open_in_d2 * p_d2 ) / p_car

print("If don't switch, probability of winning : ", p_open_d1_given_car_d3)
print("If switch, probability of winning : ", p_open_d2_given_car_d3)