from tkinter import * #imprt whole module

class CurrencyConverter: #create a class
    def __init__(self): #special method in python, by using"self" the function calls it's instance
        window = Tk() #method to create a window (provided by using tkinter)
        window.title("Currency Converter") #title name for window
        window.configure(bg = "white") #background color of the window

        #adding label widgets
        Label(window,font = "Cagliari 12 bold", bg = "white",
        text="Amount to convert").grid(row = 1, column = 1, sticky = W)
        Label(window,font = "Cagliari 12 bold", bg = "white",
        text = "Convertion rate").grid(row = 2, column = 1, sticky = W)
        Label(window,font = "Cagliari 12 bold", bg = "white",
        text = "Converted amount").grid(row = 3, column = 1, sticky = W)

        #creating objects and adding entry functions (entry functions are used when expected an input)
        self.amounttoConvertVar = StringVar()
        Entry(window, textvariable = self.amounttoConvertVar,
        justify = RIGHT).grid(row = 1, column = 2)
        self.convertionRateVar = StringVar()
        Entry(window, textvariable = self.convertionRateVar,
        justify = RIGHT).grid(row = 2, column = 2)
        self.convertedAmountVar = StringVar()
        lblConvertedAmount = Label(window, font = "Cagliari 12 bold", bg ="white",
        textvariable = self.convertedAmountVar).grid(row=3, column = 2, sticky = E)

        #creating covert and clear buttons
        btConvertedAmount = Button(window, text = "convert", font = "Cagliari 12 bold", bg = "green",
        command = self.ConvertedAmount).grid(row = 4, column = 2, sticky = E)
        btdelete_all = Button(window, text = "clear", font = "Cagliari 12 bold", bg = "red",
        command = self.delete_all).grid(row = 4, column = 6, padx = 25, pady = 25, sticky = E)

        window.mainloop()

    def ConvertedAmount(self):
        amt = float(self.convertionRateVar.get())
        convertedAmountVar = float(self.amounttoConvertVar.get()) * amt
        self.convertedAmountVar.set(format(convertedAmountVar, '10.2f'))

    def delete_all(self):
        self.amounttoConvertVar.set("")
        self.convertionRateVar.set("")
        self.convertedAmountVar.set("")

CurrencyConverter()
