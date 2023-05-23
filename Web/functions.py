FILEPATH = "files/todos.txt"


def get_todos(filepath=FILEPATH):  # parameter is filepath
    """ Reads a text file and returns list of to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_argument, filepath=FILEPATH):  # we have to have default parameter after non default
    """ Writes updated version of list with to-do items into a file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_argument)
    return None  # no need for return value, we simply write into file


def show_todos(todos_local):
    for local_index, local_item in enumerate(todos_local):
        local_item = local_item.strip('\n')
        local_row = f"{local_index + 1}. {local_item}"
        print(local_row)
    return


if __name__ == "__main__":  # __name__ == __main__ only when we run functions.py (this) directly.
    print(__name__)  # in 1.cli-todolist.py if we called print(__name__) of this file (would have to be outside if)
    print(get_todos())  # the name would be "functions" (above)
