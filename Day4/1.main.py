
todos = []


while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':

            x = 1
            for item in todos:
                print(x, item)
                x += 1

            number = input("Number of the todo to edit: ")
            number = int(number) - 1

            existing_todo = todos[int(number)]
            print("editing: ", existing_todo)

            todos[number] = input("new item of a list:")

        case 'exit':
            break


print("Bye!")

