import json
import requests
import os
import urllib.request
from PIL import Image

API_URL = 'http://api.wolframalpha.com/v2/query?'
APP_ID = '&appid=TWQXR8-U5PGHTH8UE'
USER_REQUEST = 'input='


def getQuestion(input):
    x = requests.get(API_URL + USER_REQUEST + input + "&format=image" + "&output=json" + APP_ID)
    return json.loads(x.content)


def getImgSourceFromDictionary(dict):
    return dict["queryresult"]["pods"][0]["subpods"][0]["img"]["src"]


def downloadImg(url):
    image = Image.open(urllib.request.urlopen(url))
    image.save(r"C:\Users\Nikhi\Desktop\img\name.gif")


r = getQuestion("integral from 0 to 2 of x^2 dx")
url = getImgSourceFromDictionary(r)
downloadImg(url)
