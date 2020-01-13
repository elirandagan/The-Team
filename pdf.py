from PyPDF2 import PdfFileWriter, PdfFileReader

with open("exe.pdf", "rb") as in_f:
    input1 = PdfFileReader(in_f)
    output = PdfFileWriter()

    numPages = input1.getNumPages()
    print("document has %s pages." % 1)

    page = input1.getPage(0)
    print(page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
    page.trimBox.lowerLeft = (5, 554)
    page.trimBox.upperRight = (504, 4)
    page.cropBox.lowerLeft = (48, 257)
    page.cropBox.upperRight = (364, 133)
    output.addPage(page)

    with open("out.pdf", "wb") as out_f:
        output.write(out_f)
