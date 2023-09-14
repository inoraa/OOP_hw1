import os

base_path = os.getcwd()
output_file = 'OOP txtfile/combined.txt'

file_list = [filename for filename in os.listdir(base_path) if filename.endswith('.txt')]
file_len = {}
for filename in file_list:
    full_path = os.path.join(base_path, filename)

    with open(full_path, 'r', encoding='utf-8') as f:
        file_contents = f.read()
        file_len[filename] = len(file_contents)

file_len_sort = sorted(file_len.items(), key=lambda x: x[1], reverse=True)

with open(output_file, 'w', encoding='utf-8') as f_combined:
    for filename, _ in file_len_sort:
        full_path = os.path.join(base_path, filename)

        with open(filename, 'r', encoding='utf-8') as f:
            file_contents = f.read()
            f_combined.write(f'Содержимое {filename}\n')
            f_combined.write(f'Всего строк: {len(file_contents.splitlines())}\n')
            f_combined.write(file_contents)
            f_combined.write('\n')
