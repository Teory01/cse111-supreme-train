#Copyright 2020, Brigham Young University-Idaho. All rights reserved.

""""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

#users name

user_name = "Teo"

#output 

print("Hello, " + user_name + "!")
#get user input
#users age
text = input("Please enter your age: ")

#convert string to integer

age = int(text)

#calculate the slowest and fastest rate

max_rate = 220 - age

slowest_rate = 0.65 * max_rate
fastest_rate = 0.85 * max_rate

#output

print("When you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {slowest_rate:.0f} and {fastest_rate:.0f}")
print("beats per minute.")
