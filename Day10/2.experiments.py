# Day 9: we used if/elif/else statements, to better up the program also we added list slicing
# Day 10: fixing two bugs: no newlines, having name of operation inside added todos (list slicing solution at day 9)
# today we will use user_action.startswith() string method
# also we do error handling. There are two types of errors (syntax and exceptions), today we focus on exceptions

while True:
    # get user input and strip space characters from it. Input decides an action we take
    user_action = input("Type add, complete, show, edit or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):  # if the 'add' is first in the inputed string
        todo = user_action[4::] + '\n'

        with open('../files/todos.txt', 'r') as file:  # you don't need to close file
            todos = file.readlines()

        todos.append(todo)  # appending list with user's added todo

        with open('../files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('complete'):
        try:
            try:
                with open('../files/todos.txt', 'r') as file:
                    todos = file.readlines()

                for index, item in enumerate(todos):
                    item = item.strip('\n')
                    print(f"{index + 1}. {item}")

                number = int(user_action[9:])
                index = number - 1

                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)
                print(f"Todo \"{todo_to_remove}\" was removed from the list")

                with open('../files/todos.txt', 'w') as file:
                    file.writelines(todos)
            except IndexError:
                print("There is no item with that number")
                continue
        except ValueError:
            print("Wrong value (none or characters)")
            continue

    elif user_action.startswith('show'):
        with open('../files/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:  # we try this part of code, if we get value error (user inputs letters instead of numbers) we go except
            with open('../files/todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1}. {item}")

            number = int(input("Number of the todo to edit: "))
            number = number - 1

            counter = 0
            for item in todos:
                counter += 1

            if 0 <= number < counter:
                print(f"editing: {todos[number]}")
                new_todo = input("Enter new todo: ")
                todos[number] = new_todo + "\n"

                print("Here are your new todos: ")
                for index, item in enumerate(todos):
                    item = item.strip('\n')
                    print(f"{index + 1}. {item}")

                with open('../files/todos.txt', 'w') as file:
                    file.writelines(todos)
            else:
                print("\ninvalid number of item\n")
        except ValueError:
            print("your command is not valid")
            continue  # goes back to beginning of the while loop

    elif user_action.startswith('exit'):
        break

    else:
        print("try working command")

print("Bye!")
