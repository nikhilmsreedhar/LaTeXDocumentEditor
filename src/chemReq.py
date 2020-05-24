from PIL import Image
import requests
from io import BytesIO


def get_molecule_image(molecule, element_name):
    link = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/%s/PNG"
    link = link % molecule
    print(link)
    response = requests.get(link)
    img = Image.open(BytesIO(response.content))
    print(img)
    img.save("../out/" + element_name + ".png")
    return img


def write_latex_molecule_to_txt(element_name):
    handle = open('../out/' + element_name + '.txt', 'w')
    handle.write("\\begin{figure}[ht!]\n")
    handle.write("\\centering\n")
    handle.write("\\includegraphics[width=90mm]{../out/" + element_name + ".png}\n")
    handle.write("\\end{figure}")
