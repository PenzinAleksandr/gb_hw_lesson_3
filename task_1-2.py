def num_translate_adv():
    while True:
        num = str(input('For translation, enter the number in words, or write "exit": '))
        if num != 'exit' and num[0].isupper():
            result = (new_dict.get(num.lower()))
            if result is None:
                print('None')
                continue
            print(result.capitalize())
        elif num != 'exit':
            result = (new_dict.get(num))
            if result is None:
                print('None')
                continue
            print(result)
        else:
            break


new_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


num_translate_adv()
