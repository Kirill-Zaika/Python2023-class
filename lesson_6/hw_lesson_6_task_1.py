# Візьміть дві задачі з попередніх уроків, перша легка по вирішенню(декілька стрічок),
# друга більш складна і перепишіть їх на функції. Памятайте про Атамарність та god object.
# Там де написано що користувач має щось ввести то перероблюємо на функція приймає.
# Подивіться може можна за допомогою функції спростити код. В домашку вставте будь ласка опис задачі
# (далі(один з наступних уроків) буде домашка вашу домашку покрити тестами, але ми трохи поміняємо варіанти).

# Hillel_Course_AQA_Podlinnov/Lesson_1/hw_lesson_1.py

# 7 Перевод з цельсія в фаренгейт:
# Напишіть програму, яка запитує в користувача кількість градусів в цельсіях і повертає в фаренгейтах.


print('№7 Перевод з цельсія в фаренгейт')


def inputing_degrees():
    temperature_c = float(input('Введіть кількість градусів в Цельсіях: '))
    return temperature_c


def temperature_convert():
    conversion_farenheit = (inputing_degrees() * 9 / 5) + 32
    return conversion_farenheit


print(f'Кількість градусів в Фаренгейтах = {temperature_convert()}')
