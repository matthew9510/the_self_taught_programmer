import os

# current working directory (cwd)
current_working_dir = os.getcwd()
print(current_working_dir)

# hard-coding path
path_of_dir = os.path.join("C:", os.sep, "Users", "Matthias", "Dev", "the_self_taught_programmer", "Files")
print(path_of_dir)

# [list] of files in path
contents_of_dir = os.listdir(path_of_dir)
print(contents_of_dir)

# When a module is loaded in Python, __file__ is set to its name
current_path_of_file = os.path.abspath(__file__)
print(current_path_of_file)