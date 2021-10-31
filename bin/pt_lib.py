import random
import mysql.connector
from mysql.connector import errorcode

#Read variables and values from ini file and return them as a dictionary
def read_ini ():
    reader = open('pt.ini', 'r')
    counter = 0
    d = {}
    try:
        for line in reader:
            k,v = line.split("=")
            v = v.strip("\n")
            v = v.strip("'")
            d[k] = v
    finally:
        return d
        reader.close()
    
def shuffle_cards (deck):
    rnl = random.shuffle(deck)
    return rnl

def get_meaning(card_img, card_orientation):
    ini = read_ini()
    deck = []
    try:
        #Open db connection
        cnx = mysql.connector.connect(user = ini['db_user'], password = ini['db_passwd'],
                                        host = ini['db_host'],
                                        database = ini['db_name'])
        cursor = cnx.cursor()
        card_meaning = "card_meaning_" + card_orientation
        query  = ("SELECT card_number, card_name, " + card_meaning + " from cards where card_image = '" + card_img + "'")
        cursor.execute(query)

                   
        for ( card_number, card_name, card_meaning ) in cursor:
            #print(card_number, card_name, card_meaning)
            deck.append([card_number, card_name, card_meaning])

        cursor.close()

    except mysql.connector.Error as err:

        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        #Close db connection
        cnx.close()
        #print(deck)
        return(deck)
