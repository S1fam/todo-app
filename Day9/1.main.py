# Day 8 we: used context manager to handle files better
# Day 9: we use if/elif/else statements, to better up the program
# adding a todos right after add. we change match for i statements
# tip: select multiple lines of code and press tab/shift+tab to indent or unindent multiple lines of code

while True:
    # get user input and strip space characters from it. Input decides an action we take
    user_action = input("Type add, complete, show, edit or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action[0:3]:  # if the 'add' is first in the inputed string
        todo = user_action[4::] + '\n'

        with open('../files/todos.txt', 'r') as file:  # you don't need to close file
            todos = file.readlines()

        todos.append(todo)  # appending list with user's added todo

        with open('../files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action[0:8]:
        with open('../files/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item}")

        number = int(input("Number of the todo to complete: "))
        number = number - 1

        counter = 0
        for item in todos:
            counter += 1

        if 0 <= number < counter:
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            print(f"Todo \"{todo_to_remove}\" was removed from the list")

            with open('../files/todos.txt', 'w') as file:
                file.writelines(todos)
        else:
            print("\ninvalid number of item\n")

    elif 'show' in user_action[0:4]:
        with open('../files/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif 'edit' in user_action[0:4]:
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

    elif 'exit' == user_action[0:4]:
        break

    else:
        print("try working command")

print("Bye!")
