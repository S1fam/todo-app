# Day 6 - commentary on reading files
# today we: update the breaks (empty newlines) between items of a list while showing it. (stripping '\n')
# experiments - commenting


while True:
    # get user input and strip space characters from it. Input decides an action we take
    user_action = input("Type add, complete, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('../files/todos.txt', 'r')  # reading list from a file
            todos = file.readlines()  # lines reads to a list -> 1. line will be 1. item
            file.close()

            todos.append(todo)  # appending list with user's added todo

            file = open('../files/todos.txt', 'w')
            file.writelines(todos)  # writes items of list as lines of file -> 1. item will be 1. line
            file.close()

        case 'complete':
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")
            number = int(input("Number of the todo to complete: "))
            number = number - 1
            todos.pop(number)

        case 'show':
            file = open('../files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # 1.
            # new_todos = []  --> for loop method
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            # 2.
            # new_todos = [item.strip('\n') for item in todos]  # list comprehension method
            # stores item.strip() in new_todos for each item in todos

            for index, item in enumerate(todos):
                item = item.strip('\n')  # 3. in the end this is the easiest solution
                row = f"{index + 1}. {item}"
                print(row)

        case 'edit':
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case 'exit':
            break

print("Bye!")
