from PyPDF2 import PdfMerger

allpdf = ["01 lab.pdf","02 mutataion.pdf"]
ourmerger = PdfMerger()
for newpdf in allpdf:
    ourmerger.append(newpdf)
ourmerger.write("03 Merge.pdf")
ourmerger.close()