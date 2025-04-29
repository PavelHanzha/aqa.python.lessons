adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==

""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace('\n', ' ')  # Instead 'transfer to new line'
# write 'space'


# task 02 ==
""" Замініть .... на пробіл
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace('....', '')  # Instead '....' write ' '

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.strip() # Delete spaces in start and end string
print(adwentures_of_tom_sawer)
adwentures_of_tom_sawer = adwentures_of_tom_sawer.split()  # Convert string in list
adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer)  # Convert list in string without unnecessary spaces
print(adwentures_of_tom_sawer)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

print(adwentures_of_tom_sawer.count('h'))
# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count_upper_word = 0
for upper_word in adwentures_of_tom_sawer:
    if upper_word.istitle():
        count_upper_word += 1
print(count_upper_word)
# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
# First solution
cut_first_word_Tom = adwentures_of_tom_sawer.replace('Tom', '', 1) # Cut first word 'Tom'
index_second_word_Tom = cut_first_word_Tom.index('Tom') + 3 # Check index second word 'Tom'
print(index_second_word_Tom) # Display second word 'Tom'

# Second solution
change_Tom_word = (adwentures_of_tom_sawer.replace('Tom', 'asas',1)
                   .replace('Tom', 'axax', 1).replace('asas', 'Tom'))
# Change first word 'Tom', then change seconde word 'Tom' to unique word and then back first changed word
index_second_word_Tom2 = change_Tom_word.index('axax') # Check index second word 'Tom'
print(index_second_word_Tom2) # Display second word 'Tom'
# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
#first solution
print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for s in adwentures_of_tom_sawer_sentences:
    if s.startswith('By the time'):
        print(True)
    else:
        print(False)


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
counter = len(adwentures_of_tom_sawer_sentences) - 1
list_last_sentences = adwentures_of_tom_sawer_sentences[counter].split()
number_words_in_last_senteces = len(list_last_sentences)
print(number_words_in_last_senteces)
