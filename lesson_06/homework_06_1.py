# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True,
# інакше - False. Строку отримати за допомогою функції input()
#

received_text = input('Enter any text:\n')
length_unique_received_symbols = len(set(received_text))
print(len(set(received_text)))
if 10 < length_unique_received_symbols:
    print(True)
if 10 > length_unique_received_symbols:
    print(False)
#
# # Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# # (враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
#
# # 1st attempt via for
# # received_word = input('Enter any word with letter "h":\n')
# # counter = 1
# #
# # for k in received_word:
# #     if k == 'h' or k == 'H':
# #         print('In your word present "h" or "H" letter')
# #         break
# #     if k != 'h' or k != 'H':
# #         counter += 1
# #     if len(received_word) - 1 == counter:
# #         received_word = input('Write another word, because in previous word absent letter "h" or "H"\n')
#
# # 2nd attempt via while
#
while True:
    receive_word_2 = input('Enter any word with letter "h":\n')
    if 'h' in receive_word_2:
        print('Letter "h" present')
        break
    if 'H' in receive_word_2:
        print('Letter "H" present')
        break
    else:
        print('absent letter "h" or "H"')

# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. Напишіть код, який
# свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for k in lst1:
    if type(k) == str:
        lst2.append(k)
print(lst2)

# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

list_of_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 61, 43, 42, 64, 76, 87, 98, 45, 76, 45, 65, 456,
                  654, 34]
sum_numbers = 0
for k in list_of_number:
    if k % 2 == 0:
        sum_numbers = sum_numbers + k
print(sum_numbers)
