import sys, os, json, time
import os.path as op
from zipfile import ZipFile as __zipFile
from zipfile import ZIP_DEFLATED
from shutil import copyfile


def zipFolder(source_folder, out_file_path):
    zout =  __zipFile(out_file_path, "w", ZIP_DEFLATED)
    source_list = []
    target_list = []
    target_root = op.split(source_folder)[-1]
    for root, dirs, files in os.walk(source_folder):
        for f in files:
            source_path = op.join(root, f)
            target_path = source_path.replace(source_folder, "")
            source_list.append( source_path )
            target_list.append( target_path )

    for source, target in zip(source_list, target_list):
        zout.write(source, target)
    zout.close()

def main():
    outFolder = r"D:\Construct 3\my_data\C3RexDoc\repo"
    
    for arg in sys.argv[1:]:
        if not op.isdir(arg):
            continue
      
        (head, pluginName) = op.split(arg)
        (head, category) = op.split(head)
        
        print category + ":" + pluginName
        zipFolder(arg, op.join(outFolder , pluginName+".c3addon"))
        copyfile(op.join(arg, "icon.png"), op.join(outFolder, pluginName+".png"))

    import indexGen       

# -----------------------------------------------------------------------------  
try:
    main()
except Exception, e: 
    print e

raw_input()
