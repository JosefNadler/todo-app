import FreeSimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse('Choose Files', key='-files-', file_types=(("Text Files", "*.txt"), ("All Files", "*.*")))


label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('Choose Folder', key='-folder-')

compress_button = sg.Button('Compress', key='-compress-')
label3 = sg.Text("Compression in progress...", text_color='yellow')

window = sg.Window('FileZipper', layout=[[label1, input1, choose_button1], [label2, input2, choose_button2], [compress_button, label3]])   

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values['-files-'].split(';')
    folder = values['-folder-']
    make_archive(filepaths, folder)
    label3.update("Compression complete!")

    if event == sg.WINDOW_CLOSED:
        break


