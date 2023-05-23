import functions
import PySimpleGUI as Gui
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

Gui.theme("DarkPurple4")

clock = Gui.Text('', key='clock')
label = Gui.Text("Type in a to-do")
input_box = Gui.InputText(tooltip="Enter todo", key="enter_todo")
add_button = Gui.Button("Add")
list_box = Gui.Listbox(tooltip="List of todos", values=functions.get_todos(),
                       key='todos_list', enable_events=True, size=(45, 10))

edit_button = Gui.Button("Edit")
complete_button = Gui.Button("Complete")
exit_button = Gui.Button("Exit")


window = Gui.Window('My To-Do App',
                    layout=[[clock],
                            [label], [input_box, add_button],  # ...........79
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 12))

while True:
    button_pressed, values = window.read(timeout=1000)
    window['clock'].update(value=time.strftime("%d.%m.%Y - %H:%M:%S"))
    match button_pressed:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['enter_todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos_list'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos_list'][0]
                new_todo = values['enter_todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos_list'].update(values=todos)
            except IndexError:
                Gui.popup("Please select an item", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values['todos_list'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos_list'].update(values=todos)
                window['enter_todo'].update(value="")
            except IndexError:
                Gui.popup("You have virus in your computer", font=("Helvetica", 20))

        case "Exit":
            break

        case 'todos_list':
            window['enter_todo'].update(value=values['todos_list'][0])

        case Gui.WINDOW_CLOSED:
            break

window.close()
