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
