import os

current_path_of_file = os.path.abspath(__file__)

with open(current_path_of_file, "a") as this_file:
    # note: when writing no concatenation of multi-lines needed
    this_file.write("\n\n\"\"\" \nModes:" 
              "\n r - read only" 
               "\n w - writing only, overwrite if file exists " 
               "\n w+ - reading and writing, overwrite if file exists" 
               "\n a - append to file" 
               "\n \"\"\"")

""" 
Modes:
 r - read only
 w - writing only, overwrite if file exists 
 w+ - reading and writing, overwrite if file exists
 a - append to file
 """