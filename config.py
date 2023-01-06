#!/usr/bin/env python

import configparser
import pathlib
import os

path = pathlib.Path(__file__).parent.resolve()
# CREATE OBJECT
config_file = configparser.ConfigParser()

# ADD SECTION
config_file.add_section("path")
directory = str(path)
input_folder = "input"
temp_folder = "temp"
out_folder = "output"


path1 = os.path.join(directory, input_folder)
os.mkdir(path1)
path2 = os.path.join(directory, temp_folder)
os.mkdir(path2)
path3 = os.path.join(directory, out_folder)
os.mkdir(path3)


# ADD SETTINGS TO SECTION

config_file.set("path", "input", directory + "/input/input.txt")
config_file.set("path", "temp", directory + "/temp/temp.txt")
config_file.set("path", "temp1", directory + "/temp/temp1.txt")
config_file.set("path", "temp2", directory + "/temp/temp2.txt")
config_file.set("path", "output", directory + "/output/output.txt")



# SAVE CONFIG FILE
with open(r"config.ini", "w") as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

print("Config file 'configurations.ini' created")

# PRINT FILE CONTENT
read_file = open("config.ini", "r")
content = read_file.read()
print("Content of the config file are:\n")
print(content)
read_file.flush()
read_file.close()
