def tokenizer(text,way='word'):
    if way=="sentence":
        return text.split("।")
    elif way=="word":
        return text.split()

def remove_punctuation(text):
    text = text.replace('।', '')
    text = text.replace('‘', '')
    text = text.replace('’', '')
    text = text.replace('?', '')
    text = text.replace(',', '')
    text = text.replace(';', '')
    text = text.replace('!', '')
    text = text.replace('\'', '')
    text = text.replace('-', '')
    text = text.replace('”', '')
    text = text.replace('“', '')
    text = text.replace('/', '')
    text = text.replace('৷', '')
    text = text.strip()
    return text

import re

def remove_foreign(text):
    text = "".join(i for i in text if i in ["।"] or 2432 <= ord(i) <= 2559 or ord(i)== 32)
    text = re.sub(' +', ' ', text)
    return text.strip()

def find_numbers(text):
    regex = "[০১২৩৪৫৬৭৮৯]+.[০১২৩৪৫৬৭৮৯]+|[০১২৩৪৫৬৭৮৯]+"
    match = re.findall(regex, text)
    return match


def ban_to_eng_num(text):
    text = text.replace('০', '0')
    text = text.replace('১', '1')
    text = text.replace('২', '2')
    text = text.replace('৩', '3')
    text = text.replace('৪', '4')
    text = text.replace('৫', '5')
    text = text.replace('৬', '6')
    text = text.replace('৭', '7')
    text = text.replace('৮', '8')
    text = text.replace('৯', '9')
    text = text.replace('.', '.')
    text = text.strip()

    return text


def eng_to_ban_num(text):
    text = text.replace('0', '০')
    text = text.replace('1', '১')
    text = text.replace('2', '২')
    text = text.replace('3', '৩')
    text = text.replace('4', '৪')
    text = text.replace('5', '৫')
    text = text.replace('6', '৬')
    text = text.replace('7', '৭')
    text = text.replace('8', '৮')
    text = text.replace('9', '৯')
    text = text.replace('.', '.')
    text = text.strip()

    return text

words = [
        '',
        'এক',
        'দুই',
        'তিন',
        'চার',
        'পাঁচ',
        'ছয়',
        'সাত',
        'আট',
        'নয়',
        'দশ',
        'এগারো',
        'বারো',
        'তেরো',
        'চৌদ্দ',
        'পনেরো',
        'ষোল',
        'সতেরো',
        'আঠারো',
        'উনিশ',
        'বিশ',
        'একুশ',
        'বাইশ',
        'তেইশ',
        'চব্বিশ',
        'পঁচিশ',
        'ছাব্বিশ',
        'সাতাশ',
        'আঠাশ',
        'ঊনত্রিশ',
        'ত্রিশ',
        'একত্রিশ',
        'বত্রিশ',
        'তেত্রিশ',
        'চৌত্রিশ',
        'পঁয়ত্রিশ',
        'ছত্রিশ',
        'সাঁইত্রিশ',
        'আটত্রিশ',
        'ঊনচল্লিশ',
        'চল্লিশ',
        'একচল্লিশ',
        'বিয়াল্লিশ',
        'তেতাল্লিশ',
        'চুয়াল্লিশ',
        'পঁয়তাল্লিশ',
        'ছেচল্লিশ',
        'সাতচল্লিশ',
        'আটচল্লিশ',
        'ঊনপঞ্চাশ',
        'পঞ্চাশ',
        'একান্ন',
        'বাহান্ন',
        'তিপ্পান্ন',
        'চুয়ান্ন',
        'পঞ্চান্ন',
        'ছাপ্পান্ন',
        'সাতান্ন',
        'আটান্ন',
        'ঊনষাট',
        'ষাট',
        'একষট্টি',
        'বাষট্টি',
        'তেষট্টি',
        'চৌষট্টি',
        'পঁয়ষট্টি',
        'ছেষট্টি',
        'সাতষট্টি',
        'আটষট্টি',
        'ঊনসত্তর',
        'সত্তর',
        'একাত্তর',
        'বাহাত্তর',
        'তিয়াত্তর',
        'চুয়াত্তর',
        'পঁচাত্তর',
        'ছিয়াত্তর',
        'সাতাত্তর',
        'আটাত্তর',
        'ঊনআশি',
        'আশি',
        'একাশি',
        'বিরাশি',
        'তিরাশি',
        'চুরাশি',
        'পঁচাশি',
        'ছিয়াশি',
        'সাতাশি',
        'আটাশি',
        'ঊননব্বই',
        'নব্বই',
        'একানব্বই',
        'বিরানব্বই',
        'তিরানব্বই',
        'চুরানব্বই',
        'পঁচানব্বই',
        'ছিয়ানব্বই',
        'সাতানব্বই',
        'আটানব্বই',
        'নিরানব্বই'
    ]
bnnum = [
        'শূন্য',
        'এক',
        'দুই',
        'তিন',
        'চার',
        'পাঁচ',
        'ছয়',
        'সাত',
        'আট',
        'নয়'
    ]

numbers = [
        '০',
        '১',
        '২',
        '৩',
        '৪',
        '৫',
        '৬',
        '৭',
        '৮',
        '৯'
    ]
class InvalidNumber(Exception):
    @staticmethod
    def message():
        return "Invalid number"

class InvalidRange(Exception):
    @staticmethod
    def message():
        return "Invalid range"

def is_valid(number):
    if not str(number).isnumeric():
        raise InvalidNumber.message()

    if int(number) > 999999999999999 or 'E' in str(number):
        raise InvalidRange.message()

def bn_num(number):
    is_valid(number)
    return number.translate(str.maketrans(''.join(numbers), ''.join(bn_num)))

def bn_word(number):
    is_valid(number)
    if number == 0:
        return 'শূন্য'

    if isinstance(number, float):
        return number_to_word(number)

    return to_word(number)

def bn_comma_lakh(number):
    is_valid(number)
    n = re.sub(r'(\d+?)(?=(\d\d)+(\d)(?!\d))(\.\d+)?', r'\1,', str(number))
    return n.translate(str.maketrans(''.join(numbers), ''.join(bn_num)))

def to_word(num):
    text = ''
    crore = int(num / 10000000)
    if crore != 0:
        if crore > 99:
            text += bn_word(crore) + ' কোটি '
        else:
            text += words[crore] + ' কোটি '

    crore_div = num % 10000000

    lakh = int(crore_div / 100000)
    if lakh > 0:
        text += words[lakh] + ' লক্ষ '

    lakh_div = crore_div % 100000

    thousand = int(lakh_div / 1000)
    if thousand > 0:
        text += words[thousand] + ' হাজার '

    thousand_div = lakh_div % 1000

    hundred = int(thousand_div / 100)
    if hundred > 0:
        text += words[hundred] + ' শত '

    hundred_div = thousand_div % 100
    if hundred_div > 0:
        text += words[hundred_div]

    return text

def to_decimal_word(num):
    text = ''
    decimal_parts = list(num)
    for decimal_part in decimal_parts:
        text += bnnum[int(decimal_part)] + ' '

    return text

def number_to_word(number):
    decimal_part = str(number).split('.')
    text = to_word(int(decimal_part[0]))
    if len(decimal_part) > 1:
        text += ' দশমিক ' + to_decimal_word(decimal_part[1])
    text = text.strip()
    return text