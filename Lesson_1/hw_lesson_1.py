# 1 Арифметичні операції:
#Написати програму, яка зчитує два числа та виводить їхню суму, різницю, добуток та частку.

print('№1 Арифметичні операції')
variable_1 = int(input('Перше число: '))
variable_2 = int(input('Друге число: '))
print('Сума =', variable_1 + variable_2)
print('Різниця =', variable_1 - variable_2)
print('Добуток =', variable_1 * variable_2)
print('Частка =', variable_1 / variable_2)
print() # Для відокремлення задач

# 2 Залишок від ділення:
# Користувач вводить два числа. Вивести залишок від ділення першого числа на друге.

print('№2 Залишок від ділення')
number_1 = int(input('Введіть перше число: '))
number_2 = int(input('Введіть друге число: '))
result = number_1 % number_2
print('Залишок від ділення =',result)
print() # Для відокремлення задач

# 3 Цілочисельне ділення:
# Користувач вводить два числа. Вивести, скільки разів перше число ділиться на друге без залишку.

print('№3 Цілочисельне ділення ')
first_number = int(input('Введіть перше число: '))
second_number = int(input('Введіть друге число: '))
print('Кількість разів де перше число ділиться на друге без залишку =', first_number // second_number)
print() # Для відокремлення задач

# 4 Перетворення стрічки у число:
# Користувач вводить рядок, який складається з цифр. Програма повинна перетворити його на число та вивести.

print('№4 Перетворення стрічки у число')
numbers = input('Введіть рядок, який складається з цифр: ')
transformation_int = int(numbers)
print('Вивід:', numbers)
print() # Для відокремлення задач

# 5 Стрічкова конкатенація + математика:
# Користувач вводить два числа. Програма повинна вивести два прінти: перший — їхню суму,
# другий об'єднати їх. Якщо в нас числа 5 та 4, то результат повинен бути 9 та 54.

print('№5 Стрічкова конкатенація + математика')
number_one = input('Введіть перше число: ')
number_two = input('Введиіть друге число: ')
number_one_float = float(number_one)
number_two_float = float(number_two)
result_sum = number_one_float + number_two_float
print('Сума чисел =', result_sum)
result_adding = number_one + number_two
print('Об`єднання чисел =',result_adding)
print() # Для відокремлення задач

# 6 Вік користувача:
# Запитати у користувача його рік народження, ім'я та який зараз рік (три змінні)
# та вивести на екран два прінти: ім'я та скільки років користувачу.

print('№6 Вік користувача')
birth_date = int(input('Введіть рік Вашого народження: '))
name = input('Введіть Ваше ім`я: ')
current_year = int(input('Введіть поточний рік: '))
age = current_year - birth_date
print('Ім`я:', name)
print('Ваш вік:', age)
print() # Для відокремлення задач

# 7 Перевод з цельсія в фаренгейт:
# Напишіть програму, яка запитує в користувача кількість градусів в цельсіях і повертає в фаренгейтах.

print('№7 Перевод з цельсія в фаренгейт')
temperature_c = float(input('Введіть кількість градусів в Цельсіях: '))
conversion_farenheit = (temperature_c * 9/5)+32
print('Кількість градусів в Фаренгейтах =',conversion_farenheit)
print() # Для відокремлення задач

# 8 Перевод з фаренгейта в цельсій:
# Напишіть програму, яка запитує в користувача кількість градусів в фаренгейтах і повертає в цельсіях.
# Вам може здатися, що ця задача така ж, як попередня, але будьте уважні і перевірте результат вручну.

print('№8 Перевод з фаренгейта в цельсій')
temperature_farenheit = float(input('Введіть кількість градусів в Фаренгейтах: '))
conversion_celsius = (temperature_farenheit - 32) * 5/9
print('Кількість градусів в Цельсіях =',conversion_celsius)
print() # Для відокремлення задач

# 9 Теорема Піфагора:
# Запитайте у користувача довжини катетів та виведіть на екран довжину гіпотенузи.
# Трикутник рівнобедрений. Що б взвести в степінь ставимо два рази множення
# два в степені три буде так 2**3, квадратний корінь з двух буде 2**(1/2)

print('№9 Теорема Піфагора')
leg_a = float(input('Введіть довжину катета А: '))
leg_b = float(input('Введіть довжину катета B: '))
hypotenuse_c = (leg_a**2 + leg_b**2)**(1/2)
print('Давжина гіпотенузи =', hypotenuse_c)
print() # Для відокремлення задач

# 10 Школярі та яблука
# n школярів ділять k яблук порівну, недільний залишок залишається в кошику.
# Скільки яблук дістанеться кожному школярові та скільки залишиться в кошику?
# Програма отримує на вхід числа n і k - цілі, додатні, не перевищують 10000.

print('№10 Школярі та яблука')
schoolchaild_n = int(input('Введіть кількість школярів: '))
apples_k = int(input('Введіть кількість яблук: '))
apples_for_each_schoolchild = apples_k // schoolchaild_n
print('Кількість яблук у кожного школяра:', apples_for_each_schoolchild)
apples_in_bascket = apples_k % schoolchaild_n
print('Кількість яблук що залишилась в кошику =', apples_in_bascket)
print() # Для відокремлення задач

# 11 Магазин канцелярських товарів
# Одного разу, відвідавши магазин канцелярських товарів, Вася купив X олівців, Y ручок та Z фломастерів. Відомо,
# що ціна ручки на 2 гривні більше ціни олівця та на 7 гривень менше ціни фломастера. Також відомо,
# що вартість олівця становить 3 гривні. Потрібно визначити загальну вартість покупки.
# Вхідні дані
# просимо користувача ввести три змінні
# кожне з яких не перевищує 109.
# Вихідні дані
# виведіть одне ціле число – вартість покупки в гривнях.
# приклад для перевірки програми 1
# ввів: 1 1 1
# отримав: 20

print('№11 Магазин канцелярських товарів')
pencil_x = int(input('Введіть кількість олівців: '))
pen_y = int(input('Введіть кількість ручок: '))
marker_z = int(input('Введіть кількість фломастерів: '))
pencil_coast = 3
pen_coast = 5
marker_coast = 12
price = (pencil_x * pencil_coast) + (pen_y * pen_coast) + (marker_z * marker_coast)
print('Загальна вартість покупки =', price)
print() # Для відокремлення задач

# 12 Циферблад
# Запитайте в користувача скільки хвилин пройшло з початку доби.
# Визначте, скільки годин і хвилин покаже електронний годинник в цей момент і поверніть йому результат (формататування тексту при ввиводі не важливе).
# приклад для перевірки програми 1
# користувач ввів:150
# користувач отримує: 2, 30
# приклад для перевірки програми 2
# користувач ввів:1441
# користувач отримує: 0, 1

print('№12 Циферблад')
minutes = int(input('Cкільки хвилин пройшло з початку доби: '))
time_houre = (minutes // 60) % 24
time_minutes = minutes % 60
print(time_houre, ':', time_minutes)
print() # Для відокремлення задач

# 13 Журавлики
# Петро, Катя та Сергій роблять з паперу журавликів. Разом вони зробили S журавликів.
# Скільки журавликів зробила кожна дитина, якщо відомо, що Петро та Сергій зробили однакову кількість журавликів,
# а Катя зробила в два рази більше журавликів, ніж Петро та Сергій разом.
# Вхідні дані
# Юзер вводить загальну кількість журавликів. Отримує три значення скільки зробив кожен (Петро, Катя та Сергій).

print('№13 Журавлики')
cranes = int(input('Загальна кількість журавликів: '))
katya = (cranes // 6)*4
petro = cranes // 6
sergey = cranes // 6
print('Петро зробив журавликів:',petro)
print('Катя зробила журавликів:',katya)
print('Сергій зробив журавликів:',sergey)
print() # Для відокремлення задач

# 14 Податки
# Прийшов час податків і вам треба написати програму що б допомогти відділу бугалтерії
# програма приймає від користувача його зарплату за 3 місяці та відсоток який він має сплатити.
# Виведіть на екран скільки треба сплатити податків за 3 місяці. Не забудьте ЄСВ(4422)

print('№14 Податки')
money = float(input('Введіть зарплату за 3 місяці: '))
percent = float(input('Введіть відсоток: '))
esv = 4422
pay = (money*(percent/100))+esv
print('До сплати:', pay)
print() # Для відокремлення задач