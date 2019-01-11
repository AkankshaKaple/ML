

def prob(l_mean, l_standard_deviation, l_n, l_x):
    z_score = (l_x - l_mean ) / (l_standard_deviation / (l_n ** 0.5))
    return z_score


g_mean = 23.1
g_standard_deviation = 3.1
g_n = 6
g_x = 27


print(prob(g_mean, g_standard_deviation, g_n, g_x))
print("Probability = 0.9989")