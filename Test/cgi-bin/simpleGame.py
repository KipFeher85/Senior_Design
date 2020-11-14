#!\Users\kff50\Documents\Senior Year\Python\python.exe     # Path of python interpreter
from Test import game_w_coord as gwc
import sys
import json
import cgi

fs = cgi.FieldStorage()

sys.stdout.write("Content-Type: application/json")
sys.stdout.write("\n")
sys.stdout.write("\n")

if "gameid" in fs and "jump" in fs:
    g1 = gwc.game(str(fs["gameid"].value), True, True)
    jump = g1.getJumpBalls()
    sys.stdout.write(json.dumps(jump))

elif "password" in fs:  # If password is entered.
    password = gwc.getPassword()
    sys.stdout.write(json.dumps(password))

elif "insert" in fs and "gameid" in fs:  # If a game is being inserted
    gwc.insertGame(str(fs["gameid"].value))

elif "delete" in fs and "gameid" in fs:  # If a game is being deleted.
    gwc.deleteGame(str(fs["gameid"].value))

elif "gameid" in fs and "shot" in fs:  # If a specific game's shots page is clicked
    g1 = gwc.game(str(fs["gameid"].value), True, True)
    shotList = g1.get_list_of_shots()
    shots = g1.getShots(shotList)
    sys.stdout.write(json.dumps(shots))

elif "gameid" in fs and "pass" in fs:  # If a specific game's pass page is clicked
    g1 = gwc.game(str(fs["gameid"].value), True, True)
    shotList = g1.get_list_of_shots()
    shots = g1.getShots(shotList)
    shottimes = gwc.getShotTimeRanges(shots)
    passes = g1.getPasses(shottimes)
    sys.stdout.write(json.dumps(passes))

elif "gameid" in fs and "air" in fs:  # If a specific game's airball page is clicked
    g1 = gwc.game(str(fs["gameid"].value), True, True)
    shotList = g1.get_list_of_shots()
    shots = g1.getShots(shotList)
    list = []
    i = 0
    for shot in shots:
        if "airball" in shots[i].keys():
            if shots[i]["airball"] == True:
                list.append(shots[i])
        i += 1
    sys.stdout.write(json.dumps(list))

elif "game" in fs and "air" in fs:  # If a specific game's airball page is clicked
    g1 = gwc.game(str(fs["game"].value), True, True)
    shotList = g1.get_list_of_shots()
    shots = g1.getShots(shotList)
    list = []
    i = 0
    for shot in shots:
        if "airball" in shots[i].keys():
            if shots[i]["airball"] == True:
                list.append(shots[i])
        i += 1
    sys.stdout.write(json.dumps(list))

sys.stdout.write("\n")
sys.stdout.close()

