from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as tkst

root = Tk()
root.title("Business Management System")
root.resizable(width=FALSE, height=FALSE)

#SalesGUI function

def SalesGUI():

	mainframe = ttk.Frame(root, padding="5 5 5 5")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	mainframe.columnconfigure(0, weight=1)
	mainframe.rowconfigure(0, weight=1)

	ttk.Label(mainframe, text="Sales", padding="5 5 5 5").grid(column=2, row=0, sticky=N)

	ttk.Button(mainframe, text="Add", width = 23, padding="5 5 5 5").grid(column=0, row=1, sticky=S)
	ttk.Button(mainframe, text="Remove", width = 23, padding="5 5 5 5").grid(column=1, row=1, sticky=S)
	ttk.Button(mainframe, text="Edit", width = 23, padding="5 5 5 5").grid(column=2, row=1, sticky=S)
	ttk.Button(mainframe, text="Import", width = 23, padding="5 5 5 5").grid(column=3, row=1, sticky=S)
	ttk.Button(mainframe, text="Exit", width = 23, padding="5 5 5 5", command=MainGui).grid(column=4, row=1, sticky=S)
	ttk.Button(mainframe, text="Exit", width = 23, padding="5 5 5 5", command=MainGui).grid(column=4, row=1, sticky=S)

	text_widget = tkst.ScrolledText(root, height=8, width=50).grid(column=0, row=2, sticky=(N, E, S, W))
	text_widget.insert('insert',"text  message will display here")




#PurchasesGUI Function

def PurchasesGUI():
	mainframe = ttk.Frame(root, padding="5 5 5 5")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	mainframe.columnconfigure(0, weight=1)
	mainframe.rowconfigure(0, weight=1)

	ttk.Label(mainframe, text="Sales", padding="5 5 5 5").grid(column=2, row=0, sticky=N)

	ttk.Button(mainframe, text="Add", width = 23, padding="5 5 5 5").grid(column=0, row=1, sticky=S)
	ttk.Button(mainframe, text="Remove", width = 23, padding="5 5 5 5").grid(column=1, row=1, sticky=S)
	ttk.Button(mainframe, text="Edit", width = 23, padding="5 5 5 5").grid(column=2, row=1, sticky=S)
	ttk.Button(mainframe, text="Import", width = 23, padding="5 5 5 5").grid(column=3, row=1, sticky=S)
	ttk.Button(mainframe, text="Exit", width = 23, padding="5 5 5 5", command=MainGui).grid(column=4, row=1, sticky=S)
	ttk.Button(mainframe, text="Exit", width = 23, padding="5 5 5 5", command=MainGui).grid(column=4, row=1, sticky=S)

	text_widget = tkst.ScrolledText(root, height=8, width=50).grid(column=0, row=2, sticky=(N, E, S, W))
	text_widget.insert('insert',"text  message will display here")

#Customer Details GUI Function

def CustDetailsGUI():
	mainframe = ttk.Frame(root, padding="5 5 5 5")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	mainframe.columnconfigure(0, weight=1)
	mainframe.rowconfigure(0, weight=1)

	ttk.Label(mainframe, text="Sales", padding="5 5 5 5").grid(column=2, row=0, sticky=N)

	ttk.Button(mainframe, text="Add", width = 23, padding="5 5 5 5").grid(column=0, row=1, sticky=S)
	ttk.Button(mainframe, text="Remove", width = 23, padding="5 5 5 5").grid(column=1, row=1, sticky=S)
	ttk.Button(mainframe, text="Edit", width = 23, padding="5 5 5 5").grid(column=2, row=1, sticky=S)
	ttk.Button(mainframe, text="Import", width = 23, padding="5 5 5 5").grid(column=3, row=1, sticky=S)
	ttk.Button(mainframe, text="Exit", width = 23, padding="5 5 5 5", command=MainGui).grid(column=4, row=1, sticky=S)
	ttk.Button(mainframe, text="Exit", width = 23, padding="5 5 5 5", command=MainGui).grid(column=4, row=1, sticky=S)

	text_widget = tkst.ScrolledText(root, height=8, width=50).grid(column=0, row=2, sticky=(N, E, S, W))
	text_widget.insert('insert',"text  message will display here")

#GSTGUI Function

def GSTGUI():

	def calculate(*args):
		try:
			value = float(sales.get())
			GST.set((0.1 * value * 10000.0)/10000.0)
		except ValueError:
			pass
		
	root = Toplevel()
	root.title("sales to GST")

	mainframe = ttk.Frame(root, padding="3 3 12 12")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	mainframe.columnconfigure(0, weight=1)
	mainframe.rowconfigure(0, weight=1)

	sales = StringVar()
	GST = StringVar()

	sales_entry = ttk.Entry(mainframe, width=7, textvariable=sales)
	sales_entry.grid(column=2, row=1, sticky=(W, E))

	ttk.Label(mainframe, textvariable=GST).grid(column=2, row=2, sticky=(W, E))
	ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

	ttk.Label(mainframe, text="sales").grid(column=3, row=1, sticky=W)
	ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
	ttk.Label(mainframe, text="GST").grid(column=3, row=2, sticky=W)

	for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

	sales_entry.focus()
	root.bind('<Return>', calculate)

	root.mainloop()



