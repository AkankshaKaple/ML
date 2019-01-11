def prob(l_standard_deviation, l_n, l_x1, l_x2, l_p):
    z_score1 = (l_x1 - l_n * l_p) / l_standard_deviation
    z_score2 = (l_x2 - l_n * l_p) / l_standard_deviation
    return z_score1,z_score2


g_n = 400
g_p = 0.06
g_standard_deviation = (g_n*g_p*(1 - g_p))**0.5
g_mean = g_n * g_p
g_x1 = 20-0.5
g_x2 = 25+0.5
print(prob(g_mean, g_standard_deviation, g_n, g_x1, g_x2, g_p))
z = 0.6217 - 0.1736
print("Probability = ", z)

g_n = 40
g_p = z
g_standard_deviation = (g_n*g_p*(1 - g_p))**0.5
g_mean = g_n * g_p
g_x1 = 8-0.5
print(prob(g_standard_deviation, g_n, g_x1, g_x2, g_p))
z = 0.9918 - 0.0005
print("Probability = ", z)