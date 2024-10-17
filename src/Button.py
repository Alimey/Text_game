import tkinter as tk

class ChoiceButtons:
  def __init__(self, root, progress_checker):
    self.__frame = tk.Frame(root)
    self.__buttons = []
    self.__generate_buttons()
    self.__pack_all()
    self.__progress_checker = progress_checker

  def __generate_buttons(self):
    for i in range(4):
      button = tk.Button(self.__frame, bg="black", fg="white", width=57, height=2)
      self.__buttons.append(button)
  
  def __pack_all(self):
    self.__frame.pack(side="bottom", fill="x")
    self.__buttons[0].grid(row=0, column=0, sticky="nsew")
    self.__buttons[1].grid(row=0, column=1, sticky="nsew")
    self.__buttons[2].grid(row=1, column=0, sticky="nsew")
    self.__buttons[3].grid(row=1, column=1, sticky="nsew")
  
  def upload(self, textes):
    for i in range(4):
      self.__buttons[i]["text"] = textes[i]
    self.__buttons[0]["command"] = lambda: self.__progress_checker.on_clicked(0)
    self.__buttons[1]["command"] = lambda: self.__progress_checker.on_clicked(1)
    self.__buttons[2]["command"] = lambda: self.__progress_checker.on_clicked(2)
    self.__buttons[3]["command"] = lambda: self.__progress_checker.on_clicked(3)
    





  