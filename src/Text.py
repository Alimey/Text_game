import tkinter as tk
from Constants import *

class TextDisplayer:
  """Класс TextDisplayer используется для посимвольного вывода текста на экран

    Attributes
    ----------

    __root - Собственно, окно приложения

    __messages - массив выведенных строк

    Methods
    -------

    __init__() - создание объекта класса

    add_message(message, new_page) - очищение экрана и вывод нового сообщения

    __play_message(message, i = 0) - рекурсия для посимвольного вывода сообщения

    """
  def __init__(self, root):
    """Создание объекта класса\n
    root - объект класса tk.Tk
    """
    self.__root = root
    self.__messages = []
  
  def add_message(self, message, new_page):
    """Очищение экрана и вывод нового сообщения на экран\n
    message - строка, которую надо вывести\n
    new_page - bool, нужно ли очищать экран
    """
    if (new_page):
      for l in self.__messages:
        l.destroy()
      self.__messages.clear()
    label = tk.Label(text="", bg="black", fg="white", font=("Courier", 13), justify="left", wraplength=750)
    label.pack(side="top", anchor="w")
    self.__messages.append(label)
    self.__play_message(message)

  def __play_message(self, message, i = 0):
    """Посимвольный рукурсивный вывод строки\n
    message - строка для вывода\n
    i = 0 - символ, который выводится на данном шаге
    """
    if (i < len(message)):
      self.__messages[len(self.__messages) - 1]["text"] += message[i]
      self.__root.after(MESSAGE_SPEED, lambda: self.__play_message(message, i=i+1))
    