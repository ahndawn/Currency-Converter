# install tkinter, it facilities GUIs
#  pip install tk
import tkinter as tk
from tkinter import *
import tkinter.messagebox
from flask import Flask

app = Flask(__name__)

# GUI
root = tk.Tk()

root.title("Ahni's Currency Converter")

Tops = Frame(root, bg = 'red', pady=2, width = 1850, height=100, relief="ridge")
Tops.grid(row = 0, column = 0)

head = tk.Label(Tops, font=('black', 20, 'bold'), text="Ahni's Currency Converter", bg = 'white', fg='black')

head.grid(row=1, column = 0, sticky = W)

# create a string variable using StringVar() to root
variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)
 
variable1.set("currency")
variable2.set("currency")

def CurrencyConversion():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()

    from_currency = variable1.get()
    to_currency = variable2.get()

    if (Amount1_field.get() == ""):
        tkinter.messagebox.showinfo("Error!", "Amount Not Entered.\n Please enter a valid amount.")
 
    elif (from_currency == "currency" or to_currency == "currency"):
        tkinter.messagebox.showinfo("Error!",
                                    "Currency Not Selected.\n Please select FROM and TO Currency from the menu.")
 
    else:
        new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
        Amount2_field.insert(0, str(new_amount))
 
#clearing all the data entered by the user
def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)
 
 
Currency_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]
 
root.configure(background='darkseagreen1')
# loads size of window
root.geometry("550x375")
 
#  make sure the rows and columns number matches corresponding 'Amount' fields
Label_1 = Label(root, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="darkseagreen1", fg="black")
Label_1.grid(row=1, column=0, sticky=W)
 
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Amount :  ", bg="darkseagreen1", fg="black")
label1.grid(row=2, column=0, sticky=W)
 
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    From Currency :  ", bg="darkseagreen1", fg="black")
label1.grid(row=3, column=0, sticky=W)
 
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    To Currency :  ", bg="darkseagreen1", fg="black")
label1.grid(row=4, column=0, sticky=W)
 
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Converted Amount :  ", bg="darkseagreen1", fg="black")
label1.grid(row=8, column=0, sticky=W)
 
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="darkseagreen1", fg="black")
Label_1.grid(row=5, column=0, sticky=W)
 
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="darkseagreen1", fg="black")
Label_1.grid(row=7, column=0, sticky=W)
 
FromCurrency_option = tk.OptionMenu(root, variable1, *Currency_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *Currency_list)
 
FromCurrency_option.grid(row=3, column=2, ipadx=45, sticky=E)
ToCurrency_option.grid(row=4, column=2, ipadx=45, sticky=E)
 
Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=2, ipadx=28, sticky=E)
#  make sure row number matches corresponding 'labels' above
Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=2, ipadx=31, sticky=E)
 
Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Convert  ", padx=1.5, pady=2, bg="firebrick4", fg="white",
                 command=CurrencyConversion)
Label_9.grid(row=6, column=2)
 
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=1.5, bg="darkseagreen1", fg="black")
Label_1.grid(row=9, column=0, sticky=W)
 
Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Clear All  ", padx=1.5, pady=2, bg="firebrick4", fg="white",
                 command=clear_all)
Label_9.grid(row=10, column=0)
 
 
root.mainloop()

if __name__== '__main__':
    app.run('0.0.0.0', debug = True) #defUault port is 5000