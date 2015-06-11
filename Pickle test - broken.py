# Save a dictionary into a pickle file.
import pickle

from tkinter import *
from tkinter import ttk

def exp():

	favorite_color = {sales}

	pickle.dump( favorite_color, open( "save.p", "wb" ) )

def imp():
	
	favorite_color = pickle.load( open( "save.p", "rb" ) )
	favorite_color is now { "lion": "yellow", "kitty": "red" }


root = Tk()
root.title("Business Management System")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#sales = StringVar()
#GST = StringVar()

#sales_entry = ttk.Entry(mainframe, width=7, textvariable=sales)
#sales_entry.grid(column=2, row=1, sticky=(W, E))

#ttk.Button(mainframe, text="export", command=exp).grid(column=2, row=3, sticky=W)
#ttk.Button(mainframe, text="import", command=imp).grid(column=3, row=3, sticky=W)


