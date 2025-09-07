"""
COMP.CS.100 Index Raises to Study Benefits
Creator: Ishan Malu
Student id number: 154138420
"""

#a)

benefit = float(input("Enter the amount of the study benefits: "))
index_raise = 1.17 / 100
new_benefit = benefit * (1 + index_raise)

print("If the index raise is 1.17 percent, the study benefit,")
print(f"after a raise, would be {new_benefit} euros")

#b)

first_raise = benefit * (1 + index_raise)
second_raise = first_raise * (1 + index_raise)

print("and if there was another index raise, the study")
print(f"benefits would be as much as {second_raise} euros")

