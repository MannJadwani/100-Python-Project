#pdf merger

import PyPDF2

merger = PyPDF2.PdfMerger()

pdf = ['1.pdf','2.pdf']

for filename in pdf:
    
    pdFiles= open(filename,'rb')
    
    pdfReader = PyPDF2.PdfReader(pdFiles)
    
    merger.append(pdfReader)
    
    pdFiles.close()
    
    merger.write('merger.pdf')

