import os
import platform

def clear():
  command = "cls" if platform.system() == "Windows" else "clear"
  os.system(command)