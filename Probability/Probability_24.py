# 24. : Imagine that you	have three urns that you cannot see	into. Urn1 is 90%  green balls	and	10% red. Urn2	is
# 50%	green and 50% blue. Urn3 is	20% green, 40% red,	and	40%	blue.	You	can’t	tell	which	urn	is	which.	You
# randomly	select	an	urn	and	 then	randomly	select	a	ball	from	it.	The	ball	you	drew	is	green.
# What	is	the	 probability	that	it	came	from	urn1?

p_urn1 = p_urn2 = p_urn3 = 1/3
p_green_given_urn1 = 0.9
p_red_given_urn1 = 0.5
p_green_given_urn2 = 0.1
p_blue_given_urn2 = 0.5

p_green_given_urn3 = 0.2
p_red_given_urn3 = 0.4
p_blue_given_urn3 = 0.4

total_probability = (p_urn1 * p_green_given_urn1) + (p_urn2 * p_green_given_urn2)+ (p_urn3 * p_green_given_urn3)
p_urn1_given_green = (p_urn1 * p_green_given_urn1)/total_probability
print(p_urn1_given_green)