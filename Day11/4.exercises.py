# 1. The code below is incomplete. It should calculate and print out the maximum value of the grades list.
# Please complete the function and then call it.

# def get_max():
#     grades = [9.6, 9.2, 9.7]
# The output of your code should be: 9.7

def get_max():
    grades = [9.6, 9.2, 9.7]
    return max(grades)


print(get_max())


# 2. The function we wrote in exercise 1 returned 9.7.  Change the function so this time it returns Max: 9.7,
# Min: 9.2 where 9.7 is the maximum and 9.2 is the minimum.

def get_extremes():
    grades = [9.6, 9.2, 9.7]
    minimium = min(grades)
    maximum = max(grades)
    return {"min": minimium, "max": maximum}


print(get_extremes())
