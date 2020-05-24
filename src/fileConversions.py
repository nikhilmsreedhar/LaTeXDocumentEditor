from pdflatex import PDFLaTeX
import io
import os
from os import listdir
import subprocess
import argparse
import shutil
import pathlib


def generate_tex(filepath, project_name):
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = "../resources/"
    temp_tex = dir_path + project_name + ".tex"
    print(temp_tex)
    fo = open(temp_tex, "w")
    fr = open(filepath, "r")
    line = fr.readline()
    while line:
        fo.write(line)
        line = fr.readline()
    fr.close()
    fo.close()
    return temp_tex


def generate_pdf(filename):
    proc = subprocess.Popen(['pdflatex', filename])
    proc.communicate()
    folder_path = pathlib.Path(__file__).parent
    folder = str(folder_path)
    folder = folder + "\\"
    print(folder)
    for file_name in listdir(folder_path):
        if file_name.endswith('.toc'):
            os.remove(folder + file_name)
        if file_name.endswith('.aux'):
            os.remove(folder + file_name)
        if file_name.endswith('.log'):
            os.remove(folder + file_name)


# tempFileName = generate_tex(r"C:\Users\sohil\Documents\pubChemGetReq\test.txt")
# generate_pdf(tempFileName)
