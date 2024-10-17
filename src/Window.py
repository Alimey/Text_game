import tkinter as tk
from Button import *
from Text import *
from Constants import *
from Progress_checker import *

class Window:
  def __init__(self):
    self.__root = tk.Tk()
    self.__create_base()
    self.__text_displayer = TextDisplayer(self.__root)
    self.__progress_checker = ProgressChecker()
    self.__buttons = ChoiceButtons(self.__root, self.__progress_checker)

  def __create_base(self):
    self.__root.title("Однажды на зимней сессии...")
    self.__root.geometry("800x600")
    self.__root.configure(bg="black")
    self.__root.resizable(False, False)
  
  def start(self):
    self.__root.bind('<Key>', self.__start_messaging)
    self.__root.mainloop()
  
  def __start_messaging(self, event):
    self.__text_displayer.add_message(ROUND_MESSAGES[0], False)
    self.__progress_checker.switch_on(self.__buttons, self.__text_displayer, self.__root)
    self.__root.unbind('<Key>')
    self.__root.bind('<Key>', lambda event: self.__text_displayer.add_message(ROUND_MESSAGES[1], True))