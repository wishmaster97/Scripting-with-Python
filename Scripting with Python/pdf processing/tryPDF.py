import PyPDF2 as pdf

#rb is for read binary
with open("ebook.pdf", "rb") as pdfFile:
    reader = pdf.PdfFileReader(pdfFile)
    #numPages is for num of pages in given pdf
    print(reader.numPages)

    #to get specific page, if no page in  PDF - returns an error
    print(reader.getPage(124))


    #rotating PDf content to an angle
    page = reader.getPage(124)
    #print(page.rotateClockwise(90))

    #after getting a page element we can write the page into file
    page.rotateClockwise(90)
    
    #getting a writter object from PyPDF2
    writer = pdf.PdfFileWriter()
    writer.addPage(page)
    with open("tilt.pdf", "wb") as new_file:
        writer.write(new_file)
