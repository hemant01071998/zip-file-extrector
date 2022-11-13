import PySimpleGUI as hp
from zip_extrector import  extract_archieve


hp.theme("black")
label1 = hp.Text("Select the zip file                ")
input1 = hp.Input()
choose1 = hp.FileBrowse("Choose",key="archive")

label2 = hp.Text("Select the destination folder ")
input2 = hp.Input()
choose2 = hp.FolderBrowse("Choose",key="folder")

extract_button = hp.Button("Extract")
output_level = hp.Text(key="output",text_color="green")

window = hp.Window("Zip File Extractor App",
                   layout=[[label1,input1,choose1],
                          [label2,input2,choose2],
                          [extract_button,output_level]])
while True:
    event , value  = window.read()
    print(event)
    print(value)
    archevepath = value["archive"]
    dest_path = value["folder"]
    extract_archieve(archevepath,dest_path)
    window['output'].update(value="File Extraction  successfully!!!")


window.close()