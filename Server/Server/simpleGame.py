#!\Users\kff50\Documents\Senior Year\Python\python.exe     # Path of python interpreter

import game_w_coord as gwc

import cgi
import cgitb
cgitb.enable()

def print_header():
    print ("""Content-type: text/html\n
    <!DOCTYPE html>
    <html>
    <body>""")

def print_close():
    print ("""</body>
    </html>""")

def getShotList(gameId):
    g1 = gwc.game(gameId, True, True)
    shotList = g1.get_list_of_shots()
    shots = g1.getShots(shotList)
    print_header()
    print(shots)
    print_close()


def getPassList(gameId):
    g1 = gwc.game(gameId, True, True)
    shotList = g1.get_list_of_shots()
    shots = g1.getShots(shotList)
    shottimes = gwc.getShotTimeRanges(shots)
    passes = g1.getPasses(shottimes)
    print_header()
    print(passes)
    print_close()


def getJumpList(gameId):
    g1 = gwc.game(gameId, True, True)
    jump = g1.getJumpBalls()
    print_header()
    print(jump)
    print_close()


def getAirList(gameId):
    g1 = gwc.game(gameId, True, True)
    shotList = g1.get_list_of_shots()
    shots = g1.getShots(shotList)
    list = []
    i = 0
    for shot in shots:
        if "airball" in shots[i].keys():
            if shots[i]["airball"] == True:
                list.append(shotList[i])
        i += 1
    print_header()
    print(list)
    print_close()


def main():
    form = cgi.FieldStorage()
    if "gameid" in form and "shot" in form:         # If a specific game's shots page is clicked
        getShotList(form["gameid"].value)
    if "gameid" in form and "pass" in form:         # If a specific game's pass page is clicked
        getPassList(form["gameid"].value)
    if "gameid" in form and "jump" in form:         # If a specific game's jumpball page is clicked
        getJumpList(form["gameid"].value)
    if "gameid" in form and "air" in form:         # If a specific game's airball page is clicked
        getAirList(form["gameid"].value)

main()