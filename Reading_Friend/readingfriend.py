import PyPDF2
import pyttsx3
reader = pyttsx3.init()
rate = reader.getProperty('rate')
reader.setProperty('rate', 150)
def read(txt):
    reader.say(txt)
    reader.runAndWait()
read('Welcome to RR-Web Developers')
filename = input('Enter file name without extension: ')
filename = filename + '.pdf'
pdf_book = open(filename, 'rb')
try:
    pdfReader = PyPDF2.PdfFileReader(pdf_book)
    pages = pdfReader.numPages
    print('Total Pages: ' +str(pages))
    page_num = int(input('Enter Page No: '))
    page_num = page_num -1
    read('OK Boss.')
    print('Reading......')
    for num in range(page_num, pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        text = text.replace('/n', ' ')
        text = text.replace('™', '')
        #print(text)
        read(text)
except:
    print('PDF file is not Decrypted.')
