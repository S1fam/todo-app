import PySimpleGUI as Gui

label1 = Gui.Text("Select files to compress")
label2 = Gui.Text("Select destination folder")

input_box1 = Gui.InputText(tooltip="choose files to compress")
input_box2 = Gui.InputText(tooltip="choose destination folder")

button1 = Gui.FilesBrowse("Choose")
button2 = Gui.FolderBrowse("Choose")
button3 = Gui.Button("Compress")

window = Gui.Window('File Zipper', layout=[[label1, input_box1, button1],
                                           [label2, input_box2, button2],
                                           [button3]])
window.read()
window.close()
