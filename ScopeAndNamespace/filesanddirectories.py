# a good use of recursion is obtaining a list of files in a directory
# The only things that screate scope in Python are: Modules, Functions
# and Classes
import os


def list_directories(s):


    # scoped function
    def dir_list(d):
        # creates a properly scoped variable
        # nonlocal tells python to look for a variable in the enclosing
        # scopes. This means that the variable MUST existing in the 
        # enclosing scope BUT NOT BE global
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            # take a look at this and see if you can refactor some of
            # your code using this logic (os.path.join)
            current_dir = os.path.join(d, f)
            # each time the function find a new directory, it indents
            # the tab by one, for each nested directory
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + f)
                tab_stop +=1
                # recursion
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)
    
    tab_stop = 0
    if os.path.exists(s):
        print("Direcotry list of " + s)
        dir_list(s)
    else:
        print(s + " does not exist")

list_directories('.')