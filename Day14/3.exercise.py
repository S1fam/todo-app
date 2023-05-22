# 1. Create a function that finds out the state of water (i.e., gas, liquid, solid) given the temperature.
# In other words, the function has a temperature parameter and returns either "Gas", "Liquid" or "Solid" as a string
# depending on the temperature. The function should be written in a separate file from the command line interface file.

from waterstate import water_state

temperature = float(input("Enter water temperature: "))
print(water_state(temperature))

# 2. In coding exercise 1, we hardcoded the values 0 and 100. It is better to change them to constants
# in the script where the function is defined. Therefore, your task is to modify the script from exercise 1
# by creating two global variables/constants in that file, one variable associated with 0 and another
# associated with 100. Then, use those variables in the function instead of the values.
