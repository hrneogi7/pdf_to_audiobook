
import pyttsx3
import PyPDF2
from tkinter.filedialog import *
from gtts import gTTS

pdf=askopenfilename()


pdf_read=PyPDF2.PdfFileReader(pdf)
pages=pdf_read.numPages
print(pages)

for num in range(pages):
    page_get=pdf_read.getPage(num)

    text_form=page_get.extractText()

    final_file = gTTS(text=text_form, lang='en')
    
    final_file.save("D:\Pdf_to_audio\audio_files\audio_conv.mp3")