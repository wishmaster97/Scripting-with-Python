import PyPDF2 as PDF

input_file = PDF.PdfFileReader(open("dummy.pdf", "rb"))
watermark = PDF.PdfFileReader(open("wtr.pdf", "rb"))
output_file = PDF.PdfFileWriter()

for i in range(input_file.getNumPages()):
    page = input_file.getPage(i)
    page.mergePage(watermark.getPage(0))
    output_file.addPage(page)

with open("watermarked.pdf" , "wb") as newFile:
    output_file.write(newFile)