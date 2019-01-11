p_red = p_blue = 0.5
p_no_win_given_red = 0.8
p_no_win_given_blue = 0.9
p_win_given_red = 1 - p_no_win_given_red
p_win_given_blue = 1 - p_no_win_given_blue

p_red_given_no_win = (p_no_win_given_red * p_red) / (p_no_win_given_red * p_red + p_no_win_given_blue * p_blue)
p_red_given_win =  (p_win_given_red * p_red) / (p_win_given_red * p_red + p_win_given_blue * p_blue)

print(p_red_given_no_win)
print(p_red_given_win)







