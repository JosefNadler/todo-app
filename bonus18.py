import FreeSimpleGUI as sg
import zip_extractor


sg.theme('Black')

label1 = sg.Text("Select archive: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse('Choose Archive', key='archive')

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('Choose Folder', key='folder')

exit_button = sg.Button('Exit', key='exit')
extract_button = sg.Button('Extract', key='extract')
output_label = sg.Text(key='output', text_color='yellow')

window = sg.Window('Archive Extractor', 
                    layout=[[label1, input1, choose_button1], 
                            [label2, input2, choose_button2], 
                            [exit_button, extract_button, output_label]], 
                    font=('Helvetica', 20))

while True:
    event, values = window.read()

    archivepath = values['archive']
    dest_dir = values['folder']
    
            
    if (event == sg.WINDOW_CLOSED) or (event == 'exit'):
        break

    try:
#        sg.tar_extract(archivepath, dest_dir)
        window['output'].update(value='Extracting...')
        zip_extractor.extract_archive(archivepath, dest_dir)
        window['output'].update(value='Extraction complete!')
    except:
        print("Error while extracting")


print('Bye')
window.close()  