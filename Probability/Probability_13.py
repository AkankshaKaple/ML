# 13. The table below shows the height, x, in inches and the pulse rate, y, per minute,
# for 9 people. Write a program to find the correlation coefficient and interpret your result.
# 	x ⇒ 68 72 65 70 62 75 78 64 68
# 	y ⇒ 90 85 88 100 105 98 70 65 72

x = [68, 72, 65, 70, 62, 75, 78, 64, 68]
y = [90, 85, 88, 100, 105, 98, 70, 65, 72]
x_mul_y = []
sqr_x = []
sqr_y = []
sum_x = sum(x)
sum_y = sum(y)
n = 9

sum_xy = sum([x[item]*y[item] for item in range(len(x))])
sum_sqr_x = sum([x[item] * x[item] for item in range(len(x))])
sum_sqr_y = sum([y[item] * y[item] for item in range(len(y))])


r = (n * sum_xy - sum_x * sum_y) / ((n * sum_sqr_x - sum_x ** 2) * (n * sum_sqr_y - sum_y ** 2)) ** 0.5
print(r)