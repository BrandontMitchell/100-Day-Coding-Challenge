# tkinter for pyqt5 ??
from tkinter import * 

class Calculator:
    def __init__(self, master):

        # master is 'root' from tkinter, and is required upon __init__
        self.master = master
        self.master.title("Python Calculator!") # Change title to whatever!
        self.master.geometry('410x300')         # Changing geometry is up to you
        self.master.mainloop()                  # also required to run tkinter files
        
    def createButtons(self, master):
        pass

    def clear(self):
        pass

    def concatChar(self, character):
        pass

    def evaluate(self):
        pass


# main run of program
if __name__ == '__main__':
    root = Tk()
    calc = Calculator(root)