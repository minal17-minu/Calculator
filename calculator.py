import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("300x400")
        self.window.configure(bg='black')

        # Create display
        self.display_var = tk.StringVar()
        self.display = tk.Entry(
            self.window,
            textvariable=self.display_var,
            font=('Arial', 24),
            justify='right',
            bg='white',
            fg='black'
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        # Calculator buttons
        self.buttons = [
            ['MC', 'MR', 'MS', 'M+'],
            ['(', ')', 'C', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '±', '=']
        ]

        # Create and place buttons
        for i, row in enumerate(self.buttons):
            for j, text in enumerate(row):
                button = tk.Button(
                    self.window,
                    text=text,
                    font=('Arial', 12),
                    width=5,
                    height=2,
                    bg='#333333',
                    fg='#00FF00',
                    command=lambda t=text: self.button_click(t)
                )
                button.grid(row=i+1, column=j, padx=2, pady=2, sticky='nsew')

        # Configure grid weights
        for i in range(7):
            self.window.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.window.grid_columnconfigure(i, weight=1)

    def button_click(self, value):
        current = self.display_var.get()
        
        if value == 'C':
            self.display_var.set('')
        elif value == '=':
            try:
                result = eval(current)
                self.display_var.set(result)
            except:
                self.display_var.set('Error')
        elif value in ['MC', 'MR', 'MS', 'M+', '±']:
            pass  # Memory functions not implemented
        else:
            self.display_var.set(current + value)

    def run(self):
        self.window.mainloop()

# Create and run the calculator
if __name__ == "__main__":
    calc = Calculator()
    calc.run()