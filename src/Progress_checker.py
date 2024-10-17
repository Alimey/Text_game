import tkinter as tk
from Constants import *

class ProgressChecker:
  """Класс ProgressChecker используется для контроля процесса игры и подсчета очков. Ему передает управление
  объект класса Window.

    Attributes
    ----------

    __root - Собственно, окно приложения

    __text_displayer - объект класса TextDisplayer, ответственный за вывод текста

    __ans_for_buttons - массив очков, соответствующих кнопкам

    __score - очки игрока

    Methods
    -------

    __init__() - создание объекта

    __switch_on(buttons, text_displayer, root) - включение контроля раундов

    on_clicked(i) - метод реакции нажатия на клавишу i

    __final() - вывод на экран отметки и конечного сообщения

    """
  
  def __init__(self):
    """Создание объекта класса"""
    self.__ans_for_buttons = []
    self.__score = 0
  
  def switch_on(self, buttons, text_displayer, root):
    """Активация контроля процесса игры.
    На кнопках появляется текст, устанавливаются ответы для кнопок.\n
    buttons - объект класса ChoiceButtons\n
    text_displayer - объект класса TextDisplayer\n
    root - объект класса tk.Tk
    """
    self.__buttons = buttons
    self.__text_displayer = text_displayer
    self.round = 0
    buttons.upload(BUTTONS[0])
    self.__root = root
    self.__ans_for_buttons = ANS_FOR_BUTTONS[0]
  
  def on_clicked(self, i):
    """Реакция на нажатие i-ой кнопки.
    Подсчет очков, вывод реакции на нажатие, после чего ожидание нового нажатия клавиши для перехода
    к следующему раунду.\n
    Если раунд был последним, запуск __final().
    """
    self.__text_displayer.add_message(REACTIONS[self.round][i], False)
    self.__score += self.__ans_for_buttons[i]
    self.round += 1
    if self.round == AMOUNT_OF_ROUNDS:
      self.__root.unbind('<Key>')
      self.__root.bind('<Key>', lambda event: self.__final())
      return
    self.__buttons.upload(BUTTONS[self.round])
    self.__ans_for_buttons = ANS_FOR_BUTTONS[self.round]
    self.__root.unbind('<Key>')
    self.__root.bind('<Key>', lambda event: self.__text_displayer.add_message(ROUND_MESSAGES[self.round], True))

  def __final(self):
    """Выставление отметки по значению score:\n
    score <= 0: Неуд\n
    0 < score < 5: Уд\n
    5 <= score < 8: Хор\n
    8 <= score <= 10: Отл\n
    Ожидание нажатия клавиши для завершения игры.
    """
    if self.__score <= 0:
      self.__text_displayer.add_message(FINAL_MESSAGES[0], True)
    elif self.__score < 5:
      self.__text_displayer.add_message(FINAL_MESSAGES[1], True)
    elif self.__score < 8:
      self.__text_displayer.add_message(FINAL_MESSAGES[2], True)
    else:
      self.__text_displayer.add_message(FINAL_MESSAGES[3], True)
    self.__root.unbind('<Key>')
    self.__root.bind('<Key>', lambda event: self.__root.destroy())
