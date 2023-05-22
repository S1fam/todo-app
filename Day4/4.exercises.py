# 1.

dollars = int(input("Input a dolar amount in numbers: "))

euros = dollars * 0.95
print("the amount in euros is:", euros)


# 2.

ranking = ['John', 'Sen', 'Lisa']
show_rank = int(input("what placing do you want to see?: ")) - 1

print(ranking[show_rank])

# 3.

person = input("Enter a name of a competitor: ")
print(person, "ended in", ranking.index(person) + 1, ". place")
