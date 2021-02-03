import os
import shutil

def get_folder_name(name):
    known_file_extensions = {".blend" : "BLENDER",
                             ".ma" : "MAYA ASCII",
                             ".mb" : "MAYA BINARY",
                             ".ai" : "ADOBE ILLUSTRATOR",
                             ".dmx" : "SOURCE FILMMAKER",
                             ".veg" : "SONY VEGAS",
                             ".bak" : "SONY VEGAS",
                             ".py" : "PYTHON",
                             ".rar" : "ARCHIVES",
                             ".zip" : "ARCHIVES",
                             ".7z" : "ARCHIVES",
                             ".rtf" : "DOCUMENTS",
                             ".mid" : "MIDI FILES",
                             ".flp" : "FRUITY LOOPS",
                             ".lnk" : "LINK",
                             ".xcf" : "GIMP"}
    if name in known_file_extensions:
        return known_file_extensions[name]
    else:
        return name[1:].upper()

def create_folder(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)

for fname in os.listdir('.'):
    name, ext = os.path.splitext(fname)

    if os.path.isdir(fname):
        pass
        # FOLDERS WILL BE IGNORED FOR NOW, BECAUSE IT DIDNT WORK WELL
        # foldername = "FOLDERS"
        # create_folder(foldername)
        # new_directory = foldername + "/"
        # shutil.move(fname, new_directory)
    else:
        foldername = get_folder_name(ext)
        create_folder(foldername)
        new_directory = foldername.upper() + "/"
        file_add_counter = 1
        try:
            file_add_counter = 1
            shutil.move(fname, new_directory)
        except:
            # THIS WILL RUN IF A FILE WITH THE SAME NAME ALREADY EXISTS. IT ADDS A (1) TO THE NAME
            shutil.move(fname, new_directory+f"{name} ({file_add_counter}){ext}") 
            file_add_counter += 1
