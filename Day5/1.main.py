# we want to show nuber of item when showing edit option to user, which i already did in day 4
# but today i will do it again using enumerate
# we are also adding complete feature, to remove the todos we have already done

todos = []

while True:
    user_action = input("Type add, complete, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'complete':
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")
            number = int(input("Number of the todo to complete: "))
            number = number - 1
            todos.pop(number)
        case 'show':
            for index, item in enumerate(todos):
                # print(index + 1,'.', item) --> 1 . item
                print(f"{index+1}. {item}")  # --> 1. item (formatovane retezce nam mohou pomoci s mezerami)
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
