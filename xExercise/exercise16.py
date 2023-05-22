import PySimpleGUI as Gui

label_feet = Gui.Text("Enter feet: ")
input_feet = Gui.Input(tooltip="enter feet")

label_inches = Gui.Text("Enter inches: ")
input_inches = Gui.Input(tooltip="enter inches")

convert_button = Gui.Button("Convert")

window = Gui.Window('Convertor', layout=[[label_feet, input_feet],
                                         [label_inches, input_inches],
                                         [convert_button]])

window.read()
window.close()
