from random import *
from tkinter import *
from tkinter import ttk

#Path to the pack in use:
pack = "../img/packs/rwps"

def shuffle_cards():
    deck = []
    #Upright or Reversed Indicator
    ur = randint(0,1)
    #
    if ur == 0:
        upright_or_reversed = "upright" 
    else:
        upright_or_reversed = "reversed" 

    for card in range(0,21):
        pass

def flip_cards():
    flipped_card1 = PhotoImage(file=pack + '/upright/ar00.gif')
    flipped_card2 = PhotoImage(file=pack + '/upright/ar01.gif')
    flipped_card3 = PhotoImage(file=pack + '/upright/ar02.gif')
    card_frame1.configure(image=flipped_card1)
    card_frame1.image = flipped_card1
    card_frame2.configure(image=flipped_card2)
    card_frame2.image = flipped_card2
    card_frame3.configure(image=flipped_card3)
    card_frame3.image = flipped_card3

root = Tk()

root.title("3 Card Spread")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

card1 = PhotoImage(file='../img/packs/rwps/upright/verso.gif')
card2 = PhotoImage(file='../img/packs/rwps/upright/verso.gif')
card3 = PhotoImage(file='../img/packs/rwps/upright/verso.gif')

#Row One Static Labels
ttk.Label(mainframe, text="1").grid(column=1, row=1, sticky=(W, E))
ttk.Label(mainframe, text="2").grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, text="3").grid(column=3, row=1, sticky=(W, E))
#Card Labels, will change during flip.
card_frame1 = ttk.Label(mainframe, image=card1)
card_frame1.grid(column=1, row=2, sticky=(W, E))
card_frame2 = ttk.Label(mainframe, image=card2)
card_frame2.grid(column=2, row=2, sticky=(W, E))
card_frame3 = ttk.Label(mainframe, image=card3)
card_frame3.grid(column=3, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Flip Cards", command=flip_cards).grid(column=2, row=3, sticky=(W, E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
