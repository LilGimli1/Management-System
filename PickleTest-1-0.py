from tkinter import *
from tkinter import ttk
import pickle
from sales import Sales


def Export():
#Exporting to sales.obj
	filehandler = open("Sales.pickle","wb")
	pickle.dump(sale,filehandler)
	filehandler.close()
	root.destroy()
	
	
def Calc():
	#Confirmation Window
	root = Toplevel()
	root.title("sales to GST")
	
	mainframe = ttk.Frame(root, padding="3 3 12 12")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	mainframe.columnconfigure(0, weight=1)
	mainframe.rowconfigure(0, weight=1)
	
	
	ttk.Label(mainframe, text=x.get()).grid(column=1, row=1, sticky=N)
	ttk.Label(mainframe, text=y.get()).grid(column=2, row=1, sticky=N)
	ttk.Label(mainframe, text=z.get()).grid(column=3, row=1, sticky=N)
	ttk.Label(mainframe, text="Is This The Correct Information").grid(column=2, row=2, sticky=N)
	ttk.Button(mainframe, text="No", command=root.destroy).grid(column=1, row=3, sticky=W)
	ttk.Button(mainframe, text="Yes", command=Export).grid(column=3, row=3, sticky=W)
	for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
	root.bind('<Return>')

	root.mainloop()


root = Tk()
root.title("Business Management System")
root.resizable(width=FALSE, height=FALSE)

#Gui Mainframe
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#temporary variables for input data
x = StringVar()
y = StringVar()
z = StringVar()	

#First Sector, Type of Product
ttk.Label(mainframe, text="What Type Of Product Was Sold?").grid(column=2, row=0, sticky=N)

Product_entry = ttk.Entry(mainframe, width=7, textvariable=x)
Product_entry.grid(column=2, row=1, sticky=(W, E))

#Second Sector, Amount of Product
ttk.Label(mainframe, text="How Much Product Was Sold?").grid(column=2, row=3, sticky=N)


amount_entry = ttk.Entry(mainframe, width=7, textvariable=y)
amount_entry.grid(column=2, row=4, sticky=(W, E))


#Third Sector, Date Of Sale

ttk.Label(mainframe, text="What Date Was The Product Sold?").grid(column=2, row=5, sticky=N)	

date_entry = ttk.Entry(mainframe, width=7, textvariable=z)
date_entry.grid(column=2, row=6, sticky=(W, E))

sale = Sales()
sale.Type = x
sale.Amount = y
sale.Date = z

ttk.Button(mainframe, text="Save", width = 35, padding="5 5 5 5", command=Calc).grid(column=2, row=7, sticky=N)

	
root.mainloop()
