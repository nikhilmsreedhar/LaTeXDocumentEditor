
def write_elements_to_master_txt(file_names, project_name):
    outfile = open('../out/' + project_name + ".txt", 'w')
    for i in range(len(file_names)):
        curr_file_name = "../out/" + file_names[i] + ".txt"
        handle = open(curr_file_name, 'r')
        outfile.write(handle.read())
        handle.close()
    outfile.close()


