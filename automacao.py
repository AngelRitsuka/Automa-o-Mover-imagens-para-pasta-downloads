import os
import shutil

from_dir = "C:/Users/angel/Downloads"
to_dir= "C:/Users/angel/OneDrive - Angelica Data Scientist/PERSONAL/Área de Trabalho"



list_of_files = os.listdir(from_dir)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in ['.gif', '.jpeg', '.png', '.jfif']:
        path1 = from_dir + '/' + 'Image_File'
        path2 = from_dir + '/' + 'Image_Files'
        path3 = from_dir + '/' + 'Image_Files' + '/'+ file_name

        if os.path.exists(path2):
            print("Movendo" + file_name + "..........")

            #da origem para o destino
            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("Movendo" + file_name + ".......")
            shutil.move(path1, path3)