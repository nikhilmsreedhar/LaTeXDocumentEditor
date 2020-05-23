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
        wolfram_img_file_path = textToWolfram.img_src_from_dict(wolfram_dict)
        textToWolfram.download_img(wolfram_img_file_path)

        # Use GIF from Wolfram to get Raw LaTeX
        math_pix_json = imgHandler.img_to_json(wolfram_img_file_path)
        raw_latex = imgHandler.json_to_latex(math_pix_json)

        # Crop solution from LaTeX based on input
        resolved_latex = imgHandler.latex_cropper(input, raw_latex)

        # Write LaTeX equation to text with necessary wrapper
        imgHandler.write_latex_eq_to_txt(resolved_latex, el_name)

        # Return rendered PNG of LaTeX for Display
        return imgHandler.latex_to_png(resolved_latex)

    elif choice == 1:
        # Use Image File from User to get Raw LaTeX
        math_pix_json = imgHandler.img_to_json(text_in)
        raw_latex = imgHandler.json_to_latex(math_pix_json)

        # Crop solution from LaTeX based on input
        resolved_latex = imgHandler.latex_cropper(input, raw_latex)

        # Write LaTeX equation to text with necessary wrapper
        imgHandler.write_latex_eq_to_txt(resolved_latex, el_name)

        # Return rendered PNG of LaTeX for Display
        return imgHandler.latex_to_png(resolved_latex)

    elif choice == 2:
        # Use text input from User to get PNG from PubChem
        molecule_image = chemReq.get_molecule_image(text_in, el_name)

        # Write LaTeX for inserting image
        chemReq.write_latex_molecule_to_txt(el_name)

        return molecule_image

    else:
        print("Invalid choice")


def export(file_names, project_name):
    synthesize.write_elements_to_master_txt(file_names, project_name)
    file_name = fileConversions.generate_tex("../out/" + project_name + ".txt")
    fileConversions.generate_pdf(file_name)

