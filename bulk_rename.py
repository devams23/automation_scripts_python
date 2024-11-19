import os
import shutil
def bulk_rename(folder_path, old_name_part, new_name_part):
    for filename in os.listdir(folder_path):
        print(filename)
        if old_name_part in filename:
            new_filename = filename.replace(old_name_part, new_name_part)
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            print(f"Renamed {filename} to {new_filename}")

folder = 'D:/python_tut/automation_scripts' 
bulk_rename(folder, 'prod', 'prior')



# copying file from one folder to another

def backup_file(src_path, des_path):
    if not os.path.exists(des_path):
        os.makedirs(des_path)
    for filename in os.listdir(src_path):
        src_fullfile_name=os.path.join(src_path,filename)
        if os.path.isfile(src_fullfile_name):
            shutil.copyfile(src_fullfile_name,des_path)
    

source="D:/python_tut/automation_scripts"
destination="D:/python_tut/automation_scripts/samplefolder"

backup_file(src_path=source,des_path=destination)