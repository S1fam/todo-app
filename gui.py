import functions
import PySimpleGUI as Gui

label = Gui.Text("Type in a to-do")
input_box = Gui.InputText(tooltip="Enter todo", key="todo")
add_button = Gui.Button("Add")


window = Gui.Window('My To-Do App',
                    layout=[[label], [input_box, add_button]],  # ..........79
                    font=('Helvetica', 20))

while True:
    button_pressed, values = window.read()
    print(button_pressed)
    print(values)
    match button_pressed:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.write_todos(todos)
        case Gui.WINDOW_CLOSED:
            break

window.close()
