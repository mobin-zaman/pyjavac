#! /usr/bin/python3
# if in windows convert the above line from # /usr/bin/python3 to # python3
import os

# give your root directory here, between the ' ' (absolute path)
#exmple: root_dir=('C://your_folder')
root_dir = ('')


print('scanning....')
for folder_name, sub_folders, file_names in os.walk(root_dir):

    for filename in file_names:
        if filename.endswith('.class'):
            print('DELETING CLASS FILE: ' + folder_name + filename)
            os.remove(folder_name+'/'+filename)

print('EXECUTING javac *.java  COMMAND....... ')
my_command = "javac *.java"
os.system(my_command)

print('EXECUTING java Main')
# if the driver class name is different then edit the below command replacing Msin
my_command = "java Main"
os.system(my_command)
print('DONE')
