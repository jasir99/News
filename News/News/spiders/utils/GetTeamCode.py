import unicodedata
from difflib import SequenceMatcher


def translateString(string):
    return unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore')

def checkType(string):
    if type(string) == unicode:
        return string
    return unicode(string, "utf-8")

def isMatching(a, b):
    a = translateString(checkType(a)).replace(" ", "").lower()
    b = translateString(checkType(b)).replace(" ", "").lower()

    return SequenceMatcher(None, a, b).ratio()

def getTeamCode(team_codes, league, team):
    code = "NA"
    max = 0.6

    for attr, value in team_codes.__dict__.iteritems():
        if league.lower() in attr.lower():
            for key, item in value.iteritems():
                if "team" not in item and "TeamName" not in item:
                    if isMatching(key, team) >= max:
                        code = item["team_code"]
                        max = isMatching(key, team)
                    if team.lower() == item["team_code"].lower():
                        return item["team_code"]

                if "TeamName" in item:
                    if isMatching(item["TeamName"], team) >= max:
                        code = item["TeamCode"]
                        max = isMatching(item["TeamName"], team)
                    if isMatching(key, team) >= max:
                        code = item["TeamCode"]
                        max = isMatching(key, team)

                elif "team" in item:
                    if isMatching(item["team"], team) >= max:
                        code = item["team_code"]
                        max = isMatching(item["team"], team)
                    if isMatching(key, team) >= max:
                        code = item["team_code"]
                        max = isMatching(key, team)

            return code
    return code
