# Python Final Project
# Name - Myo Mg Mg, Nickname - Chocolate, Date - 1/9/2022

from tkinter import *

# Create a calculator class
class Calculator:

    def __init__(self,calculator):
        self.calculator= calculator

        # Add tite to my calculator program
        calculator.title("Python Calculator")

        # Create a line where we display the equation
        self.equation = Entry(calculator, width=40, borderwidth=15)

        self.equation.grid(row=0, column=0, columnspan=4)

        self.Button()

    def Button(self):

        btn0 = self.AddButton(0)
        btn1 = self.AddButton(1)
        btn2 = self.AddButton(2)
        btn3 = self.AddButton(3)
        btn4 = self.AddButton(4)
        btn5 = self.AddButton(5)
        btn6 = self.AddButton(6)
        btn7 = self.AddButton(7)
        btn8 = self.AddButton(8)
        btn9 = self.AddButton(9)
        btn_add = self.AddButton("+")
        btn_sub = self.AddButton("-")
        btn_mult = self.AddButton("*")
        btn_div = self.AddButton("/")
        btn_clear = self.AddButton("C")
        btn_equal = self.AddButton("=")

        # Arrange the buttons into lists to show calculator rows
        row1 = [btn7, btn8, btn9, btn_add]
        row2 = [btn4, btn5, btn6, btn_sub]
        row3 = [btn1, btn2, btn3, btn_mult]
        row4 = [btn_clear, btn0, btn_equal, btn_div]

        # Assign each button to a particular location on the GUI
        r = 1
        for row in [row1, row2, row3, row4]:
            c = 0
            for button in row:
                button.grid(row=r, column=c, columnspan=1)
                c += 1
            r += 1

    def AddButton(self, value):

        return Button(
            self.calculator,
            text=value,
            width=9,
            command=lambda: self.clickButton(str(value)),
        )

    def clickButton(self, value):

        current_equation = str(self.equation.get())

        # To clear the calculation
        if value == "c":
            self.equation.delete(-1, END)

        elif value == "=":
            answer = str(eval(current_equation))
            self.equation.delete(-1, END)
            self.equation.insert(0, answer)

        else:
            self.equation.delete(0, END)
            self.equation.insert(-1, current_equation + value)


# Execution
if __name__ == "__main__":
    # main window of my desktop application
    window = Tk()

    # Tell our calculator class to use this window
    my_gui = Calculator(window)
    window.geometry('350x200')


    window.mainloop()
