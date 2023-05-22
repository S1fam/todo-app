# create function that gets numbers from file and calculate average

def get_average():
    with open("files/data.txt") as file:
        data = file.readlines()
    values = data[1:]  # intermediate variable
    values = [float(i) for i in values]
    average_local = sum(values) / len(values)
    return average_local


# my solution
# average = get_average()
# for index, item in enumerate(average):
#     item.strip('\n')
#     average[index] = int(item)
#
# average = sum(average) / len(average)
# print(average)

average = get_average()
print(average)
