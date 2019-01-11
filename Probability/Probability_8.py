def prob(l_mean, l_standard_deviation, l_n, l_x):
    z_score = (l_x - l_mean) / (l_standard_deviation * (l_n ** 0.5))
    return z_score


g_p = 0.1
g_n = 1000
g_mean = g_n * g_p
g_standard_deviation = (g_p * (1 - g_p))**0.5
g_x = 120


print(prob(g_mean, g_standard_deviation, g_n, g_x))
z = 1 - 0.9821
print("Probability = ", z)