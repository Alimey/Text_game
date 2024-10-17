import tkinter as tk
from Button import *
from Text import *
from Constants import *
from Progress_checker import *

class Window:
  """Класс Window используется для создания и контроля окна игры

    Attributes
    ----------

    __root - Собственно, окно приложения

    __text_displayer - объект класса TextDisplayer, ответственный за вывод текста

    __progress_checker - объект класса ProgressChecker, ответственный за подсчет очков и переходов между раундами

    __buttons - объект класса ChoiceButtons, отвественный за 4 кнопки выбора

    Methods
    -------

    __init__() - создание объекта окна

    __create_base() - установка графических характеристик окна

    start() - альтернатива методу mainloop для удобства

    """
  def __init__(self):
    """Создание объекта класса

    Вызов функции create_base для установки графических характеристик.
    """
    self.__root = tk.Tk()
    self.__create_base()
    self.__text_displayer = TextDisplayer(self.__root)
    self.__progress_checker = ProgressChecker()
    self.__buttons = ChoiceButtons(self.__root, self.__progress_checker)

  def __create_base(self):
    """Установка графических характеристик окна"""
    self.__root.title("Однажды на зимней сессии...")
    self.__root.geometry("800x600")
    self.__root.configure(bg="black")
    self.__root.resizable(False, False)
  
  def start(self):
    """Альтернатива методу mainloop из tkinter
    Выводит на начальный экран сообщение и ожидает нажатия любой клавиши для старта
    """
    self.__text_displayer.add_message(START_MESSAGE, False)
    self.__root.bind('<Key>', self.__start_messaging)
    self.__root.mainloop()
  
  def __start_messaging(self, event):
    """Выводит на экран начальное сообщение - предысторию.
    Подключает progress_checker для начала подсчета очков и контроля раундов.
    Ждет нажатия кнопки и запускает процесс игры.
    """
    self.__text_displayer.add_message(ROUND_MESSAGES[0], True)
    self.__progress_checker.switch_on(self.__buttons, self.__text_displayer, self.__root)
    self.__root.unbind('<Key>')
    self.__root.bind('<Key>', lambda event: self.__text_displayer.add_message(ROUND_MESSAGES[1], True))