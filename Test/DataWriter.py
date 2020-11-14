import json
import os
from Test import game_w_coord as gwc

data = {}

path = "GameFiles/"
dirs = os.listdir(path)


def team_details(dirs):
    data = []
    for i in range(0, len(dirs)):
        ext = dirs[i]
        id = ext[:10]
        g1 = gwc.game(id, True, True)
        gameDate = g1.gamedate.date()
        data.append(
            {'game id': g1.gameid[:10], 'game date': gameDate, 'home team': g1.home.teamname, 'away team': g1.visitor.teamname})
        with open('team-Info.json', 'w') as outfile:
            json.dump(data, outfile, default=str)

        print("next game up: " + str(i))


def get_shots(game):
    g1 = gwc.game(game, True, True)
    data["shots"] = []
    data["shots"].append({'game id' : g1.gameid})
    list = g1.get_list_of_shots()
    for i in range(0, len(g1.get_list_of_shots()) - 1):
        data["shots"].append({'Player:': list[i]["player"], 'team': list[i]["team"], 'quarter': list[i]["quarter"], 'time start': list[i]["begin"], 'time end': list[i]["end"], 'outcome': list[i]["outcome"]})
    with open('shots.json', 'w') as outfile:
        json.dump(data, outfile, default=str)


def get_passes(game):
    g1 = gwc.game(game, True, True)
    data = []
    list = g1.getPasses()
    for i in range(0, len(list) - 1):
        data.append({'passername': list[i]["passername"], 'passerid': list[i]["passerid"], 'receivername': list[i]["receivername"], 'team': list[i]["team"], 'quarter': list[i]["quarter"], 'time': list[i]["time"], 'coordinates': list[i]["coordinates"]})
    with open('pass488.json', 'w') as outfile:
        json.dump(data, outfile, default=str)
def main():
    #get_passes("0021500488")
    print(dirs)
    team_details(dirs)


if __name__ == "__main__":
        main()








