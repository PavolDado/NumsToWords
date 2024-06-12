'''
Program returns numbers written in words

Usage: send text with numbers to translator() and function return number written in words

Author: Pavol Dado
Contact: dado.pavol@gmail.com
2024
'''

def units(num, num_length):
    if num_length == 1 and num == 0:
        return 'nula'
    numlist = (
    '',
    'jeden',
    'dva',
    'tri',
    'štyri ',
    'päť ',
    'šesť ',
    'sedem',
    'osem',
    'deväť ' )
    return numlist[num]
   
   
def ten(num) :
    numlist = (
        'desať',
        'jedenásť',
        'dvanásť',
        'trinásť',
        'štrnásť',
        'pätnásť',
        'šestnásť',
        'sedemnásť',
        'osemnásť',
        'devätnásť'
        )
    return numlist[num]


def tens(num):
    numlist = (
    '',
    'desať',
    'dvadsať',
    'tridsať',
    'štyridsať',
    'päťdesiat',
    'šesťdesiat',
    'sedemdesiat',
    'osemdesiat',
    'deväťdesiat' )
    return numlist[num]


def hundreds(num):
    numlist = (
    '',
    'sto',
    'dvesto',
    'tristo',
    'štyristo',
    'päťsto',
    'šesťsto',
    'sedemsto',
    'osemsto',
    'deväťsto' )
    return numlist[num]


def thousands(num):
    numlist = (
    '',
    'tisíc',
    'dvetisíc',
    'tritisíc',
    'štyritisíc',
    'päťtisíc',
    'šesťtisíc',
    'sedemtisíc',
    'osemtisíc',
    'deväťtisíc' )
    return numlist[num]


def special_chars(char):
    special_char_list = {
        '+':'plus ',
        '-':'mínus '
                         }
    return special_char_list[char]


def number_translator(in_number):
    num_length = len(in_number)
    written_number = ''
    for i in range(num_length):
        num_size = num_length - i
    
        if num_size == 1:
            written_number += units(int(in_number[i]), num_length)
        elif num_size == 2:
            if int(in_number[i]) == 1:
                i += 1
                written_number += ten(int(in_number[i]))
                break
            else:
                written_number += tens(int(in_number[i]))
        elif num_size == 3:
            written_number += hundreds(int(in_number[i]))
        elif num_size == 4:
            written_number += thousands(int(in_number[i]))
    return written_number


def translator(intext):
    translated_text = ''
    num = ''
    num_chars = '0123456789'
    sp_chars = '+-'
    key_chars = num_chars + sp_chars
    for i in intext + ' ':
        if i not in key_chars and num != '':
            translated_text += number_translator(num) + i
            num = ''
        elif i in sp_chars:
            translated_text += special_chars(i)
        elif i in num_chars:
            num += i
        else:
            translated_text += i
    return translated_text
