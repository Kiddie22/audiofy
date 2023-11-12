from PyPDF2 import PdfReader
import pyttsx3

'''
TODO
Save audio as file
Add option to select variable volumes, voices, speeds
'''

# extract pdf text

while (True):
    fileName = input(
        "Place your pdf file in the /books folder and enter the file name with the extension: \n")
    try:
        reader = PdfReader(f'books/{fileName}')
        break
    except FileNotFoundError:
        print("Could not find a file with that name. Please try again...")

number_of_pages = len(reader.pages)

full_text = ''

for page_number in range(number_of_pages):
    page = reader.pages[page_number]
    text = page.extract_text()
    clean_text = text.strip().replace('\n', ' ')
    full_text += clean_text

# read extracted text

engine = pyttsx3.init()
engine.say(full_text)
engine.runAndWait()

print("Finished reading...")
print("Exiting application")
