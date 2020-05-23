import json
import requests
import os
import urllib.request
from PIL import Image

API_URL = 'http://api.wolframalpha.com/v2/query?'
APP_ID = '&appid=TWQXR8-U5PGHTH8UE'
USER_REQUEST = 'input='


def text_input_to_dict(input):
    x = requests.get(API_URL + USER_REQUEST + input + "&format=image" + "&output=json" + APP_ID)
    return json.loads(x.content)


def img_src_from_dict(dict):
    return dict["queryresult"]["pods"][0]["subpods"][0]["img"]["src"]


def download_img(url):
    image = Image.open(urllib.request.urlopen(url))
    image.save(r"C:\Users\Nikhi\Desktop\img\name.gif")


r = text_input_to_dict("integral from 0 to 2 of x^2 dx")
url = img_src_from_dict(r)
download_img(url)