#StoreInvGUI Function

def StoreInvGUI():

	mainframe = ttk.Frame(root, padding="5 5 5 5")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	mainframe.columnconfigure(0, weight=1)
	mainframe.rowconfigure(0, weight=1)

	ttk.Label(mainframe, text="Sales", padding="5 5 5 5").grid(column=2, row=0, sticky=N)

	ttk.Button(mainframe, text="Add", width = 23, padding="5 5 5 5").grid(column=0, row=1, sticky=S)
	ttk.Button(mainframe, text="Remove", width = 23, padding="5 5 5 5").grid(column=1, row=1, sticky=S)
	ttk.Button(mainframe, text="Edit", width = 23, padding="5 5 5 5").grid(column=2, row=1, sticky=S)
	ttk.Button(mainframe, text="Import", width = 23, padding="5 5 5 5").grid(column=3, row=1, sticky=S)
	ttk.Button(mainframe, text="Exit", width = 23, padding="5 5 5 5", command=MainGui).grid(column=4, row=1, sticky=S)
	ttk.Button(mainframe, text="Exit", width = 23, padding="5 5 5 5", command=MainGui).grid(column=4, row=1, sticky=S)

	text_widget = tkst.ScrolledText(root, height=8, width=50).grid(column=0, row=2, sticky=(N, E, S, W))
	text_widget.insert('insert',"text  message will display here")

#WarehouseInvGUI Function

def WarehouseInvGUI():
	mainframe = ttk.Frame(root, padding="5 5 5 5")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	mainframe.columnconfigure(0, weight=1)
	mainframe.rowconfigure(0, weight=1)

	ttk.Label(mainframe, text="Sales", padding="5 5 5 5").grid(column=2, row=0, sticky=N)

	ttk.Button(mainframe, text="Add", width = 23, padding="5 5 5 5").grid(column=0, row=1, sticky=S)
	ttk.Button(mainframe, text="Remove", width = 23, padding="5 5 5 5").grid(column=1, row=1, sticky=S)
	ttk.Button(mainframe, text="Edit", width = 23, padding="5 5 5 5").grid(column=2, row=1, sticky=S)
	ttk.Button(mainframe, text="Import", width = 23, padding="5 5 5 5").grid(column=3, row=1, sticky=S)
	ttk.Button(mainframe, text="Exit", width = 23, padding="5 5 5 5", command=MainGui).grid(column=4, row=1, sticky=S)
	ttk.Button(mainframe, text="Exit", width = 23, padding="5 5 5 5", command=MainGui).grid(column=4, row=1, sticky=S)

	text_widget = tkst.ScrolledText(root, height=8, width=50).grid(column=0, row=2, sticky=(N, E, S, W))
	text_widget.insert('insert',"text  message will display here")

#MainMenu Code
def MainGui() :
	root.geometry('{}x{}'.format(800, 400))
	
	mainframe = ttk.Frame(root, padding="5 5 5 5")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	mainframe.columnconfigure(0, weight=3, minsize = 40)
	mainframe.rowconfigure(0, weight=1, minsize = 40)
	
	ttk.Label(mainframe, text="Management System").grid(column=2, row=0, sticky=N)
	
	ttk.Button(mainframe, text="Sales", width = 35, padding="5 5 5 5", command=SalesGUI).grid(column=1, row=3, sticky=W)
	ttk.Button(mainframe, text="Purchases", width = 35, padding="5 5 5 5", command=PurchasesGUI).grid(column=1, row=5, sticky=W)
	ttk.Button(mainframe, text="Warehouse Inventory", width = 35, padding="5 5 5 5", command=WarehouseInvGUI).grid(column=1, row=7, sticky=W)
	
	ttk.Button(mainframe, text="Customer Details", width = 35, padding="5 5 5 5", command=CustDetailsGUI).grid(column=2, row=3, sticky=N)
	ttk.Button(mainframe, text="GST Calculation", width = 35, padding="5 5 5 5", command=GSTGUI).grid(column=2, row=5, sticky=N)
	
	ttk.Button(mainframe, text="Store 1 Inventory", width = 35, padding="5 5 5 5", command=StoreInvGUI).grid(column=3, row=3, sticky=E)
	ttk.Button(mainframe, text="Store 2 Inventory", width = 35, padding="5 5 5 5", command=StoreInvGUI).grid(column=3, row=5, sticky=E)
	ttk.Button(mainframe, text="Store 3 Inventory", width = 35, padding="5 5 5 5", command=StoreInvGUI).grid(column=3, row=7, sticky=E)

	#
	#
	#
	#
	#
	#
MainGui()	
root.mainloop()
