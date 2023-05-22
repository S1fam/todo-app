import functions
import PySimpleGUI as Gui

label = Gui.Text("Type in a to-do")
input_box = Gui.InputText(tooltip="Enter todo", key="enter_todo")
add_button = Gui.Button("Add")
list_box = Gui.Listbox(tooltip="List of todos", values=functions.get_todos(),
                       key='todos_list', enable_events=True, size=(45, 10))
edit_button = Gui.Button("Edit")


window = Gui.Window('My To-Do App',
                    layout=[[label], [input_box, add_button],  # ...........79
                            [list_box, edit_button]],
                    font=('Helvetica', 20))

while True:
    button_pressed, values = window.read()
    print(1, button_pressed)
    print(2, values)
    print(3, values['todos_list'])
    match button_pressed:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["enter_todo"] + "\n")
            functions.write_todos(todos)
            window['todos_list'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos_list'][0]
            new_todo = values['enter_todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)
            window['todos_list'].update(values=todos)
        case 'todos_list':
            window['enter_todo'].update(value=values['todos_list'][0])
        case Gui.WINDOW_CLOSED:
            break

window.close()
