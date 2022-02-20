def thesaurus_adv(*args):
    my_dict = dict()
    for ind, names in enumerate(args):
        se_names = names.split()
        key_1 = se_names[1][0]
        key_2 = se_names[0][0]
        if key_1 in my_dict:
            if key_2 in my_dict[key_1]:
                my_dict[key_1][key_2].append(names)
            else:
                my_dict[key_1][key_2] = [names]
        else:
            my_dict[key_1] = {key_2: [names]}
    return my_dict


print(thesaurus_adv('Иван Алексеев', 'Илья Андреев', 'Мария Петрова', 'Максим Александров', 'Михаил Ильин',
                    'Петр Анатольев', 'Владимир Семенов', 'Анатолий Серов', 'Илья Михайлов', 'Влад Сергеев'))
