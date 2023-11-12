from PyPDF2 import PdfReader
import pyttsx3

'''
TODO
Add option to select variable volumes, voices, speeds
Add option to listen to sample before downloading
'''


def pdfToMp3(selected_file, file_name):
    print(f'selected_file: {selected_file}')
    print(f'file_name: {file_name}')

    # extract pdf text
    file_no_ext = file_name[:-4]
    try:
        reader = PdfReader(selected_file)
    except FileNotFoundError:
        print("Could not find a file with that name. Please try again...")
    except:
        print("Unsupported file type. Please make sure you have a pdf.")

    number_of_pages = len(reader.pages)

    full_text = ''

    for page_number in range(number_of_pages):
        page = reader.pages[page_number]
        text = page.extract_text()
        clean_text = text.strip().replace('\n', ' ')
        full_text += clean_text

    # convert text to mp3

    engine = pyttsx3.init()
    engine.connect('started-utterance', print('Converting....'))
    engine.connect('finished-utterance',
                   print(f'Conversion complete! File saved as {file_no_ext}.mp3'))
    engine.save_to_file(full_text, f"{file_no_ext}.mp3")
    engine.runAndWait()
