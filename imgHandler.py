#!/usr/bin/env python
import sys
import matplotlib.pyplot as plot
import sympy
from sympy import symbols, preview, Symbol
import io
import base64
import requests
import json
from PIL import Image, ImageChops

test_path = 'C:\\Users\\arnav\\OneDrive - University of Florida\\LaTeX DocEditor for Math and Chem\\imgs\\quad.png'
out_path = 'C:\\Users\\arnav\\OneDrive - University of Florida\\LaTeX DocEditor for Math and Chem\\out\\'


def latex_to_png(latex_file_name):
    backslash_index = latex_file_name.rfind("\\")
    element_name = latex_file_name[backslash_index:]
    extension_index = element_name.find(".txt")
    element_name = element_name[0:extension_index]

    handle = open(latex_file_name, 'r')
    handle.readline()
    latex = handle.readline()
    handle.close()

    new_line_index = latex.find('\n')
    latex = latex[0:new_line_index]
    latex = "$$" + latex + "$$"

    preview(latex, output='png', viewer='file', filename=out_path+element_name+'.png', euler=False)


def gif_to_jpg(filename_gif):
    index = filename_gif.find(".gif")
    filename = filename_gif[0:index]
    Image.open(filename_gif).convert('RGB').save(filename + '.jpg')


def img_to_json(file_path):
    if file_path.find(".gif") != -1:
        gif_to_jpg(file_path)
        index = file_path.find(".gif")
        file_path = file_path[0:index] + '.jpg'

    image_uri = "data:image/jpg;base64," + base64.b64encode(open(file_path, "rb").read()).decode()
    r = requests.post("https://api.mathpix.com/v3/text",
                      data=json.dumps({'src': image_uri}),
                      headers={"content-type": "application/json",
                               "app_id": "bunnefant_gmail_com_864111",
                               "app_key": "a3a70d77d47c29c792cd"}
                      )
    return json.dumps(json.loads(r.text), indent=4, sort_keys=True)


def json_to_latex(j):
    mathpix_dict = json.loads(j)
    return mathpix_dict['latex_styled']


def write_latex_to_txt(latex, element_name):
    handle = open(out_path + element_name + '.txt', 'w')
    handle.write("\\begin{equation}\n")
    handle.write(latex + '\n')
    handle.write("\\end{equation}\n")


j = img_to_json(test_path)
l = json_to_latex(j)
write_latex_to_txt(l, "equation numero boog")
latex_to_png(out_path + "equation numero boog.txt")