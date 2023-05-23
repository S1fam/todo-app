import PySimpleGUI as Gui
import extractor

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

while True:
    try:
        event, values = window.read()
        print(event, values)
        archive = values["archive"]
        destination = values["destination"]
        extractor.extract_zip_file(zip_path=archive, extract_path=destination)
        window["output"].update(value="extraction completed!")
    except TypeError:
        break
    except AttributeError:
        break
    except FileNotFoundError:
        Gui.popup("Please select an item", font=("Helvetica", 20))

window.close()
