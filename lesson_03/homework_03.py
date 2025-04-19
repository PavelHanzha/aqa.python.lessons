# first solution
alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."\n\n\n'''
print(alice_in_wonderland)
# \n\n\n this need for more comfortable read result


# second solution
alice_in_wonderland = (f'"Would you tell me, please, which way I ought to go from here?"\n'
                       f'"That depends a good deal on where you want to get to," said the Cat.\n'
                       f'"I don\')t much care where ——" said Alice.\n'
                       f'"Then it doesn\'t matter which way you go," said the Cat.\n'
                       f'"—— so long as I get somewhere," Alice added as an explanation.\n'
                       f'"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."\n')
print(alice_in_wonderland)

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
print('Task 04 \n')
area_black_see = 436402
area_azov_see = 37800
area_both_see = area_black_see + area_azov_see

print("Площа Чорного моря становить", area_black_see, "км2, а площа Азовського")
print("моря становить", area_azov_see, "км2. Яку площу займають Чорне та Азов-")
print("ське моря разом?")
print(area_both_see)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print('Task 05 \n')
count_composition = 3
all_composition = 375291
composition3 = all_composition - 250449
composition1 = all_composition - 222950
composition2 = all_composition - composition1 - composition3
composition = [composition1, composition2, composition3]
name_composition = ['on first composition: ', 'on second composition: ', 'on third composition: ']

print("Мережа супермаркетів має", count_composition, "склади, де всього розміщено")
print(all_composition, "товар. На першому та другому складах перебуває")
print(composition1 + composition2, "товарів. На другому та третьому –", composition2 + composition3, "товарів.")
print("Знайдіть кількість товарів, що розміщені на кожному складі.")
print(name_composition[0], composition[0])
print(name_composition[1], composition[1])
print(name_composition[2], composition[2])

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print('Task 06 \n')
pay_for_one_month = 1179
price_computer = pay_for_one_month * 18
print(f'Михайло разом з батьками вирішили купити комп’ютер, ско-\n'
      f'риставшись послугою «Оплата частинами». Відомо, що сплачу-\n'
      f'вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть\n'
      f'вартість комп’ютера.\n')
print(price_computer, sep='\n')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print('Task 07 \n')
the_number_we_divide = [8019, 9907, 2789, 7248, 7128, 19224]
the_number_we_divide_by = [8, 9, 5, 6, 5, 9]
a = the_number_we_divide[0] % the_number_we_divide_by[0]
b = the_number_we_divide[1] % the_number_we_divide_by[1]
c = the_number_we_divide[2] % the_number_we_divide_by[2]
d = the_number_we_divide[3] % the_number_we_divide_by[3]
e = the_number_we_divide[4] % the_number_we_divide_by[4]
f = the_number_we_divide[5] % the_number_we_divide_by[5]
print('a =', a, '\nb =', b, '\nc =', c, '\nd =', d, '\ne =', e, '\nf =', f)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
print('Task 08 \n')
product = ['Big pizza', 'Middle pizza', 'Juice', 'Cake', 'Water']
product_count = [4, 2, 4, 1, 3]
product_price = [274, 218, 35, 350, 21]
amount_of_money_for_each_product = [product_count[0] * product_price[0], product_count[1] * product_price[1],
                                    product_count[2] * product_price[2], product_count[3] * product_price[3],
                                    product_count[4] * product_price[4], ]
print(list(zip(product, amount_of_money_for_each_product)))
print(amount_of_money_for_each_product[0] + amount_of_money_for_each_product[1] +
      amount_of_money_for_each_product[2] + amount_of_money_for_each_product[3] +
      amount_of_money_for_each_product[4])

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print('Task 09 \n')
photo_count = 232
count_photo_in_one_paper = 8
print('Count paper which need for all Igors photos:', photo_count // count_photo_in_one_paper)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
print('Task 10 \n')

distance_between_Kharkiv_and_Budapesht = 1600
count_gassoil = distance_between_Kharkiv_and_Budapesht // 100 * 9
print('1:', count_gassoil)
print('2:', count_gassoil // 48)
