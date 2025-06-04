"""Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть
його середній бал.

Як робити домашне завдання в Git

ОБОВ’ЯЗКОВО створити нову гілку
Виконати ДЗ в окремій папці homework_<#lesson>.py
Закомітити створений код**
Відправте свої зміни до вашого репозиторію
Створити ПУЛ-РЕКВЕСТ у власний репозиторій У ГІЛКУ main"""

from homeworks import (
    average_score_int
)


class Students():

    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score_int(average_score)

    def change_average_score(self):
        self.average_score = input('Enter new average score for this student: \n')

student_nikolay = Students('Nikolay', 'Sergiyenko', '21', '7,8,6,5,4,6,7,8')

print(f'Name - {student_nikolay.name} \n'
      f'Surname - {student_nikolay.surname} \n'
      f'Age - {student_nikolay.age} \n'
      f'Average score - {student_nikolay.average_score} \n')

student_nikolay.change_average_score()
print(f'Name - {student_nikolay.name} \n'
      f'Surname - {student_nikolay.surname} \n'
      f'Age - {student_nikolay.age} \n'
      f'Average score - {student_nikolay.average_score} \n')
