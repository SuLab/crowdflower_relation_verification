# last updated 2015-04-13 toby
import os

def read_file(file_name, file_loc = os.getcwd()):
    with open(os.path.join(file_loc, file_name), "r") as file:
        for line in file:
            yield line.rstrip('\n')

def make_dir(loc):
    if not os.path.exists(loc):
        os.makedirs(loc)
