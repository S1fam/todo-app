import functions

import PySimpleGUI as Gui

label = Gui.Text("Type in a to-do")
input_box = Gui.InputText(tooltip="Enter todo")
add_button = Gui.Button("Add")


window = Gui.Window('My To-Do App', layout=[[label], [input_box, add_button]])
# method that creates a window, we store it in var, we put input box and button on same line (comment bellow)
# layout expects a list putting label and input box into square brackets alone makes both thing apprear on their line
window.read()  # displays the window on the screen
window.close()
