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
    with open("game_result.csv", "r+") as f:
        for line in f:
            if ',' in line:
                #print("original line: " + str(line))
                new_statement = line.replace(',', ' ')
                slist = new_statement.split()
                print("add to a list: " + str(slist))
                add_result = ("INSERT INTO match1 "
                              "(game_index, date, pid, team_name, bih, def, "
                              "balls_made, op_balls_made, innings, timeouts, winner) "
                              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                #match_data = ('game_index', 'date', 'pid', 'team_name', 'bih', 'def', 'balls_made', 'obm', 'innings', 'timeouts', 'winner')
                match_data = tuple(slist)
                cursor.execute(add_result, match_data)
    cnx.commit()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
cnx.close()