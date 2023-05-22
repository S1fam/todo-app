# 1. The program depicted below consists of two Python files. The program tries to count and print out the number of
# periods in the "Trees are good. Grass is green." . However, running the cli-todolist.py file returns an error. fix the error.

# import functions
#
# nr_of_periods = count("Trees are good. Grass is green.")
# print(nr_of_periods)

import functions

nr_of_periods = functions.count("Trees are good. Grass is green.")
print(nr_of_periods)


# 2. The same program as in exercise 1 now is throwing yet another error. Hunt the error down and fix it.

# import functions.py  --> we delete the .py
#
# nr_of_periods = functions.count("Trees are good. Grass is green.")
# print(nr_of_periods)

nr_of_periods = functions.count("Trees are good. Grass is green.")
print(nr_of_periods)


# 3. There is another error in the same program. Please fix the error.

# from functions import count
#
# nr_of_periods = functions.count("Trees are good. Grass is green.") --> no need to call functions.
# print(nr_of_periods)

from functions import count

nr_of_periods = count("Trees are good. Grass is green.")
print(nr_of_periods)
