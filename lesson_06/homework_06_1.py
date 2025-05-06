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

# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

received_word = input('Enter any word with letter "h":\n')
counter = 1

for k in received_word:
    if k == 'h' or k == 'H':
        print('In your word present "h" or "H" letter')
        break
    if k != 'h' or k != 'H':
        counter += 1
    if len(received_word) - 1 == counter:
        received_word = input('Write another word, because in previous word absent letter "h" or "H"\n')
