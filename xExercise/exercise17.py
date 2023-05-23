import convertor
import PySimpleGUI as Gui

Gui.theme("Black")

label_feet = Gui.Text("Enter feet:")
input_feet = Gui.InputText(tooltip="Enter todo", key="enter_feet")

label_inches = Gui.Text("Enter inches:")
input_inches = Gui.InputText(tooltip="Enter todo", key="enter_inches")

convert_button = Gui.Button("Convert")
exit_button = Gui.Button("Exit")

output_label = Gui.Text("", key="output")

window = Gui.Window('Convertor', layout=[[label_feet, input_feet],
                                         [label_inches, input_inches],
                                         [convert_button, exit_button, output_label]],
                    font=('Helvetica', 20))

while True:
    try:
        event, value = window.read()
        if event == "Exit":
            break
        print(event, value)
        if value["enter_feet"] == '':
            value["enter_feet"] = 0
        if value["enter_inches"] == '':
            value["enter_inches"] = 0

        result = round(convertor.convert(float(value["enter_feet"]),
                                         float(value["enter_inches"])), 4)
        window["output"].update(value=f"{result} meters")
    except TypeError:
        break
    except ValueError:
        Gui.popup("Enter valid value")

window.close()
