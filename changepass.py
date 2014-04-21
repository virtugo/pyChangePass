# coding=Windows-1251

# --------------------------------------------------
# Вбиваем логин, прога генерирует пароль, меняет его
# и показывает новый пароль для удобства
# --------------------------------------------------

import subprocess
import os
from random import randint # подключаем модуль с функцией рандома

# Если есть файл с последним именем юзера
if os.path.exists('name.txt'):
    if os.path.isfile('name.txt'):
        fn = open('name.txt')
        lastName = fn.read() # читаем имя юзера
        fn.close()
        inputName = input('Имя пользователя (Enter для ' + lastName + '): ')
        # ------------------------------------------------------------------
        if inputName == '': # Если не ввели имя юзера
            inputName = lastName # используем последнее введенное
    else:
        inputName = input('Имя пользователя: ')
else:
    inputName = input('Имя пользователя: ')
print() # пустая строка

# Записываем в файл последнее имя юзера
fn = open('name.txt', 'w' )
fn.write(inputName)
fn.close()

inputPass = input('Новый пароль (Enter для генерации): ')
print() # пустая строка

# если ввели пароль, присваиваем конечный результат
if inputPass != '':
    genPass = inputPass
    f = open('pass.txt', 'w' )
    f.write(inputPass)
    f.close()
else: # если пароль не ввели, генерируем его
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # пишем в файл по букве
    f = open('pass.txt', 'w' )
    i = randint(0,23) # Заглавная
    f.write(a[i])
    i = randint(0,23) # малая
    f.write(b[i])
    i = randint(0,23) # малая
    f.write(b[i])
    i = randint(2,9) # цифра от 2 до 9 включительно
    f.write(str(i))
    i = randint(2,9) # цифра от 2 до 9 включительно
    f.write(str(i))
    i = randint(2,9) # цифра от 2 до 9 включительно
    f.write(str(i))
    i = randint(0,23) # малая
    f.write(b[i])
    f.close()
    # читаем из файла конечный результат
    f = open('pass.txt')
    genPass = f.read()
    f.close()

# меняем пароль
pInput = 'net user ' + inputName + ' ' + genPass + ' /DOMAIN'
p = subprocess.Popen(pInput, shell=True, stdout = subprocess.PIPE)
out1 = p.stdout.read()

# выводим ответ системы
print (out1.decode('CP866'))
print('-------------------------------------') # пустая строка
input('Enter для выхода...') # не закрываем консоль

os.startfile('pass.txt') # открываем пароль в блокноте, чтобы было удобнее копировать в письмо юзеру
