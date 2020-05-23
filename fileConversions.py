from pdflatex import PDFLaTeX
import io
import os
import subprocess
import argparse
def generateTex(filepath):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    tempTex = dir_path+r"\temp.tex"
    print(tempTex)
    #rawTempTex = r'{}'.format(tempTex)
    fO = open(tempTex, "w")
    fR = open(filepath, "r")
    line = fR.readline()
    while(line):
        fO.write(line)
        line = fR.readline()
    fR.close()
    fO.close()
    return tempTex

def generatePdf(filename):
    #pdfl = PDFLaTeX.from_texfile(r"C:\Users\sohil\Documents\pubChemGetReq\templatedoc.tex")
    #fR = open("temp.tex", "r")
    #line = fR.readline()
    #while(line):
    #    print(line)
    #    line = fR.readline()
    #pdf, log, completed_process = pdfl.create_pdf()
    proc = subprocess.Popen(['pdflatex', filename])
    proc.communicate()
    #cmd = ['pdflatex', '-interaction', 'nonstopmode', filename]
    #proc = subprocess.Popen(cmd)
    #proc.communicate()
#tempFileName = generateTex(r"C:\Users\sohil\Documents\pubChemGetReq\test.txt")
#generatePdf(tempFileName)
