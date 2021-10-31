import pt_lib
import random
import time
from playsound import playsound
from tkinter import *
from tkinter import ttk

#Path to the pack in use:
pack = "../img/packs/rwps"

def get_orientation():
    #Upright or Reversed Indicator
    ur = random.randint(0,1)
    #
    if ur == 0:
        orientation = "upright" 
    else:
        orientation = "reversed" 
    return orientation
       
def shuffle_cards():
    deck = []
    card = {}
    name = ""
    for c in range(22):
        if c < 10:
            name = "ar0" + str(c) + ".gif"
        else:
            name = "ar" + str(c) + ".gif"
        card['name'] = name 
        card['orientation'] = get_orientation()
        deck.append(card)
        card = {}
        
    #Shuffle Three times
    print("Shuffle 1")
    playsound('../snd/shuffling-cards-1.wav')
    random.shuffle(deck)
    print(deck)
    time.sleep(1)
    print("Shuffle 2")
    playsound('../snd/shuffling-cards-1.wav')
    random.shuffle(deck)
    print(deck)
    time.sleep(1)
    print("Shuffle 3")
    playsound('../snd/shuffling-cards-1.wav')
    random.shuffle(deck)
    print(deck)
    time.sleep(1)

    return deck

card1_info = []
card2_info = []
card3_info = []
def flip_cards():
    shuffled_deck = shuffle_cards()
    flipped_card1 = PhotoImage(file=pack + '/' + shuffled_deck[0]['orientation'] + '/' + shuffled_deck[0]['name'])
    flipped_card2 = PhotoImage(file=pack + '/' + shuffled_deck[1]['orientation'] + '/' + shuffled_deck[1]['name'])
    flipped_card3 = PhotoImage(file=pack + '/' + shuffled_deck[2]['orientation'] + '/' + shuffled_deck[2]['name'])
    card_frame1.configure(image=flipped_card1)
    card_frame1.image = flipped_card1
    card_frame2.configure(image=flipped_card2)
    card_frame2.image = flipped_card2
    card_frame3.configure(image=flipped_card3)
    card_frame3.image = flipped_card3
    card1_info = pt_lib.get_meaning(shuffled_deck[0]['name'], shuffled_deck[0]['orientation'])
    card2_info = pt_lib.get_meaning(shuffled_deck[1]['name'], shuffled_deck[1]['orientation']) 
    card3_info = pt_lib.get_meaning(shuffled_deck[2]['name'], shuffled_deck[2]['orientation'])
    print(card1_info)
    print(card2_info)
    print(card3_info)

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
