import re

# """
# \d = 0-9 только числа
# \D = выводит все кроме чисел
# \w = [A-Z a-z]
# \W = все символы кроме букв
# \s = выводит пробелы
# \S = выводит всё кроме пробелов
# """
#
# file_path ='class_mock_data.txt'
# result_file_path = 'result.txt'
# file_read = open(file_path, mode='r', encoding='Latin1')
# file_write = open(result_file_path, mode='w')
# class_text = file_read.read()
# seacher = r'@\w+.\w+[a-z]+'
# result_all = re.findall(seacher,class_text)
#
# for i in result_all:
#     print(i)
#     file_write.write(i + ' \n')
# print(f'Result: {str(len(result_all))}')
#



"""
\d = 0-9 только числа
\D = выводит все кроме чисел
\w = [A-Z a-z]
\W = все символы кроме букв 
\s = выводит пробелы
\S = выводит всё кроме пробелов
"""
file_path2 = 'class_mock_data.txt'
result_file_path2 = 'type_file.txt'
file_read2 = open(file_path2, mode='r', encoding='Latin1')
file_write2 = open(result_file_path2, mode='w')
class_text2 = file_read2.read()
seacher2 = r"[A-Z]+[a-z]+\w+[.]+[a-z]+[0-9]|" \
            r"[A-Z]+[a-z]+\w+[.]+[a-z]+|" \
            r"[A-Z]+[a-z]+[.]+[a-z]+[0-9]|" \
            r"[A-Z]+[a-z]+[.]+[a-z]+|" \
            r"[A-Z]+[.]+[a-z]+|" \
            r"[A-Z]+[.]+[a-z]+[0-9]"
result_all2 = re.findall(seacher2,class_text2)

for i in result_all2:
    print(i)
    file_write2.write(i + ' \n')
print(f'Result: {str(len(result_all2))}')
