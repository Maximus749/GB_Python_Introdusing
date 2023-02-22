# Модуль os
# Модуль os предоставляет множество функций для работы с операционной системой,
# причем их поведение, как правило, не зависит от ОС, поэтому программы остаются
# переносимыми. Для того, чтобы начать работать с данным модулем необходимо его
# импортировать в свою программу:
import os
# Познакомимся с базовыми функциями данного модуля:
# os.chdir(path)                                                                  # смена текущей директории.
# os.chdir('D:\Geek Brains\Python Projects\Introducing with Python\Lectures\
# Lesson_4\407_module_OS.py')
# os.getcwd()                                                                     # текущая рабочая директория
print(os.getcwd())                                                              # 'C:\Users\79190\PycharmProjects\webproject'
# ● os.path - является вложенным модулем в модуль os и реализует некоторые
# полезные функции для работы с путями, такие как:
# os.path.basename(path)                                                          # базовое имя пути
# print(os.path.basename('D:\Geek Brains\Python Projects\Introducing with Python\
# Lectures\Lesson_4\407_module_OS.py'))                                           #'407_module_OS.py'
# ● os.path.abspath(path) - возвращает нормализованный абсолютный путь.
# import os
print(os.path.abspath('407_module_OS.py'))                                      # 'C:/Users/79190/PycharmProjects/webproject/main.py'
# Это лишь малая часть возможностей модуля os.
