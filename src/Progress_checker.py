import tkinter as tk
from Constants import *

class ProgressChecker:
  def __init__(self):
    self.__ans_for_buttons = []
    self.__score = 0
  
  def switch_on(self, buttons, text_displayer, root):
    self.__buttons = buttons
    self.__text_displayer = text_displayer
    self.round = 0
    buttons.upload(BUTTONS[0])
    self.__root = root
    self.__ans_for_buttons = ANS_FOR_BUTTONS[0]
  
  def on_clicked(self, i):
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
