from PIL import Image

import imgHandler
import chemReq
import textToWolfram
import fileConversions
import synthesize


def get_image_from_input(text_in, el_name, choice):
    # Choices:
    # 0 - typed math
    # 1 - image math (text_in is a file path)
    # 2 - typed molecule name

    if choice == 0:
        # Use text input from User to get GIF from Wolfram
        wolfram_dict = textToWolfram.text_input_to_dict(text_in)
        wolfram_img_url = textToWolfram.img_src_from_dict(wolfram_dict)
        textToWolfram.download_img(wolfram_img_url)

        # Use GIF from Wolfram to get Raw LaTeX
        wolfram_img_file_path = "../imgs/temp.gif"
        math_pix_json = imgHandler.img_to_json(wolfram_img_file_path)
        raw_latex = imgHandler.json_to_latex(math_pix_json)

        # Crop solution from LaTeX based on input
        resolved_latex = imgHandler.latex_cropper(text_in, raw_latex)

        # Write LaTeX equation to text with necessary wrapper
        imgHandler.write_latex_eq_to_txt(resolved_latex, el_name)

        # Return rendered PNG of LaTeX for Display
        return imgHandler.latex_to_png("../out/" + el_name + ".txt", el_name)

    elif choice == 1:
        # Use Image File from User to get Raw LaTeX
        math_pix_json = imgHandler.img_to_json(text_in)
        raw_latex = imgHandler.json_to_latex(math_pix_json)

        # Write LaTeX equation to text with necessary wrapper
        imgHandler.write_latex_eq_to_txt(raw_latex, el_name)

        # Return rendered PNG of LaTeX for Display
        return imgHandler.latex_to_png("../out/" + el_name + ".txt", el_name)

    elif choice == 2:
        # Use text input from User to get PNG from PubChem
        molecule_image = chemReq.get_molecule_image(text_in, el_name)

        # Write LaTeX for inserting image
        chemReq.write_latex_molecule_to_txt(el_name)

        # Return previously found PNG
        return molecule_image

    else:
        print("Invalid choice")


def export(file_names, project_name):
    synthesize.write_elements_to_master_txt(file_names, project_name)
    file_name = fileConversions.generate_tex("../out/" + project_name + ".txt", project_name)
    fileConversions.generate_pdf(file_name)


# get_image_from_input("integral from 0 to 1 of x^3 dx", "equation1", 0)
# get_image_from_input("../imgs/IMG_8642.jpg", "equation2", 1)
# get_image_from_input("../imgs/quad.png", "equation3", 1)
# get_image_from_input("angelic acid", "mol1", 2)

file_names = ["header", "equation1", "equation2", "mol1", "equation3", "footer"]

export(file_names, "bruh_project")