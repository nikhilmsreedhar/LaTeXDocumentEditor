#!/usr/bin/env python
import sys
import matplotlib.pyplot as plot
import sympy
from sympy import symbols, preview, Symbol
from IPython.display import Latex
import io
import base64
import requests
import json
from PIL import Image, ImageChops

test_path = '../imgs/test.gif'
out_path = '../out/'


def count_equals(x):
    return x.count("=")


def latex_cropper(text_in, latex):
    print(text_in)
    print(latex)
    x = count_equals(text_in)
    while count_equals(latex) > x:
        index = latex.rfind("=")
        latex = latex[0:index]
    return latex


def latex_to_what(latex_file_name, element_name):
    handle = open(latex_file_name, 'r')
    handle.readline()
    latex = handle.readline()
    handle.close()

    # new_line_index = latex.find('\n')
    # latex = latex[0:new_line_index]
    # latex = "$$" + latex + "$$"

    Latex(latex)

def latex_to_png(latex_file_name, element_name):
    # backslash_index = latex_file_name.rfind("\\")
    # element_name = latex_file_name[backslash_index:]
    # extension_index = element_name.find(".txt")
    # element_name = element_name[0:extension_index]

    handle = open(latex_file_name, 'r')
    handle.readline()
    latex = handle.readline()
    handle.close()

    preamble = "\\documentclass[a4paper, 12pt, titlepage, legno]{article}\n" \
               "\\usepackage[english]{babel}\n" \
               "\\usepackage[a4paper, inner=1.25in, outer=1.25in, top=1.25in, bottom = 1.25in]{geometry}\n" \
               "\\usepackage{amsmath}\n" \
               "\\usepackage{amssymb}\n" \
               "\\usepackage{amsthm}\n" \
               "\\usepackage{wasysym}\n" \
               "\\usepackage{booktabs}\n" \
               "\\usepackage{array}\n" \
               "\\usepackage{marvosym}\n" \
               "\\usepackage{graphicx}\n" \
               "\\begin{document}"

    new_line_index = latex.find('\n')
    latex = latex[0:new_line_index]
    latex = "$$" + latex + "$$"

    preview(latex, output='png', viewer='file', filename='../out/' + element_name + '.png', euler=False, preamble=preamble)
    img = Image.open('../out/' + element_name + '.png')
    return img


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


def json_to_latex(json_file):
    math_pix_dict = json.loads(json_file)
    return math_pix_dict['latex_styled']


def write_latex_eq_to_txt(latex, element_name):
    handle = open('../out/' + element_name + '.txt', 'w')
    handle.write("\\begin{equation}\n")
    handle.write(latex + '\n')
    handle.write("\\end{equation}\n")


# input_example = "integral from 0 to 2 of x^2 dx"
# j = img_to_json(test_path)
# tex = json_to_latex(j)
# tex = latex_cropper(input_example, tex)
# write_latex_eq_to_txt(tex, "equation numero boog")
# latex_to_png('../out/' + "equation numero boog.txt")
