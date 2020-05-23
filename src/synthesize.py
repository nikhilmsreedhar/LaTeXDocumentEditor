
out_path = 'C:\\Users\\arnav\\OneDrive - University of Florida\\LaTeX DocEditor for Math and Chem\\out\\'


def write_elements_to_master_txt(file_names, proj_name):
    outfile = open(out_path + proj_name + ".txt", 'w')
    for i in range(len(file_names)):
        curr_file_name = file_names[i]
        handle = open(curr_file_name, 'r')
        outfile.write(handle.read())
        handle.close()
    outfile.close()


