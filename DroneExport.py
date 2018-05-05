import os
from datetime import datetime
import shutil

confirm = input(">>> This program will move the pictures and videos from your drone into a folder on your PC.  This "
                "operation could take a while.  Do you wish to continue (y/n)? ")

if confirm.lower() == "n":
    print("Exiting.")
    exit()

elif confirm.lower() == "y":
    today = str(datetime.date(datetime.today()))
    year = str(datetime.today().year)
    pics = 0
    videos = 0

    drone_letter = input("Please enter the drive letter for the drone (not case-sensitive): ") + ":/"
    path_to_files = drone_letter + "DCIM/100MEDIA/"
    output_letter = input("Please enter the drive letter for the output (not case-sensitive): ") + ":/"
    export_name = input("Please enter a folder name to export to (case-sensitive): ")
    output_dir = str(output_letter + export_name + "/" + year + "/" + today)
    pic_dir = str(output_dir + "/Pictures/")
    vid_dir = str(output_dir + "/Videos/")

    if export_name not in os.listdir(output_letter):
        print("Output directory not found.  Creating...")
        os.makedirs(output_letter + export_name)
        if year not in os.listdir(output_letter + export_name):
            print("Year folder not found, making it.")
            print(str(output_letter + export_name + "/" + year))
            os.makedirs(output_letter + export_name + "/" + year)
        if today not in os.listdir(output_letter + export_name + "/" + year):
            print("Today's folder not found, making it.")
            print(str(output_letter + export_name + "/" + year + "/" + today))
            os.makedirs(output_letter + export_name + "/" + year + "/" + today)
        if pic_dir not in os.listdir(output_letter + export_name + "/" + year + "/" + today):
            print("Picture folder not found, making it.")
            print(str(pic_dir))
            os.makedirs(pic_dir)
        if vid_dir not in os.listdir(output_letter + export_name + "/" + year + "/" + today):
            print("Video folder not found, making it.")
            print(str(vid_dir))
            os.makedirs(vid_dir)
    else:
        if year not in os.listdir(output_letter + export_name):
            print("Year folder not found, making it.")
            print(str(output_letter + export_name + "/" + year))
            os.makedirs(output_letter + export_name + "/" + year)
        if today not in os.listdir(output_letter + export_name + "/" + year):
            print("Today's folder not found, making it.")
            print(str(output_letter + export_name + "/" + year + "/" + today))
            os.makedirs(output_letter + export_name + "/" + year + "/" + today)
        if pic_dir not in os.listdir(output_letter + export_name + "/" + year + "/" + today):
            print("Picture folder not found, making it.")
            print(str(pic_dir))
            os.makedirs(pic_dir)
        if vid_dir not in os.listdir(output_letter + export_name + "/" + year + "/" + today):
            print("Video folder not found, making it.")
            print(str(vid_dir))
            os.makedirs(vid_dir)
        print("\nExporting files now.\n")

    for i in os.listdir(path_to_files):
        if ".JPG" in i or ".DNG" in i:
            if i not in os.listdir(pic_dir):
                print("Moving " + i)
                shutil.move(path_to_files + i, pic_dir + i)
                pics += 1
            else:
                conflict = 1
                rename = 1
                print(i + " found in output directory.  Renaming...")
                j = i.split(".")
                k = j[0] + "-" + str(rename) + "." + j[1]
                while conflict == 1:
                    if k in os.listdir(pic_dir):
                        rename += 1
                        k = j[0] + "-" + str(rename) + "." + j[1]
                    else:
                        conflict = 0
                os.rename(path_to_files + i, path_to_files + k)
                print("Moving " + k)
                shutil.move(path_to_files + k, pic_dir + k)
                pics += 1
        elif ".MP4" in i:
            if i not in os.listdir(vid_dir):
                print("Moving " + i)
                shutil.move(path_to_files + i, vid_dir + i)
                videos += 1
            else:
                conflict = 1
                rename = 1
                print(i + " found in output directory.  Renaming...")
                j = i.split(".")
                k = j[0] + "-" + str(rename) + "." + j[1]
                while conflict == 1:
                    if k in os.listdir(vid_dir):
                        rename += 1
                        k = j[0] + "-" + str(rename) + "." + j[1]
                    else:
                        conflict = 0
                os.rename(path_to_files + i, path_to_files + k)
                print("Moving " + k)
                shutil.move(path_to_files + k, vid_dir + k)
                videos += 1
    print("\nMoved {} pictures and {} videos to '".format(pics, videos) + output_dir + "/'.")
else:
    print("\n\nPlease restart the program and enter only Y or N.\n\n")
