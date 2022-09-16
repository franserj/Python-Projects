# Heads up:
# You must place the file for reading in the same directory as the code, or specify where it is.

# import pyttsx3
# speaker = pyttsx3.init()
# speaker.say("Olá, Mundo! Eu ainda estou aqui!")
# speaker.runAndWait()

import pyttsx3
import PyPDF2

book = open('dom.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(11)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
