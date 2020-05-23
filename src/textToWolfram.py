import json
import requests
import os
import urllib.request
from PIL import Image

API_URL = 'http://api.wolframalpha.com/v2/query?'
APP_ID = 'TWQXR8-U5PGHTH8UE'


def text_input_to_dict(text_in):
    x = requests.get(API_URL + 'input=' + input + "&format=image" + "&output=json" + '&appid=' + APP_ID)
    return json.loads(x.content)


def img_src_from_dict(dictionary):
    return dictionary["queryresult"]["pods"][0]["subpods"][0]["img"]["src"]


def download_img(img_url):
    image = Image.open(urllib.request.urlopen(img_url))
    image.save(r"./imgs/tempimg.gif")


r = text_input_to_dict("integral from 0 to 2 of x^2 dx")
url = img_src_from_dict(r)
download_img(url)
