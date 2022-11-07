from distutils.filelist import translate_pattern
from translate import Translator
import sys
import os

# input language option
lang = sys.argv[1]
# input file to be translated
file_input = sys.argv[2]
# output new file
file_output = sys.argv[3]
# new file directory filepath
new_dir = sys.argv[4]

print('all variables have been assigned')

translator = Translator(to_lang=f'{lang}')
print(f'language has been set to {lang}')

new_dir_list = os.listdir(new_dir)
print(new_dir_list)

# translate file into new file
try:
    if file_output not in new_dir_list:
        with open(f'{file_input}', mode='r', encoding='utf-8') as my_file:
            text = my_file.read()
            translation = translator.translate(text)
        with open(f'{file_output}', mode='w', encoding='utf-8') as my_file2:
            my_file2.write(translation)
    else:
        print('file already exists! please create a new file')
except IOError as err1:
    print('Theres an error')
    raise err1
except FileNotFoundError as err2:
    print('File not found')
    raise err2
