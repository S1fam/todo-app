# Day 7 - stripping show of newlines between items, 3 methods described and commented in experiments
# Day 8 today we: use context manager to handle files better
# with open('../files/todos.txt', 'r') as file:


while True:
    # get user input and strip space characters from it. Input decides an action we take
    user_action = input("Type add, complete, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('../files/todos.txt', 'r') as file:  # you don't need to close file
                todos = file.readlines()

            todos.append(todo)  # appending list with user's added to-do

            with open('../files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            with open('../files/todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1}. {item}")

            number = int(input("Number of the todo to complete: "))
            number = number - 1
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            print(f"Todo \"{todo_to_remove}\" was removed from the list")

            with open('../files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('../files/todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}. {item}"
                print(row)

        case 'edit':
            with open('../files/todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1}. {item}")

            number = int(input("Number of the todo to edit: "))
            number = number - 1

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            print("Here are your new todos: ")
            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1}. {item}")

            with open('../files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'exit':
            break

print("Bye!")
