import PySimpleGUI as Gui
from zipcreator import make_archive


label1 = Gui.Text("Select files to compress")
label2 = Gui.Text("Select destination folder")

input_box1 = Gui.InputText(tooltip="choose files to compress")
input_box2 = Gui.InputText(tooltip="choose destination folder")

choose_button1 = Gui.FilesBrowse("Choose", key="files")
choose_button2 = Gui.FolderBrowse("Choose", key="destination")

compress_button = Gui.Button("Compress")
output_label = Gui.Text("", key="output", text_color="red")

window = Gui.Window('File Zipper', layout=[[label1, input_box1, choose_button1],
                                           [label2, input_box2, choose_button2],
                                           [compress_button, output_label]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")  # returns a list
    destination = values["destination"]
    make_archive(filepaths, destination)
    window["output"].update(value="Compression completed!")


window.close()
