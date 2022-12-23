from PyPDF2 import PdfFileReader
import docx2txt
def read_pdf(file):
	pdfReader = PdfFileReader(file)
	count = pdfReader.numPages
	all_page_text = ""
	for i in range(count):
		page = pdfReader.getPage(i)
		all_page_text += page.extractText()

	return all_page_text
def upload(file):
    if file.type == "text/plain":
        return str(file.read(),"utf-8")
    elif file.type == "application/pdf":
        text=read_pdf(file)
        return text
    else:
        return docx2txt.process(file)