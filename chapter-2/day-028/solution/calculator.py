# tkinter for pyqt5 ??
from tkinter import * 

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Calculator!")
        self.userInput = Text(self.master, width=100, height=2, bg='black', fg='lightblue')
        self.userInput.place(x=0, y=0)
        self.userInput.pack(side=TOP, fill=X)
        self.createButtons(self.master)
        self.master.geometry('410x300')
        self.master.mainloop()
        
    def createButtons(self, master):
        self.one = Button(master, text=1, width=10, height=2, bg='lightblue', fg='gray', command = lambda: self.concatChar(1)).place(x=15, y=180)
        self.two = Button(master, text=2, width=10, height=2, bg='lightblue', fg='gray', command = lambda: self.concatChar(2)).place(x=105, y=180)
        self.three = Button(master, text=3, width=10, height=2, bg='lightblue', fg='gray', command = lambda: self.concatChar(3)).place(x=195, y=180)
        self.four = Button(master, text=4, width=10, height=2, bg='lightblue', fg='gray', command = lambda: self.concatChar(4)).place(x=15, y=120)
        self.five = Button(master, text=5, width=10, height=2, bg='lightblue', fg='gray', command = lambda: self.concatChar(5)).place(x=105, y=120)
        self.six = Button(master, text=6, width=10, height=2, bg='lightblue', fg='gray', command = lambda: self.concatChar(6)).place(x=195, y=120)
        self.seven = Button(master, text=7, width=10, height=2, bg='lightblue', fg='gray', command = lambda:  self.concatChar(7)).place(x=15, y=60)
        self.eight = Button(master, text=8, width=10, height=2, bg='lightblue', fg='gray', command = lambda: self.concatChar(8)).place(x=105, y=60)
        self.nine = Button(master, text=9, width=10, height=2, bg='lightblue', fg='gray', command = lambda:  self.concatChar(9)).place(x=195, y=60)
        self.zero = Button(master, text=0, width=10, height=2, bg='lightblue', fg='gray', command = lambda: self.concatChar(0)).place(x=15, y=240)
        self.plus = Button(master, text='+', width=10, height=2, bg='lightblue', fg='gray', command = lambda: self.concatChar('+')).place(x=285, y=180)
        self.minus = Button(master, text='-', width=10, height=2, bg='lightblue', fg='gray', command = lambda: self.concatChar('-')).place(x=285, y=60)
        self.multiply = Button(master, text='*', width=10, height=2, bg='lightblue', fg='gray', command = lambda: self.concatChar('*')).place(x=285, y=120)
        self.divide = Button(master, text='/', width=10, height=2, bg='lightblue', fg='gray', command = lambda: self.concatChar('/')).place(x=285, y=60)
        self.equals = Button(master, text='=', width=22, height=2, bg='lightblue', fg='gray', command = lambda: self.evaluate()).place(x=200, y=240)
        self.c = Button(master, text='AC', width=10, height=2, bg='lightblue', fg='gray', command = lambda: self.clear()).place(x=105, y=240)
    def clear(self):
        self.userInput.delete('1.0', END)

    def concatChar(self, c):
        self.userInput.insert(END, c)

    def evaluate(self):
        answer = eval(self.userInput.get("1.0", "end-1c"))
        self.clear()
        self.concatChar(answer)


if __name__ == '__main__':
    root = Tk()
    calc = Calculator(root)