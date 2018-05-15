# coding=utf-8
import re


nomenclat = re.compile(r'^[OPMN]-\d{2}-\d{3}-([АБВГ]|[АБВГ],[АБВГ]).*')  # Р-05-087-В,Г

input_file = r'test_data/nom.txt'
bad_items_file = r'test_data/bad_line_list.txt'
bad_item_dict_list = []


with open(input_file, 'r') as f:
    for i, line in enumerate(f.readlines()):
        line = line.rstrip()
        if re.search(nomenclat, line) is not None:
            print('Line {} - {} is Okay'.format(i+1, line))
        else:
            print('Line {} - {} does not match regex, appending to bad list'.format(i + 1, line))
            bad_item_dict_list.append({'item': line, 'line': i + 1})

with open(bad_items_file, 'w') as out_f:
    for item_dict in bad_item_dict_list:
        out_f.write(str(item_dict['line']) + ' ' + item_dict['item'] + '\n')

