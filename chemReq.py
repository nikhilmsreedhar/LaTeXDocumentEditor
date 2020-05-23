from PIL import Image
import requests
from io import BytesIO
def getImage(molecule):
     link = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/%s/PNG"
     link = link % molecule
     print(link)
     response = requests.get(link)
     img = Image.open(BytesIO(response.content))
     print(img)
     img.show()
     return img

getImage('benzene')
