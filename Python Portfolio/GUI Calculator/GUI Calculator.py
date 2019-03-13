# GUI Calculator
#Tyson Vorwaller
# Import everything from tkinter module 
from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.equation = ""
        root.attributes("-alpha", 0.7)
    def create_widgets(self):
        self.display = Text(self, height=3, width=22, wrap=WORD,)
        self.display.grid(row=1, column=1, columnspan=4, sticky=W)
        self.display.configure(bg = "black")
        self.display.configure(fg = "white")
        
        self.seven = Button(self, text="7", width=5, height=2, command=self.seven)
        self.seven.grid(row=2, column=1, sticky=W)
        self.seven.configure(bg = "black")
        self.seven.configure(fg = "white")
        self.eight = Button(self, text="8", width=5, height=2, command=self.eight)
        self.eight.grid(row=2, column=2, sticky=W)
        self.eight.configure(bg = "black")
        self.eight.configure(fg = "white")
        self.nine = Button(self, text="9", width=5, height=2, command=self.nine)
        self.nine.grid(row=2, column=3, sticky=W)
        self.nine.configure(bg = "black")
        self.nine.configure(fg = "white")
        self.divide = Button(self, text="/", width=5, height=2, command=self.divide)
        self.divide.grid(row=2, column=4, sticky=W)
        self.divide.configure(bg = "black")
        self.divide.configure(fg = "white")

        self.four = Button(self, text="4", width=5, height=2, command=self.four)
        self.four.grid(row=3, column=1, sticky=W)
        self.four.configure(bg = "black")
        self.four.configure(fg = "white")
        self.five = Button(self, text="5", width=5, height=2, command=self.five)
        self.five.grid(row=3, column=2, sticky=W)
        self.five.configure(bg = "black")
        self.five.configure(fg = "white")
        self.six = Button(self, text="6", width=5, height=2, command=self.six)
        self.six.grid(row=3, column=3, sticky=W)
        self.six.configure(bg = "black")
        self.six.configure(fg = "white")
        self.multiply = Button(self, text="*", width=5, height=2, command=self.multiply)
        self.multiply.grid(row=3, column=4, sticky=W)
        self.multiply.configure(bg = "black")
        self.multiply.configure(fg = "white")

        self.one = Button(self, text="1", width=5, height=2, command=self.one)
        self.one.grid(row=4, column=1, sticky=W)
        self.one.configure(bg = "black")
        self.one.configure(fg = "white")
        self.two = Button(self, text="2", width=5, height=2, command=self.two)
        self.two.grid(row=4, column=2, sticky=W)
        self.two.configure(bg = "black")
        self.two.configure(fg = "white")
        self.three = Button(self, text="3", width=5, height=2, command=self.three)
        self.three.grid(row=4, column=3, sticky=W)
        self.three.configure(bg = "black")
        self.three.configure(fg = "white")
        self.subtract = Button(self, text="-", width=5, height=2, command=self.subtract)
        self.subtract.grid(row=4, column=4, sticky=W)
        self.subtract.configure(bg = "black")
        self.subtract.configure(fg = "white")

        self.zero = Button(self, text="0", width=5, height=2, command=self.zero)
        self.zero.grid(row=5, column=1, sticky=W)
        self.zero.configure(bg = "black")
        self.zero.configure(fg = "white")
        self.clear = Button(self, text="C", width=5, height=2, command=self.clear)
        self.clear.grid(row=5, column=2, sticky=W)
        self.clear.configure(bg = "black")
        self.clear.configure(fg = "white")
        self.solve = Button(self, text="=", width=5, height=2, command=self.solve)
        self.solve.grid(row=5, column=3, sticky=W)
        self.solve.configure(bg = "black")
        self.solve.configure(fg = "white")
        self.add = Button(self, text="+", width=5, height=2, command=self.add)
        self.add.grid(row=5, column=4, sticky=W)
        self.add.configure(bg = "black")
        self.add.configure(fg = "white")

    def zero(self):
        self.display.insert(END, 0)
        self.equation += "0"

    def one(self):
        self.display.insert(END, 1)
        self.equation += "1"

    def two(self):
        self.display.insert(END, 2)
        self.equation += "2"

    def three(self):
        self.display.insert(END, 3)
        self.equation += "3"

    def four(self):
        self.display.insert(END, 4)
        self.equation += "4"

    def five(self):
        self.display.insert(END, 5)
        self.equation += "5"

    def six(self):
        self.display.insert(END, 6)
        self.equation += "6"

    def seven(self):
        self.display.insert(END, 7)
        self.equation += "7"

    def eight(self):
        self.display.insert(END, 8)
        self.equation += "8"

    def nine(self):
        self.display.insert(END, 9)
        self.equation += "9"

    def add(self):
        self.display.insert(END, " + ")
        self.equation += "+"

    def subtract(self):
        self.display.insert(END, " - ")
        self.equation += "-"

    def multiply(self):
        self.display.insert(END, " * ")
        self.equation += "*"

    def divide(self):
        self.display.insert(END, " / ")
        self.equation += "/"

    def clear(self):
        self.display.delete(0.0, END)
        self.equation = ""

    def solve(self):
        try:
            answer = eval(self.equation)
        except:
            answer = "ERROR"
        self.display.insert(END, " = ")
        self.display.insert(END, answer)


root = Tk()
root.title("Calculator GUI")

app = Application(root)

root.mainloop()



