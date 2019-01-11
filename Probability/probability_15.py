# 15. Let’s say that you are at work one day and have just finished lunch. You suddenly feel horrible and find yourself
# lying down and within a few minutes begin to panic. Wasn’t your friend at work recently sick with the flu? What if you
# have it? Will you have to cancel your big trip next week?
# You have a headache and sore throat, and you know that people with the flu have the same symptoms roughly 90% of the
# time. In other words, 90% of people with the flu have the same symptoms you currently have. Does this mean you have t
# he flu?

def probability_symptoms_given_flu(value1, value2, value3):
    probability = (value1 * value2) / value3
    return  probability


p_symptoms_given_flu = 0.9
p_symptoms = 0.2
p_no_symptoms = 0.8
p_flu = 0.05
print(probability_symptoms_given_flu(p_flu,p_symptoms_given_flu,p_symptoms))
