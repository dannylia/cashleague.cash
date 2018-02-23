import mysql.connector
import datetime
player_info = []
#print(type(player_info))
players = {}
try:
    cnx = mysql.connector.connect(user='admin', password='TrustM300',
                              host='127.0.0.1',
                              database='pool')
    cursor = cnx.cursor()
    with open("player_info2.csv", "r+") as f:
        for line in f:
            if ',' in line:
                print("original line: " + str(line))
                new_statement = line.replace(',', ' ')
                slist = new_statement.split()
                print("add to a list: " + str(slist))
                add_player = ("INSERT INTO players "
                              "(player_num, f_name, l_name, email, phone) "
                              "VALUES (%s, %s, %s, %s, %s)")
                new_player_info = tuple(slist)
                cursor.execute(add_player, new_player_info)
    cnx.commit()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
cnx.close()