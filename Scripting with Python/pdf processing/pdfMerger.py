import PyPDF2 as PDF
import sys

inputs = sys.argv[1:]

def combinePDF(pdf_list):
    merger = PDF.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)

    merger.write("super.pdf")

combinePDF(inputs)