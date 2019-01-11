mean = 50000
standard_deviation = 10000
total = 74000 + 11 * 47000
x = total - 20000
n = 11

z_score = (x - mean*n)/(standard_deviation * n**0.5)
print(z_score)
z = 1 - 0.7357
print("Probability = ", z)


z_score = 2.575

x = (z_score * n**0.5 * 10000) + n * mean
print(x)

total = (x - 54000) / n

print(total)