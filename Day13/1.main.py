# Day12: we added arguments to our functions to optimize code even further
# Day13: we add default parameters to functions, doc-strings (documentation strings)

def get_todos(filepath='../files/todos.txt'):  # parameter is filepath
    """ Reads a text file and returns list of to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_argument, filepath='../files/todos.txt'):  # we have to have default parameter after non default
    """ Writes updated version of list with to-do items into a file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_argument)
    return None  # no need for return value, we simply write into file


def show_todos():
    for local_index, local_item in enumerate(todos):
        local_item = local_item.strip('\n')
        local_row = f"{local_index + 1}. {local_item}"
        print(local_row)
    return


while True:
    # get user input and strip space characters from it. Input decides an action we take
    user_action = input("Type add, complete, show, edit or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):  # if the 'add' is first in the inputed string
        todo = user_action[4::]

        todos = get_todos()  # we have specified file as default parameter, if we wanted different file, we use arg here

        todos.append(todo + '\n')  # appending list with new action

        write_todos(filepath='../files/todos.txt', todos_argument=todos)  # this way we don't have to respect args order

    elif user_action.startswith('complete'):
        try:
            try:
                todos = get_todos()

                number = int(user_action[9:])
                index = number - 1

                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)
                print(f"Todo \"{todo_to_remove}\" was removed from the list, new list:")

                show_todos()

                write_todos(todos)

            except IndexError:
                print("There is no item with that number")
                continue
        except ValueError:
            print("Wrong value (none or characters)")
            continue

    elif user_action.startswith('show'):
        todos = get_todos()

        show_todos()

    elif user_action.startswith('edit'):
        try:  # we try this part of code, if we get value error (user inputs letters instead of numbers) we go except
            todos = get_todos()

            show_todos()

            number = int(input("Number of the todo to edit: "))
            number = number - 1

            counter = 0
            for item in todos:
                counter += 1

            if 0 <= number < counter:
                print(f"editing: {todos[number]}")
                new_todo = input("Enter new todo: ")
                todos[number] = new_todo + "\n"

                show_todos()

                write_todos(todos)

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
