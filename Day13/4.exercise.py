# 1. Define a function that has two parameters, year_of_birth and current_year.
# The current_year parameter should be a default parameter with the current year as a default value.
# The function should calculate and return the age of the user given the year of birth and the current year.

def age_calculation(year_of_birth_local, current_year=2023):
    age_local = current_year - year_of_birth_local
    return age_local


year_of_birth = int(input("what is your year of birth?: "))
age = age_calculation(year_of_birth)
if age > 120:
    print(f"{age}.. Damn you old af")
else:
    print(age)


# 2. Your task for this exercise is to use the function you created in exercise 1. Then, below the function definition,
# get the year of birth from the user using an input function and then call
# and print the defined function to get the user's age as output. (done above)


# 3. Extend the program you wrote in exercise 2 by printing a message to the user instead of their age if
# their age is greater than 120. Feel free to print any message that you like. (done above)


# 4. Write a program that gets a list of names from the user and returns the number of names given.
# You are encouraged to use a function. Here is how the program would work:


def lenght_of_list(string):
    list_of_names = string.split(',')
    return len(list_of_names)


string_of_names = input("Enter names separated by commas (no spaces): ")
print(lenght_of_list(string_of_names))
