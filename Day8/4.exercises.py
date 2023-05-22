# 1. A client wants to buy a coin-flip probability program from you. The programs should work like this:
# 1. The user runs the program. The program asks the user to enter "head" or "tail".
# The user flips a coin on their desk, table, floor, etc., and then enters "head" or "tail".
# The user does the same over and over again.

# In each cycle, the program should return the current percentage of coinflip in the program,
# similar to what you see in the screenshot above. Also, you should write each user entry
# (i.e., head or tail) in a text file using a with-context manager, one entry per line.

with open(f"files/coinflip/amount_of_sessions.txt") as file:
    amount_of_sessions = file.readlines()  # amount starts with 0 ['0', '1',..] -> ['01', '1',..] it works
    amount_in_ints = [int(number) for number in amount_of_sessions]
current_index = sum(amount_in_ints)

with open(f"files/coinflip/session{current_index}.txt", "w") as file:
    file.write('')

with open(f"files/coinflip/count_of_session{current_index}.txt", "w") as file:
    file.write('')

while True:
    user_choice = input("Throw the coin and enter head or tail here (0 for exit): ").strip()

    match user_choice:

        case 'head':
            with open(f"files/coinflip/session{current_index}.txt") as file:
                flipped_sides = file.readlines()

            flipped_sides.append(user_choice + '\n')

            with open(f"files/coinflip/session{current_index}.txt", "w") as file:
                file.writelines(flipped_sides)

            # here we will write 1 for heads, make sum of 1's and 0's and devide by amount of items (get % of heads)
            with open(f"files/coinflip/count_of_session{current_index}.txt") as file:
                numbers = file.readlines()

            numbers.append('1' + '\n')
            with open(f"files/coinflip/count_of_session{current_index}.txt", "w") as file:
                file.writelines(numbers)

            # after we are done working with files (appending heads to one file and number 1 to another) we count! UwU
            numbers_in_ints = [int(number) for number in numbers]
            sum_of_numbers = sum(numbers_in_ints)
            chance_in_percent = (sum_of_numbers / len(numbers_in_ints)) * 100

            print(f"Heads: {chance_in_percent}%")

        case 'tail':
            with open(f"files/coinflip/session{current_index}.txt") as file:
                flipped_sides = file.readlines()

            flipped_sides.append(user_choice + '\n')

            with open(f"files/coinflip/session{current_index}.txt", "w") as file:
                file.writelines(flipped_sides)

            # here we will write 0 for tails, make sum of 1's and 0's and devide by amount of items (get % of heads)
            with open(f"files/coinflip/count_of_session{current_index}.txt") as file:
                numbers = file.readlines()

            numbers.append('0' + '\n')
            with open(f"files/coinflip/count_of_session{current_index}.txt", "w") as file:
                file.writelines(numbers)

            # after we are done working with files (appending heads to one file and number 1 to another) we count! UwU
            numbers_in_ints = [int(number) for number in numbers]
            sum_of_numbers = sum(numbers_in_ints)
            chance_in_percent = (sum_of_numbers / len(numbers_in_ints)) * 100

            print(f"Heads: {chance_in_percent}%")

        case '_':
            pass

        case '0':
            break


amount_of_sessions.append('1' + '\n')
with open(f"files/coinflip/amount_of_sessions.txt", 'w') as file:
    file.writelines(amount_of_sessions)

print("thanks for playing current session :)")


# mockup: next version will create new file for every game so that it can be later analyzed
# using third file that counts games by simply adding line to a file every time the program is executed
# then we name files with formated indexes f"files/coinflip/session{index}.txt"
# we create new empty file at the end f"files/coinflip/session{index + 1}.txt
# i guess, it does sound complicated but ich want to do it hihi
# mockup delievered

# mockup 2: we will add recap messages to end of files
# how?: well we will count occurances of 1's and 0's in count_of_session, write in number amount of occurances
# and also percentage of heads, we will write it into both files actually, both things in both files on the end
# so decoding it becomes harder. But we will create .._raw files that will store original data without recap
# so the games are both with commented recap and without the commented one, ggs. There goes my work for tomorrow?

# mockup 3: refactor this app to a desktop application, somehow (a long shot, didn't get there in the course yet)
