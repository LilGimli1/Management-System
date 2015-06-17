from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Business Management System")
root.resizable(width=FALSE, height=FALSE)
	
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
	
ttk.Label(mainframe, text="What Type Of Product Was Sold?").grid(column=2, row=0, sticky=N)

Product = StringVar()
amount = StringVar()
date = StringVar()

Product_entry = ttk.Entry(mainframe, width=7, textvariable=Product)
Product_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="How Much Product Was Sold?").grid(column=2, row=3, sticky=N)

amount_entry = ttk.Entry(mainframe, width=7, textvariable=amount)
amount_entry.grid(column=2, row=4, sticky=(W, E))

ttk.Label(mainframe, text="What Date Was The Product Sold?").grid(column=2, row=5, sticky=N)	

date_entry = ttk.Entry(mainframe, width=7, textvariable=date)
date_entry.grid(column=2, row=6, sticky=(W, E))


ttk.Button(mainframe, text="export").grid(column=2, row=7, sticky=W)
ttk.Button(mainframe, text="import").grid(column=2, row=7, sticky=E)

root.mainloop()
