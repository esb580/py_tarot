import mysql.connector
from mysql.connector import errorcode
import pt_lib

#Open Ini-file and read in vars
ini = pt_lib.read_ini()

deck = []
try:
    #Open db connection
    cnx = mysql .connector.connect(user = ini['db_user'], password = ini['db_passwd'],
                                    host = ini['db_host'],
                                    database = ini['db_name'])
    cursor = cnx.cursor()
    query  = ("SELECT card_number, card_name from cards")
    cursor.execute(query)

    for ( card_number, card_name) in cursor:
        #print(card_number + ". " + card_name)
        deck.append(card_name)

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

################################################################
#Create a 3 card spread from your deck
pt_lib.shuffle_cards(deck)
print("")
print("3 Card: Past, Present, Future")
print("=============================")
print("")
print("[", deck[0], "][", deck[1], "][", deck[2], "]")
print("")


