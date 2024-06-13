
import pytesseract
import os, glob, sys
from pdf2image import convert_from_path, convert_from_bytes
from google.colab import files

print("Upload .pdf file")
uploaded = files.upload()

#Displaying information regarding the uploaded file
for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))
  file_name = fn


#Setting the path to the tesseract library executable file n
pytesseract.pytesseract.tesseract_cmd = (r'/usr/bin/tesseract')

#Converting PDF pages into images and assing the extracted information to "images" variable
images = convert_from_bytes(open(file_name, 'rb').read(), size=1000)

#Assigning the starting and ending page parameters
pdf_start = int(input('Enter the starting page number '))-1
pdf_end = int(input('Enter the ending page number '))

#Consizing the PDF to the desired range
images = images[pdf_start:pdf_end]
sytext = ''

#Function to extract character data from the contents of the PDF file using Google OCR engine j
def ExtractText(x):
  text = ''
  text += pytesseract.image_to_string(x, lang = 'eng')

  #Omitting unecessary string values
  text = text.replace('\n',' ')
  return text

for i in range(0,len(images)):
  sytext += '\n\n'+ ExtractText(images[i])+'\n\n'

#Obtaining the output file name from the uploaded file
DownloadFileName = file_name.replace('.pdf','')

#Creating a text file
text_file = open(DownloadFileName+".txt", "wt")
text_file.write(sytext)
text_file.close()

#Downloading the text file on to the host system
files.download(DownloadFileName+'.txt')

#### Clearing all the files in the directory

#Clearning all files
allfiles=[]
for i in glob.glob("*.*"):
  allfiles.append(i)

#Deleting all the files o
for i in allfiles:
  os.remove(i)

#Use the following command to remove all the variable data (If needed)
# sys.modules[__name__].__dict__.clear()
