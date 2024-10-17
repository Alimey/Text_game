import tkinter as tk

class ChoiceButtons:
  """Класс ChoiceButtons используется для создания 4 кнопок выбора

    Attributes
    ----------

    __frame - рамка размещения кнопок

    __buttons - массив из 4 кнопок типа tk.Button

    __progress_checker - объект класса ProgressChecker, ответственный за подсчет очков и переходов между раундами

    Methods
    -------

    __init__() - создание объекта класса

    __generate_buttons() - создание 4 объектов класса tk.Button

    __pack_all() - размещение кнопок на экране

    upload(textes) - обновление текста кнопок

    """
  def __init__(self, root, progress_checker):
    """Создание объекта класса:\n
    root - объект класса tk.Tk\n
    progress_checker - объект класса ProgressChecker
    """
    self.__frame = tk.Frame(root)
    self.__buttons = []
    self.__generate_buttons()
    self.__pack_all()
    self.__progress_checker = progress_checker

  def __generate_buttons(self):
    """Генерация 4 кнопок. Вызывается в методе __init__"""
    for i in range(4):
      button = tk.Button(self.__frame, bg="black", fg="white", width=57, height=2)
      self.__buttons.append(button)
  
  def __pack_all(self):
    """Размещение всех кнопок на экране. Вызывается в методе __init__"""
    self.__frame.pack(side="bottom", fill="x")
    self.__buttons[0].grid(row=0, column=0, sticky="nsew")
    self.__buttons[1].grid(row=0, column=1, sticky="nsew")
    self.__buttons[2].grid(row=1, column=0, sticky="nsew")
    self.__buttons[3].grid(row=1, column=1, sticky="nsew")
  
  def upload(self, textes):
    """Обновление текста кнопок:\n
    textes - массив строк, новых надписей на кнопках
    """
    for i in range(4):
      self.__buttons[i]["text"] = textes[i]
    self.__buttons[0]["command"] = lambda: self.__progress_checker.on_clicked(0)
    self.__buttons[1]["command"] = lambda: self.__progress_checker.on_clicked(1)
    self.__buttons[2]["command"] = lambda: self.__progress_checker.on_clicked(2)
    self.__buttons[3]["command"] = lambda: self.__progress_checker.on_clicked(3)
    





  