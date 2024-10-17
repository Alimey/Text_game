import tkinter as tk
from Constants import *

class TextDisplayer:
  def __init__(self, root):
    self.__root = root
    self.__messages = []
  
  def add_message(self, message, new_page):
    if (new_page):
      for l in self.__messages:
        l.destroy()
      self.__messages.clear()
    label = tk.Label(text="", bg="black", fg="white", font=("Courier", 13), justify="left", wraplength=750)
    label.pack(side="top", anchor="w")
    self.__messages.append(label)
    self.__play_message(message)

  def __play_message(self, message, i = 0):
    if (i < len(message)):
      self.__messages[len(self.__messages) - 1]["text"] += message[i]
      self.__root.after(MESSAGE_SPEED, lambda: self.__play_message(message, i=i+1))