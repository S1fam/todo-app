import PySimpleGUI as Gui

Gui.theme("Black")

label_archive = Gui.Text("Select archive: ")
label_destination = Gui.Text("Select destination: ")

archive_input = Gui.InputText(tooltip="choose archive")
destination_input = Gui.InputText(tooltip="choose destination")

choose_button1 = Gui.FileBrowse("Choose", key="archive")  # only one zip file
choose_button2 = Gui.FolderBrowse("Choose", key="destination")
extract_button = Gui.Button("Extract")

output_label = Gui.Text("", key="output", text_color="red")

window = Gui.Window('File Zipper', layout=[[label_archive, archive_input, choose_button1],
                                           [label_destination, destination_input, choose_button2],
                                           [extract_button, output_label]],
                    font=('Helvetica', 20))

window.read()
