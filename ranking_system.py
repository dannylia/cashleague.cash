
players = ['billy', 'sally', 'johnny', 'kevin', 'sam', 'mustafa',
           'stephanie', 'jerry', 'linda', 'joey', 'player11', 'player12', 'player13',
           'player14', 'player15', 'player16', 'player17', 'player18', 'player19',
           'player20', 'player21', 'player22', 'player23', 'player24', 'player25',
           'player26', 'player27', 'player28', 'player29', 'player30', 'player31',
           'player32', 'player33', 'player34', 'player35', 'player36', 'player37',
           'player38', 'player39', 'player40', 'player41', 'player42', 'player43',
           'player44', 'player45', 'player46', 'player47', 'player48', 'player49',
           'player50']
player_dict = {}
beginning_rank = 4.5
for i in players:
    player_name = i
    player_dict[player_name] = ""
for k, v in player_dict.items():
    player_dict[k] = beginning_rank
print(player_dict)
x = 4.01
y = 4.990
tot = int(0)
keys = []
values = []
curve = 1
increment = int(.01)
z = {}
#while x < y:
#    #print(x)
#    print(curve)
#    x += .01
#    keys += [x]
#    values += [curve]
#    tot += 1
#    curve += increment
#    increment -= .00003
#    #print(increment)
#print(tot)
game1 = {}
game1["innings"] = 0
game1["p1_name"] = ""
game1["p1_def_shots"] = ""
game1["p1_bih"] = ""
game1["P1_winner"] = ""
game1["p1_tot_pocketed"] = 0
game1["p2_name"] = ""
game1["p2_def_shots"] = ""
game1["p2_bih"] = ""
game1["p2_winner"] = ""
game1["p2_tot_pocketed"] = 0
rank7 = 7.5
rank6 = 6.5
list = []


two = [1.4, 1.3, 1.25, 1.2, 1.15, 1.1, 1.06, 1.03, 1, 0.995, 0.99, 0.985, 0.98]
three = [1.27, 1.2, 1.15, 1.1, 1.06, 1.03, 1, 0.995, 0.99, 0.985, 0.98, 0.97, 0.95]
four = [1.2, 1.15, 1.1, 1.06, 1.03, 1, 0.97, 0.96, 0.959, 0.951, 0.945, 0.938, 0.93]
five = [1.15, 1.1, 1.06, 1.03, 1, 0.995, 0.94, 0.93, .925, .92, .915, 0.91]
six = [1.1, 1.06, 1.03, 1, .995, .99, .95, .94, .92, .91, .9, .89, .88]
seven = [1.05, 1, .99, .97, .96, .95, .935, .92, .91, .9, .89, .875, .6667]

num_innings = 0
wins = 0
game_line = []
string = ""
new_alist = []
x = ','
team_wins = {}
team_wins["blue"] = 0
team_wins["red"] = 0
team_wins["green"] = 0
team_wins["yellow"] = 0
team_wins["azure"] = 0
team_wins["black"] = 0
team_wins["pink"] = 0
team_wins["gray"] = 0
team_wins["purple"] = 0
team_wins["orange"] = 0


# retrieve current rank from dictionary
def get_rank(pname):

    for k, v in player_dict.items():
        if k == pname:
            current_rank = v
            return current_rank


# calculate new rank
def update_rank(current_ranking, lookup):

    conv = int(current_ranking)
    current_r = float(current_ranking)
    if conv <= 2:
        int_lookup = two[lookup]
    elif conv == 3:
        int_lookup = three[lookup]
    elif conv == 4:
        int_lookup = four[lookup]
    elif conv == 5:
        int_lookup = five[lookup]
    elif conv == 6:
        int_lookup = six[lookup]
    elif conv == 7:
        int_lookup = seven[lookup]

    #print("current rank is " + str(current_r))
    #print("multiplier is " + str(int_lookup))
    new_rank = int_lookup * current_r
    #print("new rank is " + str(new_rank))
    return new_rank

def get_game_id(slist):
    date = str(slist[0])
    loc_id = str(slist[1])
    team_id = str(slist[2])
    player_id = str(slist[3])
    match_number = str(slist[4])
    game_number = str(slist[5])
    lag_winner = str(slist[6])
    game_id = date + loc_id + team_id + player_id + match_number + game_number + lag_winner

    return game_id
with open("game_result3.csv", "r+") as f:
    for line in f:
        if ',' in line:
            #print("original line: " + str(line))
            #print("detected")
            new_statement = line.replace(',', ' ')
            #print("add spaces: " + str(new_statement))
            slist = new_statement.split()
            game_id = get_game_id(slist)
            print("game id is " + game_id)
            #print(line)
            #print("add to a list: " + str(slist))
            for i, l in enumerate(slist):
                if 'TRUE' in l:
                    pname = slist[i-10]
                    print(str(pname) + " won the game in " + str(slist[i-4]) + " innings.")

                    for k, v in team_wins.items():
                        if k == slist[i-7]:
                            team_wins[k] = 1

                    lookup = int(slist[i-2]) - 1
                    #print("lookup value is " + str(lookup))
                    current_ranking = 6.2
                    #current_ranking = get_rank(pname)
                    new_rank = update_rank(current_ranking, lookup)
                    print(str(pname) + "'s rank has been updated from " + str(current_ranking) + " to " + str(new_rank))
                elif 'FALSE' in l:
                    print(str(slist[i-10]) + " lost the game and made " + str(slist[i-5]) + " of the opponent's balls.")
print(team_wins)


        #list += [line]
        #if ',' in words:
        #    new_statement = words.replace(',', ', ')
        #    #print(new_statement)
#
        ##print(words)
        #for n, i in enumerate(words):
        #    #slist[n] = new_word
        #    #for x in i:
        #        #new_word = i.strip(".")
        #        #slist[n] = new_word
        #    if 'TRUE' in i:
        #        wins += 1
        #        #print("team " + str(line.split()[0]) + " won this game.")
#print(wins)
#print(list)
#print(new_alist)
#for i in list:
    #print(i)

#for i, d in enumerate(list):  # traverse the list
#    #print(list[i])
#    if 'TRUE' in d:
#        game_line += [d]
#        print(game_line)
#        for word in game_line:
#            string + word
#            print(string)
#        #print(i)
#        wins += 1
#    #print(d)
#    temp = {}
#    for key, val in game1.items():  # go through the `dict`
#
#        if key == 'p1_name':
#            game1[key] = [d]
#        else:
#            pass
#
##print(game1.items())
#print(wins)
#for i, num in enumerate(seven):
#
#    new_rank = rank7 * seven[i]
#    #print("if a " + str(rank7) + " wins in " + str(i) + " innings, the new rank is " + str(new_rank))
#
#for i, num in enumerate(six):
#    new_rank = rank6 * six[i]
#    #print("if a " + str(rank6) + " wins in " + str(i) + " innings, the new rank is " + str(new_rank))
#