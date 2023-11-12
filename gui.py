import PySimpleGUI as sg
import converter

sg.theme('DarkBlue')


def convert_file(selected_file):
    file = open(selected_file)
    file_name = file.name
    file_no_ext = file_name[:-4]
    try:
        converter.pdfToMp3(selected_file, file_name)
        sg.popup(f'Conversion complete! File saved as {file_no_ext}.mp3')
    except:
        sg.popup('Something went wrong. Please check the logs')


def main():
    # Define the layout of the GUI
    layout = [
        [sg.Text("Select a pdf to convert:")],
        [sg.Input(key="file_path", enable_events=True,
                  size=(45, 1)),
         sg.FilesBrowse(file_types=(("PDF Files", "*.pdf"))),
         sg.Button("Convert")]
    ]

    # Create the window
    window = sg.Window("File Browser", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            break

        if event == "Convert":
            selected_file = values["file_path"]

            if selected_file:
                convert_file(selected_file)
            else:
                sg.popup("You need to select a PDF first")

    window.close()


if __name__ == "__main__":
    main()
