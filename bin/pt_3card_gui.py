from tkinter import *
from tkinter import ttk


def deal_cards(*args):
    pass

root = Tk()
root.title("3 Card Spread")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

card1 = PhotoImage(file='../img/gif/verso.gif')
card2 = PhotoImage(file='../img/gif/verso.gif')
card3 = PhotoImage(file='../img/gif/verso.gif')

ttk.Label(mainframe, text="1").grid(column=1, row=1, sticky=(W, E))
ttk.Label(mainframe, text="2").grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, text="3").grid(column=3, row=1, sticky=(W, E))

card_frame1 = ttk.Label(mainframe, image=card1).grid(column=1, row=2, sticky=(W, E))
card_frame2 = ttk.Label(mainframe, image=card2).grid(column=2, row=2, sticky=(W, E))
card_frame3 = ttk.Label(mainframe, image=card3).grid(column=3, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Deal", command=deal_cards).grid(column=2, row=3, sticky=(W, E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
