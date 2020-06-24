import PyPDF2 as PDF
import sys
'''
inputs = sys.argv[1:]

def combinePDF(pdf_list):
    merger = PDF.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
        

    merger.write("super.pdf")
    '''

def addWatermark():
    input_file = "dummy.pdf"
    wtr = "wtr.pdf"
    output_file = "output.pdf"

    # create a pdf writer object for the output file
    

    with open(input_file, "rb") as filehandle_input:
        # read content of the original file
        input_pdf = PDF.PdfFileReader(filehandle_input)
    
        with open(wtr, "rb") as filehandle_watermark:
            # read content of the watermark
            watermark = PDF.PdfFileReader(filehandle_watermark)
            # get ith page of the original PDF
            pdf_writer = PDF.PdfFileWriter()
            for i in range(input_pdf.getNumPages()):
                curr_page_inputFile = input_pdf.getPage(i)

                # merge the two pages
                curr_page_inputFile.mergePage(watermark.getPage(0))

                # add page
                pdf_writer.addPage(curr_page_inputFile)

            #merge append the page
            with open(output_file, "wb") as filehandle_output:
                # write the watermarked file to the new file
                pdf_writer.write(filehandle_output)

#combinePDF(inputs)

addWatermark()