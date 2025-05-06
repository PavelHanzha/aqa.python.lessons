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
