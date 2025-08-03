import csv
from pathlib import Path

parent_directory =  Path('C:/Users/jhanz/aqa.python.lessons/aqa.python.lessons')
path_csv = 'C:/Users/jhanz/aqa.python.lessons/aqa.python.lessons/lesson_13/csv/uniques_rows.csv'

# directories = [f for f in parent_directory.iterdir() if f.is_dir()]
#
#
# print("List of directories:")
# for directory in directories:
#     print(directory)
#
#
# files = [f for f in parent_directory.iterdir() if f.is_file()]
#
# print("list of file")
# for file in files:
#     print(file)

# extension = '.py'
#
# file_with_extension = [f for f in parent_directory.iterdir() if f.suffix == extension]
#
# print('list with file suffix ".py"')
# for end_file in file_with_extension:
#     print(end_file)
# for item in parent_directory.iterdir():
#     print(item)

# current_directory = Path.cwd()
# print(f"path current directory is : {current_directory}")
#
# home_directory = Path.home()
#
# print(f'path for home directory: {home_directory}')

# with open('random.csv', 'r', encoding='utf-8') as f:
#     content = f.read()
#     print(content)

# with open('random.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(', '.join(row))
list_with_data_for_hm = []
with open('random.csv', newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        list_with_data_for_hm.append(row)

list_with_data_for_hm_2 = []
with open('random-michaels.csv', newline="") as csvfile_2:
    reader_2 = csv.reader(csvfile_2)
    for row_2 in reader_2:
        list_with_data_for_hm_2.append(row_2)

both_list = list_with_data_for_hm + list_with_data_for_hm_2

uniques_row_in_list = list({tuple(row) for row in both_list})


with open(path_csv, 'w', newline='', encoding='utf-8') as csvfile_3:
    writer = csv.writer(csvfile_3)
    writer.writerows(uniques_row_in_list)


print(list_with_data_for_hm)
print(list_with_data_for_hm_2)
