from distutils.filelist import translate_pattern
from translate import Translator
import sys
import os

# input language option

lang, file_input, file_output, new_dir = sys.argv[1:4]


translator = Translator(to_lang=f'{lang}')

if 
# translate file into new file
try:
    with open(f'{file_input}', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
    with open(f'{file_output}', mode='w') as my_file2:
        my_file2.write(translation)
except IOError as err1:
    print('Theres an error')
except FileNotFoundError as err2:
    print('File not found')
