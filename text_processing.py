# -*- coding: utf-8 -*-

from pypinyin import lazy_pinyin
import json

not_need_correction = ['jv', 'jvan', 'jve', 'jvn',
                       'qv', 'qvan', 'qve', 'qvn',
                       'xv', 'xvan', 'xve', 'xvn']

def writejson2file(data, filename):
    with open(filename, 'w') as outfile:
        data = json.dumps(data, indent=4, sort_keys=True)
        outfile.write(data)

def readjson(filename):
    with open(filename) as outfile:
        return json.load(outfile)

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

def generator_finally():
    for line in open('./data/output/chinese.txt'):
        line = line.replace('\n', ' ')
        with open('./data/output/chinese_finally.txt', 'a') as chinese_finally_file:
            chinese_finally_file.write(line)

    for line in open('./data/output/pinyin_error.txt'):
        line = line.replace('\n', ' ')
        with open('./data/output/pinyin_error_finally.txt', 'a') as pinyin_error_finally_file:
            pinyin_error_finally_file.write(line)

    for line in open('./data/output/pinyin_true.txt'):
        line = line.replace('\n', ' ')
        with open('./data/output/pinyin_true_finally.txt', 'a') as pinyin_true_finally_file:
            pinyin_true_finally_file.write(line)

def generator_error_statistics():
    with open('./data/output/pinyin_error_finally.txt') as pinyin_error_finally_file:
        pinyin_error_content = pinyin_error_finally_file.read()
        pinyin_error_list = pinyin_error_content.split(' ')

    with open('./data/output/pinyin_true_finally.txt') as pinyin_true_file:
        pinyin_true_content = pinyin_true_file.read()
        pinyin_true_list = pinyin_true_content.split(' ')

    true2error_statistics = {}
    error2true_statistics = {}
    for i in range(0, len(pinyin_error_list)):
        if pinyin_error_list[i] != pinyin_true_list[i] and pinyin_error_list[i] not in not_need_correction:
            true2error_statistics.setdefault(pinyin_true_list[i], {})
            true2error_statistics[pinyin_true_list[i]].setdefault(pinyin_error_list[i], 0)
            true2error_statistics[pinyin_true_list[i]][pinyin_error_list[i]] += 1

            error2true_statistics.setdefault(pinyin_error_list[i], {})
            error2true_statistics[pinyin_error_list[i]].setdefault(pinyin_true_list[i], 0)
            error2true_statistics[pinyin_error_list[i]][pinyin_true_list[i]] += 1

    writejson2file(true2error_statistics, './data/output/true2error_statistics.json')
    writejson2file(error2true_statistics, './data/output/error2true_statistics.json')

correction_table = {}
correction_table.setdefault('aaa', 'a')
correction_table.setdefault('ix', 'i')
correction_table.setdefault('eee', 'e')
correction_table.setdefault('iiiu', 'you')
correction_table.setdefault('iiio', 'yo')
correction_table.setdefault('iiin', 'yin')
correction_table.setdefault('iiie', 'ye')
correction_table.setdefault('iiia', 'ya')
correction_table.setdefault('iii', 'yi')
correction_table.setdefault('ooo', 'o')
correction_table.setdefault('iz', 'i')
correction_table.setdefault('uuun', 'wen')
correction_table.setdefault('uuui', 'wei')
correction_table.setdefault('uuu', 'u')
correction_table.setdefault('aaa', 'a')
correction_table.setdefault('vvv', 'yu')
correction_table_special_keys = correction_table.keys()

error2true_statistics = readjson('./data/output/error2true_statistics.json')

for key in error2true_statistics:
    if key not in correction_table_special_keys:
        correction_table.setdefault(key, list(error2true_statistics[key].keys()))

writejson2file(correction_table, './data/output/correction_table.json')

if __name__ == '__main__':
    # generator_chinese()
    # generator_error_pinyin()
    # generator_true_pinyin()
    # generator_finally()
    # generator_error_statistics()
    pass