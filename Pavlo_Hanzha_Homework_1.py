# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello}, {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
_storona = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = _storona + storona_2 + storona_3 + storona_4
print(perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""

apples_tree = 4
pear_tree = apples_tree + 5
plum_tree = apples_tree - 2
print("У саду посадили", apples_tree, "яблуні. Груш", pear_tree, ", а слив", plum_tree, ".")
print("Скільки всього дерев посадили в саду?")
print("Всього в саду було", apples_tree + pear_tree + plum_tree, "дерев")


# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""


temperature_before_afternoon = 5
temperature_after_afternoon = temperature_before_afternoon - 10
temperature_in_the_evening = temperature_after_afternoon + 4
print("До обіда температура повітря була на", temperature_before_afternoon, "градусів вище нуля.")
print("Після обіду температура була", temperature_after_afternoon)
print("Надвечір температура була", temperature_in_the_evening, ".")
print("Яка була температура надвечір?")
print(temperature_in_the_evening)


# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""


boys = 24
girls = boys // 2
print("Взагалі у театральному гуртку -", boys, "хлопчики, а дівчаток -", girls, ".")
print("1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.")
print("Скількі сьогодні дітей у театральному гуртку?")
print((boys - 1) + (girls - 2))

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""

# Перший варіант як я зрозумів умови задачі
book_1 = 8
book_2 = book_1 + 2
book_3 = book_1 / 2 + book_2
print("Перша книжка коштує", book_1, "грн., друга", book_2, "а третя", book_3)
print("Скільки будуть коштувати усі книги, якщо купити по одному примірнику?")
print(book_1 + book_2 + book_3)


# Другий варіант як я зрозумів умови задачі
book_1 = 8
book_2 = book_1 + 2
book_3 = book_1 / 2 + book_2 / 2
print("Перша книжка коштує", book_1, "грн., друга", book_2, "а третя", book_3)
print("Скільки будуть коштувати усі книги, якщо купити по одному примірнику?")
print(book_1 + book_2 + book_3)
