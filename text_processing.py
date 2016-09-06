# -*- coding: utf-8 -*-

from pypinyin import lazy_pinyin

def generator_chinese():
    for line in open('./data/input/ref_word.txt'):
        line = line.strip()
        line_dict = line.split(' ')
        line_dict = line_dict[1: len(line_dict)]
        line_out = ' '.join(''.join(line_dict))
        with open('./data/output/chinese.txt', 'a') as chinese_file:
            chinese_file.write(line_out)
            chinese_file.write('\n')

def generator_error_pinyin():
    for line in open('./data/input/ref_phone.txt'):
        line_dict_out = []
        line = line.strip()
        line_dict = line.split(' ')
        line_dict = line_dict[1: len(line_dict)]
        for i in range(len(line_dict)):
            if i % 2 == 0:
                single = line_dict[i] + line_dict[i + 1][0: len(line_dict[i + 1]) - 1]
                line_dict_out.append(single)
        line_out = ' '.join(line_dict_out)
        with open('./data/output/pinyin_error.txt', 'a') as pinyin_error_file:
            pinyin_error_file.write(line_out)
            pinyin_error_file.write('\n')

def generator_true_pinyin():
    for line in open('./data/output/chinese.txt'):
        pinyin_line = []
        for i in range(len(line)):
            if i % 2 == 0:
                pinyin_line.append(''.join(lazy_pinyin(line[i])))
        pinyin_line_out = ' '.join(pinyin_line)
        with open('./data/output/pinyin_true.txt', 'a') as pinyin_true_file:
            pinyin_true_file.write(pinyin_line_out)
            pinyin_true_file.write('\n')







