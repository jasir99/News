# -*- coding: utf-8 -*-
from mongoalchemy.document import Document, Index
from mongoalchemy.fields import *
from dateparser import parse

SOCCER_LEAGUES = ['EPL', 'LALIGA', 'UEFA', 'Bund', 'SerieA',
                  'LIGUE', 'ERED', 'MLS', 'PRIME', 'Argent',
                  'Brazil', 'Mexico', 'EFL', 'FACUP', 'Turkey',
                  'EuroL', 'SERIEA', 'BUND']


class News(Document):
    title = StringField()
    description = StringField()
    link = StringField()
    image = StringField()
    sport = StringField(default="")
    team = StringField()
    league = StringField()
    source = StringField()
    published_at = StringField()
    crawled_time = DateTimeField()
    team_code = StringField()
    hash = StringField()
    isExternal = BoolField(default=False)

    i_hash = Index().ascending('hash').unique()

    def serialize(self):
        sport = ''
        if self.league in SOCCER_LEAGUES:
            sport = 'SOCCER'

        self.fixDate()

        return {
            'title': self.title,
            'description': self.description,
            'link': self.link,
            'image': self.image,
            'sport': sport,
            'team': self.team,
            'league': self.league,
            'source': self.source,
            'published_at': self.published_at,
            'crawled_time': str(self.crawled_time),
            'team_code': self.team_code,
            'hash': self.hash,
            'isExternal': self.isExternal
        }

    def fixDate(self):
        try:
            pd = parse(self.published_at)
            pd = pd.replace(minute=self.crawled_time.minute, hour=self.crawled_time.hour,
                            second=self.crawled_time.second, microsecond=self.crawled_time.microsecond)
            self.published_at = pd.strftime("%Y-%m-%d %H:%M:%S")
        except:
            pass


class CrawlerStats(Document):
    time = DateTimeField()
    resource = StringField()
    hash = StringField()
    count = IntField()
    operation_time = FloatField()

    
class TeamCodes:
    MLB = {
        "ari": {
            "TeamName": "Arizona Diamondbacks",
            "TeamCode": "25507be1-6a68-4267-bd82-e097d94b359b"
        },
        "atl": {
            "TeamName": "Atlanta Braves",
            "TeamCode": "12079497-e414-450a-8bf2-29f91de646bf"
        },
        "bal": {
            "TeamName": "Baltimore Orioles",
            "TeamCode": "75729d34-bca7-4a0f-b3df-6f26c6ad3719"
        },
        "bos": {
            "TeamName": "Boston Red Sox",
            "TeamCode": "93941372-eb4c-4c40-aced-fe3267174393"
        },
        "chc": {
            "TeamName": "Chicago Cubs",
            "TeamCode": "55714da8-fcaf-4574-8443-59bfb511a524"
        },
        "chw": {
            "TeamName": "Chicago White Sox",
            "TeamCode": "47f490cd-2f58-4ef7-9dfd-2ad6ba6c1ae8"
        },
        "cin": {
            "TeamName": "Cincinnati Reds",
            "TeamCode": "c874a065-c115-4e7d-b0f0-235584fb0e6f"
        },
        "cle": {
            "TeamName": "Cleveland Indians",
            "TeamCode": "80715d0d-0d2a-450f-a970-1b9a3b18c7e7"
        },
        "col": {
            "TeamName": "Colorado Rockies",
            "TeamCode": "29dd9a87-5bcc-4774-80c3-7f50d985068b"
        },
        "det": {
            "TeamName": "Detroit Tigers",
            "TeamCode": "575c19b7-4052-41c2-9f0a-1c5813d02f99"
        },
        "hou": {
            "TeamName": "Houston Astros",
            "TeamCode": "eb21dadd-8f10-4095-8bf3-dfb3b779f107"
        },
        "kan": {
            "TeamName": "Kansas City Royals",
            "TeamCode": "833a51a9-0d84-410f-bd77-da08c3e5e26e"
        },
        "laa": {
            "TeamName": "Los Angeles Angels",
            "TeamCode": "4f735188-37c8-473d-ae32-1f7e34ccf892"
        },
        "laa2": {
            "TeamName": "Los Angeles Angels (A)",
            "TeamCode": "4f735188-37c8-473d-ae32-1f7e34ccf892"
        },
        "laa3": {
            "TeamName": "Los Angeles Angels (AAA)",
            "TeamCode": "4f735188-37c8-473d-ae32-1f7e34ccf892"
        },
        "lad": {
            "TeamName": "Los Angeles Dodgers",
            "TeamCode": "ef64da7f-cfaf-4300-87b0-9313386b977c"
        },
        "mia": {
            "TeamName": "Miami Marlins",
            "TeamCode": "03556285-bdbb-4576-a06d-42f71f46ddc5"
        },
        "mia2": {
            "TeamName": "Miami Marlins  (A)",
            "TeamCode": "03556285-bdbb-4576-a06d-42f71f46ddc5"
        },
        "mia3": {
            "TeamName": "Miami Marlins  (AAA)",
            "TeamCode": "03556285-bdbb-4576-a06d-42f71f46ddc5"
        },
        "mil": {
            "TeamName": "Milwaukee Brewers",
            "TeamCode": "dcfd5266-00ce-442c-bc09-264cd20cf455"
        },
        "min": {
            "TeamName": "Minnesota Twins",
            "TeamCode": "aa34e0ed-f342-4ec6-b774-c79b47b60e2d"
        },
        "nym": {
            "TeamName": "New York Mets",
            "TeamCode": "f246a5e5-afdb-479c-9aaa-c68beeda7af6"
        },
        "nyy": {
            "TeamName": "New York Yankees",
            "TeamCode": "a09ec676-f887-43dc-bbb3-cf4bbaee9a18"
        },
        "oak": {
            "TeamName": "Oakland Athletics",
            "TeamCode": "27a59d3b-ff7c-48ea-b016-4798f560f5e1"
        },
        "phi": {
            "TeamName": "Philadelphia Phillies",
            "TeamCode": "2142e1ba-3b40-445c-b8bb-f1f8b1054220"
        },
        "pit": {
            "TeamName": "Pittsburgh Pirates",
            "TeamCode": "481dfe7e-5dab-46ab-a49f-9dcc2b6e2cfd"
        },
        "sdg": {
            "TeamName": "San Diego Padres",
            "TeamCode": "d52d5339-cbdd-43f3-9dfa-a42fd588b9a3"
        },
        "sfo": {
            "TeamName": "San Francisco Giants",
            "TeamCode": "a7723160-10b7-4277-a309-d8dd95a8ae65"
        },
        "sea": {
            "TeamName": "Seattle Mariners",
            "TeamCode": "43a39081-52b4-4f93-ad29-da7f329ea960"
        },
        "stl": {
            "TeamName": "St. Louis Cardinals",
            "TeamCode": "44671792-dc02-4fdd-a5ad-f5f17edaa9d7"
        },
        "stl2": {
            "TeamName": "St Louis Cardinals",
            "TeamCode": "44671792-dc02-4fdd-a5ad-f5f17edaa9d7"
        },

        "tam": {
            "TeamName": "Tampa Bay Rays",
            "TeamCode": "bdc11650-6f74-49c4-875e-778aeb7632d9"
        },
        "tex": {
            "TeamName": "Texas Rangers",
            "TeamCode": "d99f919b-1534-4516-8e8a-9cd106c6d8cd"
        },
        "tor": {
            "TeamName": "Toronto Blue Jays",
            "TeamCode": "1d678440-b4b1-4954-9b39-70afb3ebbcfa"
        },
        "was": {
            "TeamName": "Washington Nationals",
            "TeamCode": "d89bed32-3aee-4407-99e3-4103641b999a"
        },
        "was2": {
            "TeamName": "Washington Nationals  (A)",
            "TeamCode": "d89bed32-3aee-4407-99e3-4103641b999a"
        },
        "was3": {
            "TeamName": "Washington Nationals  (AAA)",
            "TeamCode": "d89bed32-3aee-4407-99e3-4103641b999a"
        }
    }

    NFL = {
        "buf": {
            "TeamName": "Buffalo Bills",
            "TeamCode": "BUF"
        },
        "buf2": {
            "TeamName": "Buffalo",
            "TeamCode": "BUF"
        },
        "mia": {
            "TeamName": "Miami Dolphins",
            "TeamCode": "MIA"
        },
        "mia2": {
            "TeamName": "Miami",
            "TeamCode": "MIA"
        },
        "nyj": {
            "TeamName": "New York Jets",
            "TeamCode": "NYJ"
        },
        "nyj2": {
            "TeamName": "N.Y. Jets",
            "TeamCode": "NYJ"
        },
        "nwe": {
            "TeamName": "NE Patriots",
            "TeamCode": "NE"
        },
        "nwe2": {
            "TeamName": "New England",
            "TeamCode": "NE"
        },
        "nwe3": {
            "TeamName": "New England Patriots",
            "TeamCode": "NE"
        },
        "den": {
            "TeamName": "Denver Broncos",
            "TeamCode": "DEN"
        },
        "den2": {
            "TeamName": "Denver",
            "TeamCode": "DEN"
        },
        "jac": {
            "TeamName": "Jacksonville Jaguars",
            "TeamCode": "JAC"
        },
        "jac2": {
            "TeamName": "Jacksonville",
            "TeamCode": "JAC"
        },
        "nor": {
            "TeamName": "New Orleans Saints",
            "TeamCode": "NO"
        },
        "nor2": {
            "TeamName": "New Orleans",
            "TeamCode": "NO"
        },
        "cle": {
            "TeamName": "Cleveland Browns",
            "TeamCode": "CLE"
        },
        "cle2": {
            "TeamName": "Cleveland",
            "TeamCode": "CLE"
        },
        "pit": {
            "TeamName": "Pittsburgh Steelers",
            "TeamCode": "PIT"
        },
        "pit2": {
            "TeamName": "Pittsburgh",
            "TeamCode": "PIT"
        },
        "kan": {
            "TeamName": "Kansas City Chiefs",
            "TeamCode": "KC"
        },
        "kan2": {
            "TeamName": "Kansas City",
            "TeamCode": "KC"
        },
        "bal": {
            "TeamName": "Baltimore Ravens",
            "TeamCode": "BAL"
        },
        "bal2": {
            "TeamName": "Baltimore Ravens",
            "TeamCode": "BAL"
        },
        "cin": {
            "TeamName": "Cincinnati Bengals",
            "TeamCode": "CIN"
        },
        "phi": {
            "TeamName": "Philadelphia Eagles",
            "TeamCode": "PHI"
        },
        "hou": {
            "TeamName": "Houston Texans",
            "TeamCode": "HOU"
        },
        "lar": {
            "TeamName": "Los Angeles Rams",
            "TeamCode": "LA"
        },
        "lar2": {
            "TeamName": "L.A. Rams",
            "TeamCode": "LA"
        },
        "tam": {
            "TeamName": "Tampa Bay Bucs",
            "TeamCode": "TB"
        },
        "tam2": {
            "TeamName": "Tampa Bay Buccaneers",
            "TeamCode": "TB"
        },
        "gnb": {
            "TeamName": "Green Bay Packers",
            "TeamCode": "GB"
        },
        "dal": {
            "TeamName": "Dallas Cowboys",
            "TeamCode": "DAL"
        },
        "oak": {
            "TeamName": "Oakland Raiders",
            "TeamCode": "OAK"
        },
        "ind": {
            "TeamName": "Indianapolis Colts",
            "TeamCode": "IND"
        },
        "sfo": {
            "TeamName": "San Francisco 49ers",
            "TeamCode": "SF"
        },
        "sfo2": {
            "TeamName": "San Francisco 49Ers",
            "TeamCode": "SF"
        },
        "ten": {
            "TeamName": "Tennessee Titans",
            "TeamCode": "TEN"
        },
        "chi": {
            "TeamName": "Chicago Bears",
            "TeamCode": "CHI"
        },
        "det": {
            "TeamName": "Detroit Lions",
            "TeamCode": "DET"
        },
        "nyg": {
            "TeamName": "N.Y. Giants",
            "TeamCode": "NYG"
        },
        "nyg2": {
            "TeamName": "New York Giants",
            "TeamCode": "NYG"
        },
        "was": {
            "TeamName": "Washington Redskins",
            "TeamCode": "WAS"
        },
        "atl": {
            "TeamName": "Atlanta Falcons",
            "TeamCode": "ATL"
        },
        "NA": {
            "TeamName": "San Diego Chargers",
            "TeamCode": "SD"
        },
        "car": {
            "TeamName": "Carolina Panthers",
            "TeamCode": "CAR"
        },
        "min": {
            "TeamName": "Minnesota Vikings",
            "TeamCode": "MIN"
        },
        "ari": {
            "TeamName": "Arizona Cardinals",
            "TeamCode": "ARI"
        },
        "sea": {
            "TeamName": "Seattle Seahawks",
            "TeamCode": "SEA"
        },
        "lac": {
            "TeamName": "Los Angeles Chargers",
            "TeamCode": "LAC"
        },
        "lac2": {
            "TeamName": "L.A. Chargers",
            "TeamCode": "LAC"
        }
    }

    NBA = {
        "Toronto Raptors": {
            "TeamName": "Toronto Raptors",
            "TeamCode": "583ecda6-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Cleveland Cavaliers": {
            "TeamName": "Cleveland Cavaliers",
            "TeamCode": "583ec773-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Sacramento Kings": {
            "TeamName": "Sacramento Kings",
            "TeamCode": "583ed0ac-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Indiana Pacers": {
            "TeamName": "Indiana Pacers",
            "TeamCode": "583ec7cd-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "San Antonio Spurs": {
            "TeamName": "San Antonio Spurs",
            "TeamCode": "583ecd4f-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Phoenix Suns": {
            "TeamName": "Phoenix Suns",
            "TeamCode": "583ecfa8-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Oklahoma City Thunder": {
            "TeamName": "Oklahoma City Thunder",
            "TeamCode": "583ecfff-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Memphis Grizzlies": {
            "TeamName": "Memphis Grizzlies",
            "TeamCode": "583eca88-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Brooklyn Nets": {
            "TeamName": "Brooklyn Nets",
            "TeamCode": "583ec9d6-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Orlando Magic": {
            "TeamName": "Orlando Magic",
            "TeamCode": "583ed157-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Denver Nuggets": {
            "TeamName": "Denver Nuggets",
            "TeamCode": "583ed102-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Chicago Bulls": {
            "TeamName": "Chicago Bulls",
            "TeamCode": "583ec5fd-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "New York Knicks": {
            "TeamName": "New York Knicks",
            "TeamCode": "583ec70e-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Houston Rockets": {
            "TeamName": "Houston Rockets",
            "TeamCode": "583ecb3a-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Detroit Pistons": {
            "TeamName": "Detroit Pistons",
            "TeamCode": "583ec928-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Charlotte Hornets": {
            "TeamName": "Charlotte Hornets",
            "TeamCode": "583ec97e-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Miami Heat": {
            "TeamName": "Miami Heat",
            "TeamCode": "583ecea6-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Boston Celtics": {
            "TeamName": "Boston Celtics",
            "TeamCode": "583eccfa-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Utah Jazz": {
            "TeamName": "Utah Jazz",
            "TeamCode": "583ece50-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Los Angeles Clippers": {
            "TeamName": "Los Angeles Clippers",
            "TeamCode": "583ecdfb-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "LA Clippers": {
            "TeamName": "LA Clippers",
            "TeamCode": "583ecdfb-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Los Angeles Lakers": {
            "TeamName": "Los Angeles Lakers",
            "TeamCode": "583ecae2-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "LA Lakers": {
            "TeamName": "LA Lakers",
            "TeamCode": "583ecae2-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Dallas Mavericks": {
            "TeamName": "Dallas Mavericks",
            "TeamCode": "583ecf50-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Atlanta Hawks": {
            "TeamName": "Atlanta Hawks",
            "TeamCode": "583ecb8f-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "New Orleans Pelicans": {
            "TeamName": "New Orleans Pelicans",
            "TeamCode": "583ecc9a-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Golden State Warriors": {
            "TeamName": "Golden State Warriors",
            "TeamCode": "583ec825-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Philadelphia 76ers": {
            "TeamName": "Philadelphia 76ers",
            "TeamCode": "583ec87d-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Philadelphia 76Ers": {
            "TeamName": "Philadelphia 76ers",
            "TeamCode": "583ec87d-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Milwaukee Bucks": {
            "TeamName": "Milwaukee Bucks",
            "TeamCode": "583ecefd-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Washington Wizards": {
            "TeamName": "Washington Wizards",
            "TeamCode": "583ec8d4-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Portland Trail Blazers": {
            "TeamName": "Portland Trail Blazers",
            "TeamCode": "583ed056-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Minnesota Timberwolves": {
            "TeamName": "Timberwolves",
            "TeamCode": "583eca2f-fb46-11e1-82cb-f4ce4684ea4c"
        },
        "Minnesota": {
            "TeamName": "Minnesota",
            "TeamCode": "583eca2f-fb46-11e1-82cb-f4ce4684ea4c"
        }
    }

    EuroL = {
        "Everton": {
            "TeamName": "Everton",
            "TeamCode": "EVE"
        },
        "Arsenal": {
            "TeamName": "Arsenal",
            "TeamCode": "ARS"
        },
        "Galatasaray": {
            "TeamName": "Galatasaray",
            "TeamCode": "GAL"
        },
        "Lazio": {
            "TeamName": "Lazio",
            "TeamCode": "LAZ"
        },
        "Marseille": {
            "TeamName": "Olympique Marseille",
            "TeamCode": "MRS"
        },
        "RB Salzburg": {
            "TeamName": "Salzburg",
            "TeamCode": "SAL"
        },
        "Celtic": {
            "TeamName": "Celtic",
            "TeamCode": "CEL"
        },
        "Crvena Zvezda": {
            "TeamName": "Crvena Zvezda",
            "TeamCode": "CRVE"
        },
        "Sporting CP": {
            "TeamName": "Sporting CP",
            "TeamCode": "SCP"
        },
        "Borussia Dortmund": {
            "TeamName": "Borussia Dortmund",
            "TeamCode": "BVB"
        },
        "Olympique Lyonnais": {
            "TeamName": "Olympique Lyonnais",
            "TeamCode": "LYON"
        },
        "Vitesse": {
            "TeamName": "Vitesse",
            "TeamCode": "VIT"
        },
        "Milan": {
            "TeamName": "Milan",
            "TeamCode": "MIL"
        },
        "RB Leipzig": {
            "TeamName": "RB Leipzig",
            "TeamCode": "RBL"
        },
        "Nice": {
            "TeamName": "Nice",
            "TeamCode": "NICE"
        },
        "Dynamo Kyiv": {
            "TeamName": "Dynamo Kyiv",
            "TeamCode": "KIEV"
        },
        "CSKA Moskva": {
            "TeamName": "CSKA Moskva",
            "TeamCode": "CSKA"
        },
        "Real Sociedad": {
            "TeamName": "Real Sociedad",
            "TeamCode": "RSO"
        },
        "Napoli": {
            "TeamName": "Napoli",
            "TeamCode": "NAP"
        },
        "Sheriff": {
            "TeamName": "Sheriff",
            "TeamCode": "FST"
        },
        "Young Boys": {
            "TeamName": "Young Boys",
            "TeamCode": "BSCY"
        },
        "Atalanta": {
            "TeamName": "Atalanta",
            "TeamCode": "ATA"
        },
        "AEK Athens": {
            "TeamName": "AEK Athens",
            "TeamCode": "AEK"
        },
        "Vitória Guimarães": {
            "TeamName": "Vitória Guimarães",
            "TeamCode": "GUI"
        },
        "Skendija 79": {
            "TeamName": "Skendija 79",
            "TeamCode": "Sken"
        },
        "Sporting": {
            "TeamName": "Sporting",
            "TeamCode": "BRAG"
        },
        "Zulte-Waregem": {
            "TeamName": "Zulte-Waregem",
            "TeamCode": "ZUL"
        },
        "Rosenborg": {
            "TeamName": "Rosenborg",
            "TeamCode": "ROS"
        },
        "Östersunds FK": {
            "TeamName": "Östersunds FK",
            "TeamCode": "OFK"
        },
        "Konyaspor": {
            "TeamName": "Konyaspor",
            "TeamCode": "KNY"
        },
        "Hoffenheim": {
            "TeamName": "Hoffenheim",
            "TeamCode": "HOF"
        },
        "Partizan": {
            "TeamName": "Partizan",
            "TeamCode": "FKP"
        },
        "Ludogorets": {
            "TeamName": "Ludogorets",
            "TeamCode": "LUD"
        },
        "Zenit": {
            "TeamName": "Zenit",
            "TeamCode": "ZEN"
        },
        "Hertha BSC": {
            "TeamName": "Hertha BSC",
            "TeamCode": "HER"
        },
        "Rijeka": {
            "TeamName": "Rijeka",
            "TeamCode": "RIJ"
        },
        "Villarreal": {
            "TeamName": "Villarreal",
            "TeamCode": "VIL"
        },
        "Viktoria Plzeň": {
            "TeamName": "Viktoria Plzeň",
            "TeamCode": "VPLZ"
        },
        "Austria Wien": {
            "TeamName": "Austria Wien",
            "TeamCode": "VIE"
        },
        "İstanbul Başakşehir": {
            "TeamName": "İstanbul Başakşehir",
            "TeamCode": "IBUY"
        },
        "BATE": {
            "TeamName": "BATE",
            "TeamCode": "BATE"
        },
        "Skënderbeu Korçë": {
            "TeamName": "Skënderbeu Korçë",
            "TeamCode": "SKE"
        },
        "Vardar": {
            "TeamName": "Vardar",
            "TeamCode": "VAR"
        },
        "Astana": {
            "TeamName": "Astana",
            "TeamCode": "ASTA"
        },
        "Apollon": {
            "TeamName": "Apollon",
            "TeamCode": "Apol"
        },
        "Atlético Madrid": {
            "TeamName": "Atlético Madrid",
            "TeamCode": "AMA"
        },
        "Athletic Club": {
            "TeamName": "Athletic Club",
            "TeamCode": "ABI"
        },
        "Lugano": {
            "TeamName": "Lugano",
            "TeamCode": "LUG"
        },
        "CSKA Moscow": {
            "TeamName": "CSKA Moscow",
            "TeamCode": "CSKA"
        },
        "Olympique Marseille": {
            "TeamName": "Olympique Marseille",
            "TeamCode": "MRS"
        }
    }

    UEFA = {
        "Barcelona": {
            "TeamName": "Barcelona",
            "TeamCode": "BAR"
        },
        "Anderlecht": {
            "TeamName": "Anderlecht",
            "TeamCode": "AND"
        },
        "APOEL": {
            "TeamName": "APOEL",
            "TeamCode": "ANI"
        },
        "Atlético Madrid": {
            "TeamName": "Atlético Madrid",
            "TeamCode": "AMA"
        },
        "Basel": {
            "TeamName": "Basel",
            "TeamCode": "BAS"
        },
        "Bayern München": {
            "TeamName": "Bayern München",
            "TeamCode": "BMU"
        },
        "Bayern Munich": {
            "TeamName": "Munich",
            "TeamCode": "BMU"
        },
        "Benfica": {
            "TeamName": "Benfica",
            "TeamCode": "BEN"
        },
        "Beşiktaş": {
            "TeamName": "Beşiktaş",
            "TeamCode": "BES"
        },
        "Borussia Dortmund": {
            "TeamName": "Borussia Dortmund",
            "TeamCode": "BVB"
        },
        "Celtic": {
            "TeamName": "Celtic",
            "TeamCode": "CEL"
        },
        "Chelsea": {
            "TeamName": "Chelsea",
            "TeamCode": "CHE"
        },
        "CSKA Moskva": {
            "TeamName": "CSKA Moskva",
            "TeamCode": "CSKA"
        },
        "Feyenoord": {
            "TeamName": "Feyenoord",
            "TeamCode": "FEY"
        },
        "Juventus": {
            "TeamName": "Juventus",
            "TeamCode": "JUV"
        },
        "Liverpool": {
            "TeamName": "Liverpool",
            "TeamCode": "LIV"
        },
        "Manchester City": {
            "TeamName": "Manchester City",
            "TeamCode": "MNC"
        },
        "Man. City": {
            "TeamName": "Manchester City",
            "TeamCode": "MNC"
        },
        "Manchester United": {
            "TeamName": "Manchester United",
            "TeamCode": "MAN"
        },
        "Man. United": {
            "TeamName": "Manchester United",
            "TeamCode": "MAN"
        },
        "Maribor": {
            "TeamName": "Maribor",
            "TeamCode": "MARI"
        },
        "Monaco": {
            "TeamName": "Monaco",
            "TeamCode": "MON"
        },
        "Napoli": {
            "TeamName": "Napoli",
            "TeamCode": "NAP"
        },
        "Olympiakos Piraeus": {
            "TeamName": "Olympiakos Piraeus",
            "TeamCode": "OLY"
        },
        "Porto": {
            "TeamName": "Porto",
            "TeamCode": "POR"
        },
        "PSG": {
            "TeamName": "PSG",
            "TeamCode": "PSG"
        },
        "Qarabağ": {
            "TeamName": "Qarabağ",
            "TeamCode": "QBG"
        },
        "RB Leipzig": {
            "TeamName": "RB Leipzig",
            "TeamCode": "RBL"
        },
        "Real Madrid": {
            "TeamName": "Real Madrid",
            "TeamCode": "RMA"
        },
        "Roma": {
            "TeamName": "Roma",
            "TeamCode": "ROMA"
        },
        "Sevilla": {
            "TeamName": "Sevilla",
            "TeamCode": "SEV"
        },
        "Shakhtar Donetsk": {
            "TeamName": "Shakhtar Donetsk",
            "TeamCode": "SHAK"
        },
        "Shakhtar": {
            "TeamName": "Shakhtar Donetsk",
            "TeamCode": "SDO"
        },
        "Spartaks Jūrmala": {
            "TeamName": "Spartaks Jūrmala",
            "TeamCode": "SMO"
        },
        "Sporting CP": {
            "TeamName": "Sporting CP",
            "TeamCode": "SCP"
        },
        "Sporting": {
            "TeamName": "Sporting CP",
            "TeamCode": "SCP"
        },
        "Tottenham Hotspur": {
            "TeamName": "Tottenham Hotspur",
            "TeamCode": "TOT"
        },
        "Tottenham": {
            "TeamName": "Tottenham Hotspur",
            "TeamCode": "TOT"
        }
    }

    LALIGA = {
        "Real Valladolid": {
            "TeamName": "Real Valladolid",
            "TeamCode": "VLD"
        },
        "Valladolid": {
            "TeamName": "Real Valladolid",
            "TeamCode": "VLD"
        },
        "SD Huesca": {
            "TeamName": "SD Huesca",
            "TeamCode": "HUE"
        },
        "Huesca": {
            "TeamName": "SD Huesca",
            "TeamCode": "HUE"
        },
        "Rayo Vallecano": {
            "TeamName": "Rayo Vallecano",
            "TeamCode": "RAY"
        },
        "Barcelona": {
            "TeamName": "Barcelona",
            "TeamCode": "BAR"
        },
        "FC Barcelona": {
            "TeamName": "Barcelona",
            "TeamCode": "BAR"
        },
        "Eibar": {
            "TeamName": "Eibar",
            "TeamCode": "EIB"
        },
        "Deportivo La Coruña": {
            "TeamName": "Deportivo La Coruña",
            "TeamCode": "DEP"
        },
        "Deportivo de La Coruña": {
            "TeamName": "Deportivo La Coruña",
            "TeamCode": "DEP"
        },
        "Deportivo": {
            "TeamName": "Deportivo La Coruña",
            "TeamCode": "DEP"
        },
        "Celta de Vigo": {
            "TeamName": "Celta de Vigo",
            "TeamCode": "CVI"
        },
        "Celta Vigo": {
            "TeamName": "Celta Vigo",
            "TeamCode": "CVI"
        },
        "Celta": {
            "TeamName": "Celta Vigo",
            "TeamCode": "CVI"
        },
        "Girona": {
            "TeamName": "Girona",
            "TeamCode": "GIR"
        },
        "Valencia": {
            "TeamName": "Valencia",
            "TeamCode": "VAL"
        },
        "Valencia CF": {
            "TeamName": "Valencia",
            "TeamCode": "VAL"
        },
        "VAL": {
            "TeamName": "Valencia",
            "TeamCode": "VAL"
        },
        "Getafe": {
            "TeamName": "Getafe",
            "TeamCode": "GET"
        },
        "Real Betis": {
            "TeamName": "Real Betis",
            "TeamCode": "BET"
        },
        "BET": {
            "TeamName": "Real Betis",
            "TeamCode": "BET"
        },
        "Betis": {
            "TeamName": "Real Betis",
            "TeamCode": "BET"
        },
        "Málaga": {
            "TeamName": "Málaga",
            "TeamCode": "MCF"
        },
        "Malaga": {
            "TeamName": "Málaga",
            "TeamCode": "MCF"
        },
        "MAG": {
            "TeamName": "Málaga",
            "TeamCode": "MAG"
        },
        "Espanyol": {
            "TeamName": "Espanyol",
            "TeamCode": "ESP"
        },
        "Las Palmas": {
            "TeamName": "Las Palmas",
            "TeamCode": "LPA"
        },
        "LP": {
            "TeamName": "Las Palmas",
            "TeamCode": "LP"
        },
        "Real Sociedad": {
            "TeamName": "Real Sociedad",
            "TeamCode": "RSO"
        },
        "Sevilla": {
            "TeamName": "Sevilla",
            "TeamCode": "SEV"
        },
        "Leganés": {
            "TeamName": "Leganés",
            "TeamCode": "LEG"
        },
        "Leganes": {
            "TeamName": "Leganés",
            "TeamCode": "LEG"
        },
        "LGN": {
            "TeamName": "Leganés",
            "TeamCode": "LGN"
        },
        "Atlético Madrid": {
            "TeamName": "Atlético Madrid",
            "TeamCode": "AMA"
        },
        "Atletico Madrid": {
            "TeamName": "Atlético Madrid",
            "TeamCode": "AMA"
        },
        "Atlético de Madrid": {
            "TeamName": "Atlético Madrid",
            "TeamCode": "AMA"
        },
        "ATL": {
            "TeamName": "Atlético Madrid",
            "TeamCode": "AMA"
        },
        "Atl&eacute;tico Madrid": {
            "TeamName": "Atlético Madrid",
            "TeamCode": "AMA"
        },
        "Levante": {
            "TeamName": "Levante",
            "TeamCode": "LEV"
        },
        "Real Madrid": {
            "TeamName": "Real Madrid",
            "TeamCode": "RMA"
        },
        "RMD": {
            "TeamName": "Real Madrid",
            "TeamCode": "RMA"
        },
        "Deportivo Alavés": {
            "TeamName": "Deportivo Alavés",
            "TeamCode": "ALA"
        },
        "ALA": {
            "TeamName": "Deportivo Alavés",
            "TeamCode": "ALA"
        },
        "Athletic Club": {
            "TeamName": "Athletic Club",
            "TeamCode": "ABI"
        },
        "Athletic": {
            "TeamName": "Athletic Club",
            "TeamCode": "ABI"
        },
        "Athletic Bilbao": {
            "TeamName": "Athletic Bilbao",
            "TeamCode": "ABI"
        },
        "ATH": {
            "TeamName": "Athletic Bilbao",
            "TeamCode": "ABI"
        },
        "Villarreal": {
            "TeamName": "Villarreal",
            "TeamCode": "VIL"
        },
        "Alavés": {
            "TeamName": "Alavés",
            "TeamCode": "ALA"
        },
        "Alaves": {
            "TeamName": "Alavés",
            "TeamCode": "ALA"
        },
        "Deportivo Alaves": {
            "TeamName": "Alavés",
            "TeamCode": "ALA"
        },
        "RCD Mallorca": {
            "TeamName": "RCD Mallorca",
            "TeamCode": "MLA"
        },
        "Granada CF": {
            "TeamName": "Granada CF",
            "TeamCode": "GCF"
        },
        "CA Osasuna": {
            "TeamName": "CA Osasuna",
            "TeamCode": "OSA"
        }
    }

    EFL = {
        "Sunderland": {
            "TeamName": "Sunderland",
            "TeamCode": "SUN"
        },
        "Middlesbrough": {
            "TeamName": "Middlesbrough",
            "TeamCode": "MID"
        },
        "Fulham": {
            "TeamName": "Fulham",
            "TeamCode": "FUL"
        },
        "Birmingham": {
            "TeamName": "Birmingham City",
            "TeamCode": "BIR"
        },
        "Aston Villa": {
            "TeamName": "Aston Villa",
            "TeamCode": "AVL"
        },
        "Bolton": {
            "TeamName": "Bolton Wanderers",
            "TeamCode": "BLT"
        },
        "Sheffield United": {
            "TeamName": "Sheffield United",
            "TeamCode": "SHEF"
        },
        "Hull City": {
            "TeamName": "Hull City",
            "TeamCode": "HUL"
        },
        "Reading": {
            "TeamName": "Reading",
            "TeamCode": "REA"
        },
        "Derby County": {
            "TeamName": "Derby County",
            "TeamCode": "DER"
        },
        "Wolverhampton": {
            "TeamName": "Wolverhampton",
            "TeamCode": "WOL"
        },
        "Wolverhampton Wanderers": {
            "TeamName": "Wolverhampton",
            "TeamCode": "WOL"
        },
        "Norwich City": {
            "TeamName": "Norwich City",
            "TeamCode": "NOR"
        },
        "Queens Park Rangers": {
            "TeamName": "Queens Park Rangers",
            "TeamCode": "QPR"
        },
        "QPR": {
            "TeamName": "Queens Park Rangers",
            "TeamCode": "QPR"
        },
        "Barnsley": {
            "TeamName": "Barnsley",
            "TeamCode": "BAR"
        },
        "Sheffield Wednesday": {
            "TeamName": "Sheffield Wednesday",
            "TeamCode": "SHW"
        },
        "Sheffield Wed.": {
            "TeamName": "Sheffield Wednesday",
            "TeamCode": "SHW"
        },
        "Nottingham Forest": {
            "TeamName": "Nottingham Forest",
            "TeamCode": "FOR"
        },
        "Nottm Forest": {
            "TeamName": "Nottm Forest",
            "TeamCode": "FOR"
        },
        "Millwall": {
            "TeamName": "Millwall",
            "TeamCode": "MIL"
        },
        "Cardiff City": {
            "TeamName": "Cardiff City",
            "TeamCode": "CAR"
        },
        "Leeds United": {
            "TeamName": "Leeds United",
            "TeamCode": "LEE"
        },
        "Preston": {
            "TeamName": "Preston North End",
            "TeamCode": "PNE"
        },
        "Ipswich Town": {
            "TeamName": "Ipswich Town",
            "TeamCode": "IPS"
        },
        "Bristol City": {
            "TeamName": "Bristol City",
            "TeamCode": "BRC"
        },
        "Burton Albion": {
            "TeamName": "Burton Albion",
            "TeamCode": "BUR"
        },
        "Brentford": {
            "TeamName": "Brentford",
            "TeamCode": "BRN"
        }
    }

    EPL = {
        "Cardiff City": {
            "TeamName": "Cardiff City",
            "TeamCode": "CAR"
        },
        "Cardiff": {
            "TeamName": "Cardiff City",
            "TeamCode": "CAR"
        },
        "Fulham": {
            "TeamName": "Fulham",
            "TeamCode": "FUL"
        },
        "Wolverhampton": {
            "TeamName": "Wolverhampton",
            "TeamCode": "WOL"
        },
        "Wolverhampton Wanderers": {
            "TeamName": "Wolverhampton",
            "TeamCode": "WOL"
        },
        "Wolves": {
            "TeamName": "Wolverhampton",
            "TeamCode": "WOL"
        },
        "AFC Bournemouth": {
            "TeamName": "AFC Bournemouth",
            "TeamCode": "BOU"
        },
        "Bournemouth": {
            "TeamName": "AFC Bournemouth",
            "TeamCode": "BOU"
        },
        "Arsenal": {
            "TeamName": "Arsenal",
            "TeamCode": "ARS"
        },
        "Brighton & Hove Albion": {
            "TeamName": "Brighton & Hove Albion",
            "TeamCode": "BHA"
        },
        "Brighton": {
            "TeamName": "Brighton & Hove Albion",
            "TeamCode": "BHA"
        },
        "Burnley": {
            "TeamName": "Burnley",
            "TeamCode": "BUR"
        },
        "Chelsea": {
            "TeamName": "Chelsea",
            "TeamCode": "CHE"
        },
        "Crystal Palace": {
            "TeamName": "Crystal Palace",
            "TeamCode": "CRY"
        },
        "Everton": {
            "TeamName": "Everton",
            "TeamCode": "EVE"
        },
        "Hull": {
            "TeamName": "Hull",
            "TeamCode": "HUL"
        },
        "Huddersfield Town": {
            "TeamName": "Huddersfield Town",
            "TeamCode": "HUD"
        },
        "Huddersfield": {
            "TeamName": "Huddersfield Town",
            "TeamCode": "HUD"
        },
        "Leicester City": {
            "TeamName": "Leicester City",
            "TeamCode": "LEI"
        },
        "Leicester": {
            "TeamName": "Leicester City",
            "TeamCode": "LEI"
        },
        "Liverpool": {
            "TeamName": "Liverpool",
            "TeamCode": "LIV"
        },
        "Manchester City": {
            "TeamName": "Manchester City",
            "TeamCode": "MNC"
        },
        "Man. City": {
            "TeamName": "Manchester City",
            "TeamCode": "MNC"
        },
        "Man City": {
            "TeamName": "Manchester City",
            "TeamCode": "MNC"
        },
        "Manchester United": {
            "TeamName": "Manchester United",
            "TeamCode": "MAN"
        },
        "Manchester Utd": {
            "TeamName": "Manchester United",
            "TeamCode": "MAN"
        },
        "Man. United": {
            "TeamName": "Manchester United",
            "TeamCode": "MAN"
        },
        "Newcastle United": {
            "TeamName": "Newcastle United",
            "TeamCode": "NEW"
        },
        "MCI": {
            "TeamName": "Manchester City",
            "TeamCode": "MCI"
        },
        "MUN": {
            "TeamName": "Manchester United",
            "TeamCode": "MUN"
        },
        "Newcastle": {
            "TeamName": "Newcastle United",
            "TeamCode": "NEW"
        },
        "Southampton": {
            "TeamName": "Southampton",
            "TeamCode": "SOU"
        },
        "Stoke City": {
            "TeamName": "Stoke City",
            "TeamCode": "STK"
        },
        "Sunderland": {
            "TeamName": "Sunderland",
            "TeamCode": "SUN"
        },
        "Swansea City": {
            "TeamName": "Swansea City",
            "TeamCode": "SWA"
        },
        "Tottenham Hotspur": {
            "TeamName": "Tottenham Hotspur",
            "TeamCode": "TOT"
        },
        "Tottenham": {
            "TeamName": "Tottenham Hotspur",
            "TeamCode": "TOT"
        },
        "Watford": {
            "TeamName": "Watford",
            "TeamCode": "WAT"
        },
        "West Bromwich Albion": {
            "TeamName": "West Bromwich Albion",
            "TeamCode": "WBA"
        },
        "West Brom": {
            "TeamName": "West Bromwich Albion",
            "TeamCode": "WBA"
        },
        "West Ham United": {
            "TeamName": "West Ham United",
            "TeamCode": "WHU"
        },
        "West Ham": {
            "TeamName": "West Ham United",
            "TeamCode": "WHU"
        },
        "Norwich": {
            "TeamName": "Norwich",
            "TeamCode": "NOR"
        },
        "Norwich City": {
            "TeamName": "Norwich",
            "TeamCode": "NOR"
        },
        "Aston Villa": {
            "TeamName": "Aston Villa",
            "TeamCode": "AVA"
        },
        "Sheffield United": {
            "TeamName": "Sheffield United",
            "TeamCode": "SHU"
        }
    }

    Bund = {
        "FORTUNA DUSSELDORF": {
            "TeamName": "FORTUNA DUSSELDORF",
            "TeamCode": "DUS"
        },
        "Fortuna Dusseldorf": {
            "TeamName": "Fortuna Dusseldorf",
            "TeamCode": "DUS"
        },
        "Fortuna D&uuml;sseldorf": {
            "TeamName": "Fortuna Dusseldorf",
            "TeamCode": "DUS"
        },
        "Fortuna": {
            "TeamName": "Fortuna",
            "TeamCode": "DUS"
        },
        "SC Paderborn 07": {
            "TeamName": "SC Paderborn 07",
            "TeamCode": "PAD"
        },
        "SC Paderborn": {
            "TeamName": "SC Paderborn",
            "TeamCode": "PAD"
        },
        "FC Nürnberg": {
            "TeamName": "FC Nürnberg",
            "TeamCode": "NUR"
        },
        "1. FC Nürnberg": {
            "TeamName": "FC Nürnberg",
            "TeamCode": "NUR"
        },
        "Nurenberg": {
            "TeamName": "FC Nürnberg",
            "TeamCode": "NUR"
        },
        "Nuremberg": {
            "TeamName": "FC Nürnberg",
            "TeamCode": "NUR"
        },
        "1. FC N&uuml;rnberg": {
            "TeamName": "FC Nürnberg",
            "TeamCode": "NUR"
        },
        "Schalke 04": {
            "TeamName": "Schalke 04",
            "TeamCode": "SCH"
        },
        "FC Schalke 04": {
            "TeamName": "Schalke 04",
            "TeamCode": "SCH"
        },
        "Schalke": {
            "TeamName": "Schalke 04",
            "TeamCode": "SCH"
        },
        "SKE": {
            "TeamName": "Schalke 04",
            "TeamCode": "SKE"
        },
        "Borussia Dortmund": {
            "TeamName": "Borussia Dortmund",
            "TeamCode": "BVB"
        },
        "Bor. Dortmund": {
            "TeamName": "Borussia Dortmund",
            "TeamCode": "BVB"
        },
        "DOR": {
            "TeamName": "Borussia Dortmund",
            "TeamCode": "DOR"
        },
        "Werder Bremen": {
            "TeamName": "Werder Bremen",
            "TeamCode": "BRE"
        },
        "Augsburg": {
            "TeamName": "Augsburg",
            "TeamCode": "AUG"
        },
        "FC Augsburg": {
            "TeamName": "Augsburg",
            "TeamCode": "AUG"
        },
        "RB Leipzig": {
            "TeamName": "RB Leipzig",
            "TeamCode": "RBL"
        },
        "Eintracht Frankfurt": {
            "TeamName": "Eintracht Frankfurt",
            "TeamCode": "FRA"
        },
        "Frankfurt": {
            "TeamName": "Eintracht Frankfurt",
            "TeamCode": "FRA"
        },
        "EF": {
            "TeamName": "Eintracht Frankfurt",
            "TeamCode": "EF"
        },
        "Bayern München": {
            "TeamName": "Bayern München",
            "TeamCode": "BMU"
        },
        "Bayern Munich": {
            "TeamName": "Bayern München",
            "TeamCode": "BMU"
        },
        "BM": {
            "TeamName": "Bayern München",
            "TeamCode": "BM"
        },
        "Wolfsburg": {
            "TeamName": "Wolfsburg",
            "TeamCode": "WLF"
        },
        "VfL Wolfsburg": {
            "TeamName": "Wolfsburg",
            "TeamCode": "WLF"
        },
        "WOL": {
            "TeamName": "Wolfsburg",
            "TeamCode": "WOL"
        },
        "Borussia M'gladbach": {
            "TeamName": "Borussia M'gladbach",
            "TeamCode": "MGB"
        },
        "M&ouml;nchengladbach": {
            "TeamName": "Borussia M'gladbach",
            "TeamCode": "MGB"
        },
        "MUN": {
            "TeamName": "Borussia M'gladbach",
            "TeamCode": "MGB"
        },
        "M'gladbach": {
            "TeamName": "Borussia M'gladbach",
            "TeamCode": "MGB"
        },
        "Mainz 05": {
            "TeamName": "Mainz 05",
            "TeamCode": "MNZ"
        },
        "FSV Mainz 05": {
            "TeamName": "Mainz 05",
            "TeamCode": "MNZ"
        },
        "MAI": {
            "TeamName": "Mainz 05",
            "TeamCode": "MAI"
        },
        "Hannover 96": {
            "TeamName": "Hannover 96",
            "TeamCode": "HAN"
        },
        "Hamburger SV": {
            "TeamName": "Hamburger SV",
            "TeamCode": "HSV"
        },
        "Hamburg": {
            "TeamName": "Hamburger SV",
            "TeamCode": "HSV"
        },
        "HAM": {
            "TeamName": "Hamburger SV",
            "TeamCode": "HAM"
        },
        "Hoffenheim": {
            "TeamName": "Hoffenheim",
            "TeamCode": "HOF"
        },
        "1899 Hoffenheim": {
            "TeamName": "Hoffenheim",
            "TeamCode": "HOF"
        },
        "Hertha BSC": {
            "TeamName": "Hertha BSC",
            "TeamCode": "HER"
        },
        "Hertha BSC Berlin": {
            "TeamName": "Hertha BSC",
            "TeamCode": "HER"
        },
        "Hertha Berlin": {
            "TeamName": "Hertha BSC",
            "TeamCode": "HER"
        },
        "HB": {
            "TeamName": "Hertha BSC",
            "TeamCode": "HB"
        },
        "Stuttgart": {
            "TeamName": "Stuttgart",
            "TeamCode": "STU"
        },
        "VfB Stuttgart": {
            "TeamName": "Stuttgart",
            "TeamCode": "STU"
        },
        "SGT": {
            "TeamName": "Stuttgart",
            "TeamCode": "SGT"
        },
        "Köln": {
            "TeamName": "Köln",
            "TeamCode": "COL"
        },
        "FC Köln": {
            "TeamName": "Köln",
            "TeamCode": "COL"
        },
        "1. FC Köln": {
            "TeamName": "Köln",
            "TeamCode": "COL"
        },
        "Cologne": {
            "TeamName": "Köln",
            "TeamCode": "COL"
        },
        "KLN": {
            "TeamName": "Köln",
            "TeamCode": "KLN"
        },
        "Bayer Leverkusen": {
            "TeamName": "Bayer Leverkusen",
            "TeamCode": "LEV"
        },
        "Freiburg": {
            "TeamName": "Freiburg",
            "TeamCode": "FRE"
        },
        "SC Freiburg": {
            "TeamName": "Freiburg",
            "TeamCode": "FRE"
        },
        "FBG": {
            "TeamName": "Freiburg",
            "TeamCode": "FBG"
        },
        "Mönchengladbach": {
            "TeamName": "Mönchengladbach",
            "TeamCode": "MGB"
        },
        "FC Cologne": {
            "TeamName": "FC Cologne",
            "TeamCode": "COL"
        },
        "FC Union Berlin": {
            "TeamName": "FC Union Berlin",
            "TeamCode": "FCU"
        }
    }

    SerieA = {
        "Roma": {
            "TeamName": "Roma",
            "TeamCode": "ROMA"
        },
        "ROM": {
            "TeamName": "Roma",
            "TeamCode": "ROM"
        },
        "Lazio": {
            "TeamName": "Lazio",
            "TeamCode": "LAZ"
        },
        "Crotone": {
            "TeamName": "Crotone",
            "TeamCode": "CRO"
        },
        "Chievo": {
            "TeamName": "Chievo",
            "TeamCode": "CVO"
        },
        "CHV": {
            "TeamName": "Chievo",
            "TeamCode": "CHV"
        },
        "Genoa": {
            "TeamName": "Genoa",
            "TeamCode": "GEN"
        },
        "Fiorentina": {
            "TeamName": "Fiorentina",
            "TeamCode": "FIO"
        },
        "Milan": {
            "TeamName": "Milan",
            "TeamCode": "MIL"
        },
        "AC Milan": {
            "TeamName": "Milan",
            "TeamCode": "MIL"
        },
        "Udinese": {
            "TeamName": "Udinese",
            "TeamCode": "UDI"
        },
        "UDN": {
            "TeamName": "Udinese",
            "TeamCode": "UDN"
        },
        "SPAL": {
            "TeamName": "SPAL",
            "TeamCode": "SPAL"
        },
        "SPL": {
            "TeamName": "SPAL",
            "TeamCode": "SPL"
        },
        "Sampdoria": {
            "TeamName": "Sampdoria",
            "TeamCode": "SMP"
        },
        "Benevento": {
            "TeamName": "Benevento",
            "TeamCode": "BEN"
        },
        "Cagliari": {
            "TeamName": "Cagliari",
            "TeamCode": "CAG"
        },
        "Napoli": {
            "TeamName": "Napoli",
            "TeamCode": "NAP"
        },
        "Torino": {
            "TeamName": "Torino",
            "TeamCode": "TOR"
        },
        "Juventus": {
            "TeamName": "Juventus",
            "TeamCode": "JUV"
        },
        "Atalanta": {
            "TeamName": "Atalanta",
            "TeamCode": "ATA"
        },
        "Hellas Verona": {
            "TeamName": "Hellas Verona",
            "TeamCode": "HEL"
        },
        "Verona": {
            "TeamName": "Hellas Verona",
            "TeamCode": "HEL"
        },
        "VNA": {
            "TeamName": "Hellas Verona",
            "TeamCode": "VNA"
        },
        "Sassuolo": {
            "TeamName": "Sassuolo",
            "TeamCode": "SAS"
        },
        "Internazionale": {
            "TeamName": "Internazionale",
            "TeamCode": "INT"
        },
        "Inter Milan": {
            "TeamName": "Internazionale",
            "TeamCode": "INT"
        },
        "Bologna": {
            "TeamName": "Bologna",
            "TeamCode": "BOL"
        },
        "BGN": {
            "TeamName": "Bologna",
            "TeamCode": "BGN"
        },
        "Empoli": {
            "TeamName": "Empoli",
            "TeamCode": "EMP"
        },
        "Frosinone": {
            "TeamName": "Frosinone",
            "TeamCode": "FRO"
        },
        "Parma": {
            "TeamName": "Parma",
            "TeamCode": "PAR"
        },
        "Brescia Calcio": {
            "TeamName": "Brescia Calcio",
            "TeamCode": "BRS"
        },
        "Brescia": {
            "TeamName": "Brescia Calcio",
            "TeamCode": "BRS"
        },
        "Hellas Verona": {
            "TeamName": "Hellas Verona",
            "TeamCode": "HEL"
        },
        "US Lecce": {
            "TeamName": "US Lecce",
            "TeamCode": "LEC"
        },
        "Lecce": {
            "TeamName": "US Lecce",
            "TeamCode": "LEC"
        }
    }

    LIGUE = {
        "Nimes Olympique": {
            "TeamName": "Nimes Olympique",
            "TeamCode": "NIM"
        },
        "Reims": {
            "TeamName": "Reims",
            "TeamCode": "REI"
        },
        "Olympique Marseille": {
            "TeamName": "Olympique Marseille",
            "TeamCode": "MRS"
        },
        "Marseille": {
            "TeamName": "Olympique Marseille",
            "TeamCode": "MRS"
        },
        "MAR": {
            "TeamName": "Olympique Marseille",
            "TeamCode": "MAR"
        },
        "Nantes": {
            "TeamName": "Nantes",
            "TeamCode": "NAN"
        },
        "NTE": {
            "TeamName": "Nantes",
            "TeamCode": "NTE"
        },
        "Olympique Lyonnais": {
            "TeamName": "Olympique Lyonnais",
            "TeamCode": "LYON"
        },
        "Lyon": {
            "TeamName": "Olympique Lyonnais",
            "TeamCode": "LYON"
        },
        "LYO": {
            "TeamName": "Olympique Lyonnais",
            "TeamCode": "LYO"
        },
        "Saint-Étienne": {
            "TeamName": "Saint-Étienne",
            "TeamCode": "STE"
        },
        "St. Etienne": {
            "TeamName": "Saint-Étienne",
            "TeamCode": "STE"
        },
        "ETI": {
            "TeamName": "Saint-Étienne",
            "TeamCode": "ETI"
        },
        "Toulouse": {
            "TeamName": "Toulouse",
            "TeamCode": "TOU"
        },
        "Nice": {
            "TeamName": "Nice",
            "TeamCode": "NICE"
        },
        "NIC": {
            "TeamName": "Nice",
            "TeamCode": "NIC"
        },
        "Montpellier": {
            "TeamName": "Montpellier",
            "TeamCode": "MNT"
        },
        "MTP": {
            "TeamName": "Montpellier",
            "TeamCode": "MTP"
        },
        "PSG": {
            "TeamName": "PSG",
            "TeamCode": "PSG"
        },
        "Paris Saint-Germain": {
            "TeamName": "PSG",
            "TeamCode": "PSG"
        },
        "Rennes": {
            "TeamName": "Rennes",
            "TeamCode": "REN"
        },
        "Strasbourg": {
            "TeamName": "Strasbourg",
            "TeamCode": "STRA"
        },
        "STR": {
            "TeamName": "Strasbourg",
            "TeamCode": "STR"
        },
        "Lille": {
            "TeamName": "Lille",
            "TeamCode": "LOSC"
        },
        "LIL": {
            "TeamName": "Lille",
            "TeamCode": "LIL"
        },
        "Angers SCO": {
            "TeamName": "Angers SCO",
            "TeamCode": "ANG"
        },
        "Angers": {
            "TeamName": "Angers SCO",
            "TeamCode": "ANG"
        },
        "Amiens SC": {
            "TeamName": "Amiens SC",
            "TeamCode": "AMI"
        },
        "AMN": {
            "TeamName": "Amiens SC",
            "TeamCode": "AMN"
        },
        "Caen": {
            "TeamName": "Caen",
            "TeamCode": "CAN"
        },
        "CAE": {
            "TeamName": "Caen",
            "TeamCode": "CAE"
        },
        "Guingamp": {
            "TeamName": "Guingamp",
            "TeamCode": "GUI"
        },
        "Metz": {
            "TeamName": "Metz",
            "TeamCode": "MTZ"
        },
        "MET": {
            "TeamName": "Metz",
            "TeamCode": "MET"
        },
        "Bordeaux": {
            "TeamName": "Bordeaux",
            "TeamCode": "BOR"
        },
        "BDX": {
            "TeamName": "Bordeaux",
            "TeamCode": "BDX"
        },
        "Monaco": {
            "TeamName": "Monaco",
            "TeamCode": "MON"
        },
        "Dijon": {
            "TeamName": "Dijon",
            "TeamCode": "DFCO"
        },
        "DIJ": {
            "TeamName": "Dijon",
            "TeamCode": "DIJ"
        },
        "Troyes": {
            "TeamName": "Troyes",
            "TeamCode": "TRY"
        },
        "TRO": {
            "TeamName": "Troyes",
            "TeamCode": "TRO"
        },
        "FC Metz": {
            "TeamName": "FC Metz",
            "TeamCode": "MTZ"
        },
        "Stade Brest": {
            "TeamName": "Stade Brest",
            "TeamCode": "BRS"
        }
    }

    ERED = {
        "AZ": {
            "TeamName": "AZ",
            "TeamCode": "ALK"
        },
        "Feyenoord": {
            "TeamName": "Feyenoord",
            "TeamCode": "FEY"
        },
        "Vitesse": {
            "TeamName": "Vitesse",
            "TeamCode": "VIT"
        },
        "FC Twente": {
            "TeamName": "FC Twente",
            "TeamCode": "TWN"
        },
        "Ajax": {
            "TeamName": "Ajax",
            "TeamCode": "AJAX"
        },
        "NAC Breda": {
            "TeamName": "NAC Breda",
            "TeamCode": "NAC"
        },
        "Willem II": {
            "TeamName": "Willem II",
            "TeamCode": "WIL"
        },
        "PSV": {
            "TeamName": "PSV",
            "TeamCode": "PSV"
        },
        "FC Utrecht": {
            "TeamName": "FC Utrecht",
            "TeamCode": "UTR"
        },
        "Sparta Rotterdam": {
            "TeamName": "Sparta Rotterdam",
            "TeamCode": "ROT"
        },
        "PEC Zwolle": {
            "TeamName": "PEC Zwolle",
            "TeamCode": "ZWO"
        },
        "SC Heerenveen": {
            "TeamName": "SC Heerenveen",
            "TeamCode": "HER"
        },
        "ADO Den Haag": {
            "TeamName": "ADO Den Haag",
            "TeamCode": "ADO"
        },
        "Heracles": {
            "TeamName": "Heracles",
            "TeamCode": "HER"
        },
        "Excelsior": {
            "TeamName": "Excelsior",
            "TeamCode": "EXL"
        },
        "Roda JC Kerkrade": {
            "TeamName": "Roda JC Kerkrade",
            "TeamCode": "ROD"
        },
        "FC Groningen": {
            "TeamName": "FC Groningen",
            "TeamCode": "GRN"
        },
        "VVV-Venlo": {
            "TeamName": "VVV-Venlo",
            "TeamCode": "VVV"
        },
        "Fortuna Sittard": {
            "TeamName": "Fortuna Sittard",
            "TeamCode": "FOR"
        },
        "FC EMMEN": {
            "TeamName": "FC EMMEN",
            "TeamCode": "EMM"
        },
        "FC Emmen": {
            "TeamName": "FC Emmen",
            "TeamCode": "EMM"
        },
        "Graafschap": {
            "TeamName": "Graafschap",
            "TeamCode": "GRA"
        }
    }

    MLS = {
        "FC Cincinnati": {
            "TeamName": "FC Cincinnati",
            "TeamCode": "CIN"
        },
        "Cincinnati": {
            "TeamName": "FC Cincinnati",
            "TeamCode": "CIN"
        },
        "D.C. United": {
            "TeamName": "DC United",
            "TeamCode": "DCU"
        },
        "DC United": {
            "TeamName": "DC United",
            "TeamCode": "DCU"
        },
        "DC": {
            "TeamName": "DC United",
            "TeamCode": "DC"
        },
        "Portland": {
            "TeamName": "Portland Timbers",
            "TeamCode": "POR"
        },
        "Portland Timbers": {
            "TeamName": "Portland Timbers",
            "TeamCode": "POR"
        },
        "Chicago": {
            "TeamName": "Chicago Fire",
            "TeamCode": "CHI"
        },
        "Chicago Fire": {
            "TeamName": "Chicago Fire",
            "TeamCode": "CHI"
        },
        "New York Red Bulls": {
            "TeamName": "NY Red Bulls",
            "TeamCode": "NWY"
        },
        "NY Red Bulls": {
            "TeamName": "NY Red Bulls",
            "TeamCode": "NWY"
        },
        "NY": {
            "TeamName": "NY Red Bulls",
            "TeamCode": "NWY"
        },
        "Colorado": {
            "TeamName": "Colorado Rapids",
            "TeamCode": "COL"
        },
        "Colorado Rapids": {
            "TeamName": "Colorado Rapids",
            "TeamCode": "COL"
        },
        "Real Salt Lake": {
            "TeamName": "Real Salt Lake",
            "TeamCode": "SAL"
        },
        "RSL": {
            "TeamName": "Real Salt Lake",
            "TeamCode": "SAL"
        },
        "New England": {
            "TeamName": "New England Revolution",
            "TeamCode": "NEE"
        },
        "New England Revolution": {
            "TeamName": "New England Revolution",
            "TeamCode": "NEE"
        },
        "NE": {
            "TeamName": "New England Revolution",
            "TeamCode": "NEE"
        },
        "San Jose": {
            "TeamName": "San Jose Earthquakes",
            "TeamCode": "SJE"
        },
        "San Jose Earthquakes": {
            "TeamName": "San Jose Earthquakes",
            "TeamCode": "SJE"
        },
        "SJ": {
            "TeamName": "San Jose Earthquakes",
            "TeamCode": "SJE"
        },
        "Columbus": {
            "TeamName": "Columbus Crew",
            "TeamCode": "CDC"
        },
        "Columbus Crew": {
            "TeamName": "Columbus Crew",
            "TeamCode": "CDC"
        },
        "CLB": {
            "TeamName": "Columbus Crew",
            "TeamCode": "CLB"
        },
        "Toronto": {
            "TeamName": "Toronto FC",
            "TeamCode": "TOR"
        },
        "Toronto FC": {
            "TeamName": "Toronto FC",
            "TeamCode": "TOR"
        },
        "Seattle": {
            "TeamName": "Seattle Sounders",
            "TeamCode": "SEA"
        },
        "Seattle Sounders FC": {
            "TeamName": "Seattle Sounders FC",
            "TeamCode": "SEA"
        },
        "Minnesota": {
            "TeamName": "Minnesota United FC",
            "TeamCode": "MIN"
        },
        "Minnesota United FC": {
            "TeamName": "Minnesota United FC",
            "TeamCode": "MIN"
        },
        "Minnesota United": {
            "TeamName": "Minnesota United",
            "TeamCode": "MIN"
        },
        "Philadelphia": {
            "TeamName": "Philadelphia Union",
            "TeamCode": "PHI"
        },
        "Philadelphia Union": {
            "TeamName": "Philadelphia Union",
            "TeamCode": "PHI"
        },
        "Orlando": {
            "TeamName": "Orlando City SC",
            "TeamCode": "OSC"
        },
        "Orlando City": {
            "TeamName": "Orlando City SC",
            "TeamCode": "OSC"
        },
        "Orlando City SC": {
            "TeamName": "Orlando City SC",
            "TeamCode": "OSC"
        },
        "ORL": {
            "TeamName": "Orlando City SC",
            "TeamCode": "OSC"
        },
        "Vancouver": {
            "TeamName": "Vancouver Whitecaps FC",
            "TeamCode": "VAN"
        },
        "Vancouver Whitecaps FC": {
            "TeamName": "Vancouver Whitecaps FC",
            "TeamCode": "VAN"
        },
        "NYCFC": {
            "TeamName": "New York City FC",
            "TeamCode": "NYC"
        },
        "New York City FC": {
            "TeamName": "New York City FC",
            "TeamCode": "NYC"
        },
        "Atlanta": {
            "TeamName": "Atlanta United FC",
            "TeamCode": "ATL"
        },
        "Atlanta United FC": {
            "TeamName": "Atlanta United FC",
            "TeamCode": "ATL"
        },
        "Atlanta United": {
            "TeamName": "Atlanta United",
            "TeamCode": "ATL"
        },
        "Montreal": {
            "TeamName": "Montreal Impact",
            "TeamCode": "MON"
        },
        "Montreal Impact": {
            "TeamName": "Montreal Impact",
            "TeamCode": "MON"
        },
        "MTL": {
            "TeamName": "Montreal Impact",
            "TeamCode": "MON"
        },
        "LA Galaxy": {
            "TeamName": "LA Galaxy",
            "TeamCode": "LAG"
        },
        "Los Angeles Galaxy": {
            "TeamName": "Los Angeles Galaxy",
            "TeamCode": "LAG"
        },
        "LA": {
            "TeamName": "LA Galaxy",
            "TeamCode": "LAG"
        },
        "Sporting KC": {
            "TeamName": "Sporting Kansas City",
            "TeamCode": "SKC"
        },
        "Sporting Kansas City": {
            "TeamName": "Sporting Kansas City",
            "TeamCode": "SKC"
        },
        "KC": {
            "TeamName": "Sporting Kansas City",
            "TeamCode": "KC"
        },
        "Houston": {
            "TeamName": "Houston Dynamo",
            "TeamCode": "HOU"
        },
        "Houston Dynamo": {
            "TeamName": "Houston Dynamo",
            "TeamCode": "HOU"
        },
        "FC Dallas": {
            "TeamName": "FC Dallas",
            "TeamCode": "DAL"
        },
        "Los Angeles FC": {
            "TeamName": "Los Angeles FC",
            "TeamCode": "LAN"
        },
        "Los Angeles Football Club": {
            "TeamName": "Los Angeles Football Club",
            "TeamCode": "LAN"
        },
        "LAF": {
            "TeamName": "Los Angeles FC",
            "TeamCode": "LAN"
        }
    }

    Mexico = {
        "Necaxa": {
            "TeamName": "Necaxa",
            "TeamCode": "NCX"
        },
        "Club Necaxa": {
            "TeamName": "Necaxa",
            "TeamCode": "NCX"
        },
        "Santos Laguna": {
            "TeamName": "Santos Laguna",
            "TeamCode": "SNT"
        },
        "Tigres UANL": {
            "TeamName": "Tigres UANL",
            "TeamCode": "TIG"
        },
        "UANL Tigres": {
            "TeamName": "UANL Tigres",
            "TeamCode": "TIG"
        },
        "TIG": {
            "TeamName": "Tigres UANL",
            "TeamCode": "TIG"
        },
        "Deportivo Toluca": {
            "TeamName": "Deportivo Toluca",
            "TeamCode": "TOL"
        },
        "Toluca": {
            "TeamName": "Deportivo Toluca",
            "TeamCode": "TOL"
        },
        "Puebla": {
            "TeamName": "FC Puebla",
            "TeamCode": "PUE"
        },
        "FC Puebla": {
            "TeamName": "FC Puebla",
            "TeamCode": "PUE"
        },
        "Cruz Azul": {
            "TeamName": "Cruz Azul",
            "TeamCode": "CAZ"
        },
        "CA": {
            "TeamName": "Cruz Azul",
            "TeamCode": "CAZ"
        },
        "Monterrey": {
            "TeamName": "CF Monterrey",
            "TeamCode": "MTY"
        },
        "CF Monterrey": {
            "TeamName": "CF Monterrey",
            "TeamCode": "MTY"
        },
        "Monarcas Morelia": {
            "TeamName": "Monarcas Morelia",
            "TeamCode": "MOR"
        },
        "Morelia": {
            "TeamName": "Monarcas Morelia",
            "TeamCode": "MOR"
        },
        "Club América": {
            "TeamName": "Club América",
            "TeamCode": "AME"
        },
        "America de Mexico": {
            "TeamName": "America de Mexico",
            "TeamCode": "AME"
        },
        "América de Mexico": {
            "TeamName": "America de Mexico",
            "TeamCode": "AME"
        },
        "América": {
            "TeamName": "America de Mexico",
            "TeamCode": "AME"
        },
        "Am&eacute;rica": {
            "TeamName": "America de Mexico",
            "TeamCode": "AME"
        },
        "AME": {
            "TeamName": "America de Mexico",
            "TeamCode": "AME"
        },
        "Pumas UNAM": {
            "TeamName": "Pumas UNAM",
            "TeamCode": "PUM"
        },
        "Unam Pumas": {
            "TeamName": "Pumas UNAM",
            "TeamCode": "PUM"
        },
        "UNM": {
            "TeamName": "Pumas UNAM",
            "TeamCode": "PUM"
        },
        "Pachuca": {
            "TeamName": "CF Pachuca",
            "TeamCode": "PAC"
        },
        "CF Pachuca": {
            "TeamName": "CF Pachuca",
            "TeamCode": "PAC"
        },
        "Guadalajara Chivas": {
            "TeamName": "Guadalajara Chivas",
            "TeamCode": "GDC"
        },
        "Guadalajara": {
            "TeamName": "Guadalajara Chivas",
            "TeamCode": "GDC"
        },
        "GUA": {
            "TeamName": "Guadalajara Chivas",
            "TeamCode": "GDC"
        },
        "Veracruz": {
            "TeamName": "Tiburones Rojos de Veracruz",
            "TeamCode": "VER"
        },
        "Tiburones Rojos de Veracruz": {
            "TeamName": "Tiburones Rojos de Veracruz",
            "TeamCode": "VER"
        },
        "Atlas": {
            "TeamName": "Atlas",
            "TeamCode": "ATS"
        },
        "ATS": {
            "TeamName": "Atlas",
            "TeamCode": "ATS"
        },
        "Querétaro": {
            "TeamName": "Gallos Blancos Queretaro",
            "TeamCode": "QRO"
        },
        "Queretaro": {
            "TeamName": "Gallos Blancos Queretaro",
            "TeamCode": "QRO"
        },
        "QUE": {
            "TeamName": "Gallos Blancos Queretaro",
            "TeamCode": "QRO"
        },
        "Gallos Blancos Queretaro": {
            "TeamName": "Gallos Blancos Queretaro",
            "TeamCode": "QRO"
        },
        "Tijuana": {
            "TeamName": "Club Tijuana",
            "TeamCode": "TIJ"
        },
        "Club Tijuana": {
            "TeamName": "Club Tijuana",
            "TeamCode": "TIJ"
        },
        "León": {
            "TeamName": "Leon",
            "TeamCode": "LEN"
        },
        "Leon": {
            "TeamName": "Leon",
            "TeamCode": "LEN"
        },
        "Lobos BUAP": {
            "TeamName": "Lobos B.U.A.P.",
            "TeamCode": "LBS"
        },
        "Lobos B.U.A.P.": {
            "TeamName": "Lobos B.U.A.P.",
            "TeamCode": "LBS"
        },
        "LOB": {
            "TeamName": "Lobos B.U.A.P.",
            "TeamCode": "LBS"
        },
        "Atlético San Luis": {
            "TeamName": "Atlético San Luis",
            "TeamCode": "ASL"
        },
        "Atl&eacute;tico San Luis": {
            "TeamName": "Atlético San Luis",
            "TeamCode": "ASL"
        },
        "Atletico San Luis": {
            "TeamName": "Atlético San Luis",
            "TeamCode": "ASL"
        },
        "Ju&aacute;rez": {
            "TeamName": "FC Juárez",
            "TeamCode": "FCJ"
        },
        "Juárez": {
            "TeamName": "FC Juárez",
            "TeamCode": "FCJ"
        }
    }

    Brazil = {
        "Vasco Da Gama RJ": {
            "TeamName": "Vasco Da Gama RJ",
            "TeamCode": "VAS"
        },
        "Vasco da Gama": {
            "TeamName": "Vasco da Gama",
            "TeamCode": "VAS"
        },
        "Cruzeiro MG": {
            "TeamName": "Cruzeiro MG",
            "TeamCode": "CRU"
        },
        "Cruzeiro": {
            "TeamName": "Cruzeiro",
            "TeamCode": "CRU"
        },
        "Internacional RS": {
            "TeamName": "Internacional RS",
            "TeamCode": "INT"
        },
        "America Mineiro MG": {
            "TeamName": "America Mineiro MG",
            "TeamCode": "AMG"
        },
        "Atletico Mineiro MG": {
            "TeamName": "Atletico Mineiro MG",
            "TeamCode": "CAM"
        },
        "Atlético Mineiro": {
            "TeamName": "Atlético Mineiro",
            "TeamCode": "CAM"
        },
        "Corinthians SP": {
            "TeamName": "Corinthians SP",
            "TeamCode": "COR"
        },
        "Corinthians": {
            "TeamName": "Corinthians",
            "TeamCode": "COR"
        },
        "Vitoria BA": {
            "TeamName": "Vitoria BA",
            "TeamCode": "VIT"
        },
        "Vitória": {
            "TeamName": "Vitória",
            "TeamCode": "VIT"
        },
        "Botafogo RJ": {
            "TeamName": "Botafogo RJ",
            "TeamCode": "BOT"
        },
        "Botafogo": {
            "TeamName": "Botafogo",
            "TeamCode": "BOT"
        },
        "Atletico Paranaense": {
            "TeamName": "Atletico Paranaense",
            "TeamCode": "CAP"
        },
        "Atlético - PR": {
            "TeamName": "Atlético - PR",
            "TeamCode": "APR"
        },
        "Palmeiras SP": {
            "TeamName": "Palmeiras SP",
            "TeamCode": "PAL"
        },
        "Palmeiras": {
            "TeamName": "Palmeiras",
            "TeamCode": "PAL"
        },
        "Santos FC SP": {
            "TeamName": "Santos FC SP",
            "TeamCode": "SAN"
        },
        "Santos": {
            "TeamName": "Santos",
            "TeamCode": "SAN"
        },
        "Flamengo RJ": {
            "TeamName": "Flamengo RJ",
            "TeamCode": "FLA"
        },
        "Flamengo": {
            "TeamName": "Flamengo",
            "TeamCode": "FLA"
        },
        "EC Bahia BA": {
            "TeamName": "EC Bahia BA",
            "TeamCode": "BAH"
        },
        "Parana Clube PR": {
            "TeamName": "Parana Clube PR",
            "TeamCode": "PAR"
        },
        "Fluminense RJ": {
            "TeamName": "Fluminense RJ",
            "TeamCode": "FLU"
        },
        "Fluminense": {
            "TeamName": "Fluminense",
            "TeamCode": "FLU"
        },
        "Ceara CE": {
            "TeamName": "Ceara CE",
            "TeamCode": "CEA"
        },
        "Sao Paulo SP": {
            "TeamName": "Sao Paulo SP",
            "TeamCode": "SAO"
        },
        "São Paulo": {
            "TeamName": "São Paulo",
            "TeamCode": "SAO"
        },
        "Gremio RS": {
            "TeamName": "Gremio RS",
            "TeamCode": "GRE"
        },
        "Grêmio": {
            "TeamName": "Grêmio",
            "TeamCode": "GRE"
        },
        "Sport Recife PE": {
            "TeamName": "Sport Recife PE",
            "TeamCode": "SPO"
        },
        "Sport Recife": {
            "TeamName": "Sport Recife",
            "TeamCode": "SPO"
        },
        "Chapecoense SC": {
            "TeamName": "Chapecoense SC",
            "TeamCode": "CHA"
        },
        "Chapecoense": {
            "TeamName": "Chapecoense",
            "TeamCode": "CHA"
        }
    }

    Argent = {
        "Atletico Lanus": {
            "TeamName": "Atletico Lanus",
            "TeamCode": "LAN"
        },
        "Atlético": {
            "TeamName": "Atlético",
            "TeamCode": "LAN"
        },
        "Lanús": {
            "TeamName": "Lanús",
            "TeamCode": "LAN"
        },
        "CA San Lorenzo": {
            "TeamName": "CA San Lorenzo",
            "TeamCode": "SLOR"
        },
        "San Lorenzo": {
            "TeamName": "San Lorenzo",
            "TeamCode": "SLOR"
        },
        "Racing Club": {
            "TeamName": "Racing Club",
            "TeamCode": "RAC"
        },
        "Racing": {
            "TeamName": "Racing",
            "TeamCode": "RAC"
        },
        "CA Rosario Central": {
            "TeamName": "CA Rosario Central",
            "TeamCode": "ROS"
        },
        "Rosario Central": {
            "TeamName": "Rosario Central",
            "TeamCode": "ROS"
        },
        "Velez Sarsfield": {
            "TeamName": "Velez Sarsfield",
            "TeamCode": "VEL"
        },
        "Vélez Sarsfield": {
            "TeamName": "Vélez Sarsfield",
            "TeamCode": "VEL"
        },
        "CA River Plate": {
            "TeamName": "CA River Plate",
            "TeamCode": "CARP"
        },
        "River Plate": {
            "TeamName": "River Plate",
            "TeamCode": "CARP"
        },
        "Gimnasia y Esgrima": {
            "TeamName": "Gimnasia y Esgrima",
            "TeamCode": "GLP"
        },
        "Gimnasia": {
            "TeamName": "Gimnasia",
            "TeamCode": "GLP"
        },
        "CA Chacarita Juniors": {
            "TeamName": "CA Chacarita Juniors",
            "TeamCode": "CHA"
        },
        "Chacarita": {
            "TeamName": "Chacarita",
            "TeamCode": "CHA"
        },
        "Argentinos Jrs": {
            "TeamName": "Argentinos Jrs",
            "TeamCode": "ARGJ"
        },
        "Argentinos Juniors": {
            "TeamName": "Argentinos Juniors",
            "TeamCode": "ARGJ"
        },
        "Boca Juniors": {
            "TeamName": "Boca Juniors",
            "TeamCode": "CABJ"
        },
        "CA Independiente": {
            "TeamName": "CA Independiente",
            "TeamCode": "IND"
        },
        "Independiente": {
            "TeamName": "Independiente",
            "TeamCode": "IND"
        },
        "Union de Santa Fe": {
            "TeamName": "Union de Santa Fe",
            "TeamCode": "USF"
        },
        "Unión": {
            "TeamName": "Unión",
            "TeamCode": "USF"
        },
        "Colon de Santa Fe": {
            "TeamName": "Colon de Santa Fe",
            "TeamCode": "COL"
        },
        "Colón": {
            "TeamName": "Colón",
            "TeamCode": "COL"
        },
        "CA Talleres": {
            "TeamName": "CA Talleres",
            "TeamCode": "TDC"
        },
        "Talleres": {
            "TeamName": "Talleres",
            "TeamCode": "TDC"
        },
        "Newell's Old Boys": {
            "TeamName": "Newell's Old Boys",
            "TeamCode": "NOB"
        },
        "Estudiantes de La Plata": {
            "TeamName": "Estudiantes de La Plata",
            "TeamCode": "EST"
        },
        "Estudiantes": {
            "TeamName": "Estudiantes",
            "TeamCode": "EST"
        },
        "CA Belgrano": {
            "TeamName": "CA Belgrano",
            "TeamCode": "BEL"
        },
        "Belgrano": {
            "TeamName": "Belgrano",
            "TeamCode": "BEL"
        },
        "CA Banfield": {
            "TeamName": "CA Banfield",
            "TeamCode": "CAP"
        },
        "Banfield": {
            "TeamName": "Banfield",
            "TeamCode": "CAP"
        },
        "Arsenal de Sarandi": {
            "TeamName": "Arsenal de Sarandi",
            "TeamCode": "ARSE"
        },
        "Arsenal": {
            "TeamName": "Arsenal",
            "TeamCode": "ARSE"
        },
        "Club Olimpo": {
            "TeamName": "Club Olimpo",
            "TeamCode": "OBB"
        },
        "Olimpo": {
            "TeamName": "Olimpo",
            "TeamCode": "OBB"
        },
        "CA Huracan": {
            "TeamName": "CA Huracan",
            "TeamCode": "HUR"
        },
        "Huracán": {
            "TeamName": "Huracán",
            "TeamCode": "HUR"
        },
        "Godoy Cruz A.T.": {
            "TeamName": "Godoy Cruz A.T.",
            "TeamCode": "GCM"
        },
        "Godoy Cruz": {
            "TeamName": "Godoy Cruz",
            "TeamCode": "GCM"
        },
        "CA Tigre": {
            "TeamName": "CA Tigre",
            "TeamCode": "TIG"
        },
        "Tigre": {
            "TeamName": "Tigre",
            "TeamCode": "TIG"
        },
        "San Martin de San Juan": {
            "TeamName": "San Martin de San Juan",
            "TeamCode": "SMSJ"
        },
        "Atletico Tucuman": {
            "TeamName": "Atletico Tucuman",
            "TeamCode": "CAT"
        },
        "Atlético Tucumán": {
            "TeamName": "Atlético Tucumán",
            "TeamCode": "CAT"
        },
        "CA Temperley": {
            "TeamName": "CA Temperley",
            "TeamCode": "TEMP"
        },
        "Temperley": {
            "TeamName": "Temperley",
            "TeamCode": "TEMP"
        },
        "Defensa y Justicia": {
            "TeamName": "Defensa y Justicia",
            "TeamCode": "DYJ"
        },
        "CA Patronato Parana": {
            "TeamName": "CA Patronato Parana",
            "TeamCode": "PAP"
        },
        "Patronato": {
            "TeamName": "Patronato",
            "TeamCode": "PAP"
        }
    }

    PRIME = {
        "Sporting": {
            "TeamName": "Sporting CP",
            "TeamCode": "SCP"
        },
        "Belenenses": {
            "TeamName": "Belenenses",
            "TeamCode": "BELE"
        },
        "Benfica": {
            "TeamName": "Benfica",
            "TeamCode": "BEN"
        },
        "Porto": {
            "TeamName": "Porto",
            "TeamCode": "POR"
        },
        "Vitória": {
            "TeamName": "Vitória FC",
            "TeamCode": "GUI"
        },
        "Braga": {
            "TeamName": "Sporting Braga",
            "TeamCode": "BRAGA"
        },
        "Boavista": {
            "TeamName": "Boavista",
            "TeamCode": "BOA"
        },
        "Chaves": {
            "TeamName": "Chaves",
            "TeamCode": "GDC"
        },
        "Moreirense": {
            "TeamName": "Moreirense",
            "TeamCode": "MORE"
        },
        "Pacos Ferreira": {
            "TeamName": "Pacos Ferreira",
            "TeamCode": "PFC"
        },
        "Paços de Ferreira": {
            "TeamName": "Paços de Ferreira",
            "TeamCode": "PFC"
        },
        "Estoril": {
            "TeamName": "Estoril",
            "TeamCode": "EST"
        },
        "Portimonense": {
            "TeamName": "Portimonense",
            "TeamCode": "BET"
        },
        "Tondela": {
            "TeamName": "Tondela",
            "TeamCode": "CDT"
        },
        "Victoria SC": {
            "TeamName": "Victoria SC",
            "TeamCode": "SET"
        },
        "Maritimo": {
            "TeamName": "Maritimo",
            "TeamCode": "MARI"
        },
        "Marítimo": {
            "TeamName": "Marítimo",
            "TeamCode": "MARI"
        },
        "Rio Ave": {
            "TeamName": "Rio Ave",
            "TeamCode": "RIO"
        },
        "Feirense": {
            "TeamName": "Feirense",
            "TeamCode": "FEI"
        },
        "Desportivo Aves": {
            "TeamName": "Desportivo Aves",
            "TeamCode": "DAV"
        }
    }

    Turkey = {
        "Galatasaray": {
            "TeamName": "Galatasaray",
            "TeamCode": "GAL"
        },
        "Başakşehir": {
            "TeamName": "Başakşehir",
            "TeamCode": "IBUY"
        },
        "Antalyaspor": {
            "TeamName": "Antalyaspor",
            "TeamCode": "ANT"
        },
        "Fenerbahçe": {
            "TeamName": "Fenerbahçe",
            "TeamCode": "FEN"
        },
        "Gençlerbirliği": {
            "TeamName": "Gençlerbirliği",
            "TeamCode": "GEN"
        },
        "Alanyaspor": {
            "TeamName": "Alanyaspor",
            "TeamCode": "ALA"
        },
        "Sivasspor": {
            "TeamName": "Sivasspor",
            "TeamCode": "SIV"
        },
        "Beşiktaş": {
            "TeamName": "Beşiktaş",
            "TeamCode": "BES"
        },
        "Kayserispor": {
            "TeamName": "Kayserispor",
            "TeamCode": "KAY"
        },
        "Trabzonspor": {
            "TeamName": "Trabzonspor",
            "TeamCode": "TRA"
        },
        "Osmanlıspor": {
            "TeamName": "Osmanlıspor",
            "TeamCode": "OSM"
        },
        "Kasımpaşa": {
            "TeamName": "Kasımpaşa",
            "TeamCode": "KAS"
        },
        "Bursaspor": {
            "TeamName": "Bursaspor",
            "TeamCode": "BUR"
        },
        "Akhisar Belediye": {
            "TeamName": "Akhisar Belediyespor",
            "TeamCode": "AKB"
        },
        "Karabükspor": {
            "TeamName": "Karabükspor",
            "TeamCode": "KAR"
        },
        "Göztepe": {
            "TeamName": "Göztepe",
            "TeamCode": "GOZ"
        },
        "Yeni Malatyaspor": {
            "TeamName": "Yeni Malatyaspor",
            "TeamCode": "MAL"
        },
        "Konyaspor": {
            "TeamName": "Konyaspor",
            "TeamCode": "KNY"
        }
    }

    PREMIER = {
        "Celtic": {
            "TeamName": "Celtic",
            "TeamCode": "CEL"
        },
        "Rangers": {
            "TeamName": "Rangers",
            "TeamCode": "RANG"
        },
        "Hibernian": {
            "TeamName": "Hibernian",
            "TeamCode": "HIBS"
        },
        "Kilmarnock": {
            "TeamName": "Kilmarnock",
            "TeamCode": "KILM"
        },
        "Ross County": {
            "TeamName": "Ross County",
            "TeamCode": "ROSS"
        },
        "Aberdeen": {
            "TeamName": "Aberdeen",
            "TeamCode": "ABER"
        },
        "Dundee": {
            "TeamName": "Dundee",
            "TeamCode": "DUN"
        },
        "Motherwell": {
            "TeamName": "Motherwell",
            "TeamCode": "MOT"
        },
        "Hearts": {
            "TeamName": "Hearts",
            "TeamCode": "HOM"
        },
        "Hamilton Accies": {
            "TeamName": "Hamilton Academical",
            "TeamCode": "HAM"
        },
        "Partick Thistle": {
            "TeamName": "Partick Thistle",
            "TeamCode": "PAR"
        },
        "St Johnstone": {
            "TeamName": "St. Johnstone",
            "TeamCode": "STJO"
        }
    }

    NCAAFB = {
        "aab": {
            "TeamName": "Air Force",
            "TeamCode": "AF"
        },
        "aac": {
            "TeamName": "Akron",
            "TeamCode": "AKR"
        },
        "aad": {
            "TeamName": "Alabama",
            "TeamCode": "BAMA"
        },
        "aad2": {
            "TeamName": "Alabama Crimson Tide",
            "TeamCode": "BAMA"
        },
        "aag": {
            "TeamName": "Albany",
            "TeamCode": "ALB"
        },
        "aah": {
            "TeamName": "Alcorn State",
            "TeamCode": "ALCST"
        },
        "aak": {
            "TeamName": "Appalachian State",
            "TeamCode": "APP"
        },
        "aal": {
            "TeamName": "Arizona",
            "TeamCode": "ARI"
        },
        "aal2": {
            "TeamName": "Arizona Wildcats",
            "TeamCode": "ARI"
        },
        "aam": {
            "TeamName": "Arizona State",
            "TeamCode": "ASU"
        },
        "aam2": {
            "TeamName": "Arizona State Sun Devils",
            "TeamCode": "ASU"
        },
        "aan": {
            "TeamName": "Arkansas",
            "TeamCode": "ARK"
        },
        "aan2": {
            "TeamName": "Arkansas Razorbacks",
            "TeamCode": "ARK"
        },
        "aap": {
            "TeamName": "Arkansas State",
            "TeamCode": "ARKS"
        },
        "aaq": {
            "TeamName": "Army",
            "TeamCode": "ARM"
        },
        "aaq2": {
            "TeamName": "Army Black Knights",
            "TeamCode": "ARM"
        },
        "aar": {
            "TeamName": "Auburn",
            "TeamCode": "AUB"
        },
        "aar2": {
            "TeamName": "Auburn Tigers",
            "TeamCode": "AUB"
        },
        "aaz": {
            "TeamName": "UAB",
            "TeamCode": "UAB"
        },
        "bba": {
            "TeamName": "Ball State",
            "TeamCode": "BALL"
        },
        "bbb": {
            "TeamName": "Baylor",
            "TeamCode": "BAY"
        },
        "bbb2": {
            "TeamName": "Baylor Bears",
            "TeamCode": "BAY"
        },
        "bbe": {
            "TeamName": "Boise State",
            "TeamCode": "BOISE"
        },
        "bbe2": {
            "TeamName": "Boise State Broncos",
            "TeamCode": "BOISE"
        },
        "bbf": {
            "TeamName": "Boston College",
            "TeamCode": "BC"
        },
        "bbf2": {
            "TeamName": "College Lacrosse",
            "TeamCode": "BC"
        },
        "bbf3": {
            "TeamName": "Boston College Eagles",
            "TeamCode": "BC"
        },
        "bbh": {
            "TeamName": "Bowling Green",
            "TeamCode": "BGN"
        },
        "bbi": {
            "TeamName": "BYU",
            "TeamCode": "BYU"
        },
        "bbi2": {
            "TeamName": "BYU Cougars",
            "TeamCode": "BYU"
        },
        "bbi3": {
            "TeamName": "Brigham Young Cougars",
            "TeamCode": "BYU"
        },
        "bbj": {
            "TeamName": "Brown",
            "TeamCode": "BRN"
        },
        "bbp": {
            "TeamName": "Buffalo",
            "TeamCode": "BUF"
        },
        "bbr": {
            "TeamName": "Butler",
            "TeamCode": "BUT"
        },
        "bvx": {
            "TeamName": "Bryant",
            "TeamCode": "BRY"
        },
        "caa": {
            "TeamName": "Cal Poly",
            "TeamCode": "CPS"
        },
        "cam": {
            "TeamName": "Campbell",
            "TeamCode": "CAM"
        },
        "cbi": {
            "TeamName": "Coastal Carolina",
            "TeamCode": "CC"
        },
        "ccb": {
            "TeamName": "UC Davis",
            "TeamCode": "UCD"
        },
        "ccd": {
            "TeamName": "California",
            "TeamCode": "CAL"
        },
        "ccd2": {
            "TeamName": "California Golden Bears",
            "TeamCode": "CAL"
        },
        "ccf": {
            "TeamName": "UCF",
            "TeamCode": "UCF"
        },
        "ccg": {
            "TeamName": "Central Michigan",
            "TeamCode": "CMC"
        },
        "ucf": {
            "TeamName": "Central Florida Golden Knights",
            "TeamCode": "UCF"
        },
        "ccj": {
            "TeamName": "Cincinnati",
            "TeamCode": "CIN"
        },
        "ccj2": {
            "TeamName": "Cincinnati Bearcats",
            "TeamCode": "CIN"
        },
        "cck": {
            "TeamName": "Citadel",
            "TeamCode": "CIT"
        },
        "ccl": {
            "TeamName": "Clemson",
            "TeamCode": "CLE"
        },
        "ccl2": {
            "TeamName": "Clemson Tigers",
            "TeamCode": "CLE"
        },
        "ccn": {
            "TeamName": "Colorado",
            "TeamCode": "COL"
        },
        "ccn": {
            "TeamName": "Colorado Buffaloes",
            "TeamCode": "COL"
        },
        "cco": {
            "TeamName": "Colorado State",
            "TeamCode": "CSU"
        },
        "ccp": {
            "TeamName": "Columbia",
            "TeamCode": "CMB"
        },
        "ccq": {
            "TeamName": "Connecticut",
            "TeamCode": "UCONN"
        },
        "ccr": {
            "TeamName": "Cornell",
            "TeamCode": "COR"
        },
        "ccz": {
            "TeamName": "Charleston Southern",
            "TeamCode": "CCH"
        },
        "dda": {
            "TeamName": "Dartmouth",
            "TeamCode": "DRT"
        },
        "ddb": {
            "TeamName": "Davidson",
            "TeamCode": "DAV"
        },
        "ddc": {
            "TeamName": "Delaware",
            "TeamCode": "DEL"
        },
        "dde": {
            "TeamName": "Drake",
            "TeamCode": "DRA"
        },
        "ddf": {
            "TeamName": "Duke",
            "TeamCode": "DUK"
        },
        "ddf2": {
            "TeamName": "Duke Blue Devils",
            "TeamCode": "DUK"
        },
        "ddi": {
            "TeamName": "Duquesne",
            "TeamCode": "DUQ"
        },
        "ddj": {
            "TeamName": "Dayton",
            "TeamCode": "DAY"
        },
        "eea": {
            "TeamName": "East Carolina",
            "TeamCode": "ECU"
        },
        "eee": {
            "TeamName": "Eastern Kentucky",
            "TeamCode": "EKY"
        },
        "eef": {
            "TeamName": "Eastern Michigan",
            "TeamCode": "EMC"
        },
        "eeg": {
            "TeamName": "Eastern Washington",
            "TeamCode": "EW"
        },
        "eeo": {
            "TeamName": "Elon",
            "TeamCode": "ELO"
        },
        "ffa": {
            "TeamName": "Florida",
            "TeamCode": "FLA"
        },
        "ffa2": {
            "TeamName": "Florida Gators",
            "TeamCode": "FLA"
        },
        "ffa3": {
            "TeamName": "Florida International Golden Panthers",
            "TeamCode": "FLA"
        },
        "ffc": {
            "TeamName": "Florida State",
            "TeamCode": "FSU"
        },
        "ffc2": {
            "TeamName": "Florida State Seminoles",
            "TeamCode": "FSU"
        },
        "ffe": {
            "TeamName": "Fresno State",
            "TeamCode": "FRE"
        },
        "ffr": {
            "TeamName": "Florida Atlantic",
            "TeamCode": "FAU"
        },
        "fli": {
            "TeamName": "Florida International",
            "TeamCode": "FIU"
        },
        "gag": {
            "TeamName": "Georgia State",
            "TeamCode": "GST"
        },
        "ggb": {
            "TeamName": "Georgia",
            "TeamCode": "UGA"
        },
        "ggb2": {
            "TeamName": "Georgia Bulldogs",
            "TeamCode": "UGA"
        },
        "ggc": {
            "TeamName": "Georgia Tech",
            "TeamCode": "UGA"
        },
        "ggc2": {
            "TeamName": "Georgia Tech Yellow Jackets",
            "TeamCode": "UGA"
        },
        "ggf": {
            "TeamName": "Gardner-Webb",
            "TeamCode": "GWB"
        },
        "ggh": {
            "TeamName": "Georgia Southern",
            "TeamCode": "GSO"
        },
        "hha": {
            "TeamName": "Hampton",
            "TeamCode": "HAMP"
        },
        "hhb": {
            "TeamName": "Harvard",
            "TeamCode": "HAR"
        },
        "hhc": {
            "TeamName": "Hawaii",
            "TeamCode": "HAW"
        },
        "hhe": {
            "TeamName": "Houston",
            "TeamCode": "HOU"
        },
        "hhe2": {
            "TeamName": "Houston Cougars",
            "TeamCode": "HOU"
        },
        "hhf": {
            "TeamName": "Howard",
            "TeamCode": "HOW"
        },
        "iia": {
            "TeamName": "Idaho",
            "TeamCode": "IDA"
        },
        "iib": {
            "TeamName": "Idaho State",
            "TeamCode": "IDS"
        },
        "iic": {
            "TeamName": "Illinois",
            "TeamCode": "ILL"
        },
        "iic2": {
            "TeamName": "Illinois Fighting Illini",
            "TeamCode": "ILL"
        },
        "iie": {
            "TeamName": "Indiana",
            "TeamCode": "IU"
        },
        "iig": {
            "TeamName": "Iowa",
            "TeamCode": "IOW"
        },
        "iig2": {
            "TeamName": "Iowa Hawkeyes",
            "TeamCode": "IOW"
        },
        "iih": {
            "TeamName": "Iowa State",
            "TeamCode": "ISU"
        },
        "iih2": {
            "TeamName": "Iowa St.Cyclones",
            "TeamCode": "ISU"
        },
        "incarnate_word": {
            "TeamName": "Incarnate Word",
            "TeamCode": "IW"
        },
        "jjb": {
            "TeamName": "James Madison",
            "TeamCode": "JM"
        },
        "jjc": {
            "TeamName": "Jacksonville State",
            "TeamCode": "JVS"
        },
        "jjg": {
            "TeamName": "Jacksonville",
            "TeamCode": "JAC"
        },
        "kka": {
            "TeamName": "Kansas",
            "TeamCode": "KAN"
        },
        "kka2": {
            "TeamName": "Kansas Jayhawks",
            "TeamCode": "KAN"
        },
        "kkb": {
            "TeamName": "Kansas State",
            "TeamCode": "KST"
        },
        "kkb2": {
            "TeamName": "Kansas State Wildcats",
            "TeamCode": "KST"
        },
        "kkc": {
            "TeamName": "Kent State",
            "TeamCode": "KNT"
        },
        "kkc2": {
            "TeamName": "KKent Golden Flashes",
            "TeamCode": "KNT"
        },
        "kkd": {
            "TeamName": "Kentucky",
            "TeamCode": "KEN"
        },
        "kkd2": {
            "TeamName": "Kentucky Wildcats",
            "TeamCode": "KEN"
        },
        "lab": {
            "TeamName": "Lamar",
            "TeamCode": "LAM"
        },
        "lla": {
            "TeamName": "Lafayette",
            "TeamCode": "LAF"
        },
        "lle": {
            "TeamName": "Liberty Flames",
            "TeamCode": "LIB"
        },
        "llg": {
            "TeamName": "Louisiana Tech",
            "TeamCode": "LT"
        },
        "llg2": {
            "TeamName": "Louisiana - Lafayette Ragin' Cajuns",
            "TeamCode": "LT"
        },
        "llh": {
            "TeamName": "Louisville",
            "TeamCode": "LOU"
        },
        "llh2": {
            "TeamName": "Louisville Cardinals",
            "TeamCode": "LOU"
        },
        "lli": {
            "TeamName": "LSU",
            "TeamCode": "LSU"
        },
        "lli2": {
            "TeamName": "LSU Tigers",
            "TeamCode": "LSU"
        },
        "lli3": {
            "TeamName": "Lsu Tigers",
            "TeamCode": "LSU"
        },
        "mad": {
            "TeamName": "Marist",
            "TeamCode": "MST"
        },
        "mae": {
            "TeamName": "Monmouth",
            "TeamCode": "MNM"
        },
        "mma": {
            "TeamName": "Maine",
            "TeamCode": "UMAINE"
        },
        "mmc": {
            "TeamName": "Marshall",
            "TeamCode": "MSH"
        },
        "mmc2": {
            "TeamName": "Marshall Thundering Herd",
            "TeamCode": "MSH"
        },
        "mmd": {
            "TeamName": "Maryland",
            "TeamCode": "MAR"
        },
        "mmd2": {
            "TeamName": "Maryland Terrapins",
            "TeamCode": "MAR"
        },
        "mme": {
            "TeamName": "Massachusetts",
            "TeamCode": "UMASS"
        },
        "mmg": {
            "TeamName": "Memphis",
            "TeamCode": "MEM"
        },
        "mmg2": {
            "TeamName": "Memphis Tigers",
            "TeamCode": "MEM"
        },
        "mmi": {
            "TeamName": "Miami (FL)",
            "TeamCode": "MFL"
        },
        "mmi2": {
            "TeamName": "Miami - Florida Hurricanes",
            "TeamCode": "MFL"
        },
        "mmi3": {
            "TeamName": "Miami (Fl) Hurricanes",
            "TeamCode": "MFL"
        },
        "mmj": {
            "TeamName": "Miami (OH)",
            "TeamCode": "MOH"
        },
        "mmj2": {
            "TeamName": "Miami Hurricanes",
            "TeamCode": "MOH"
        },
        "mmj3": {
            "TeamName": "Miami - Florida Hurricanes",
            "TeamCode": "MOH"
        },
        "mmk": {
            "TeamName": "Michigan",
            "TeamCode": "MICH"
        },
        "mmk2": {
            "TeamName": "Michigan Wolverines",
            "TeamCode": "MICH"
        },
        "mml": {
            "TeamName": "Mich. St.",
            "TeamCode": "MSU"
        },
        "mml3": {
            "TeamName": "Michigan State",
            "TeamCode": "MSU"
        },
        "mml2": {
            "TeamName": "Michigan State Spartans",
            "TeamCode": "MSU"
        },
        "mmm": {
            "TeamName": "Middle Tennessee",
            "TeamCode": "MTS"
        },
        "mmm2": {
            "TeamName": "Middle Tenn.St Blue Raiders",
            "TeamCode": "MTS"
        },
        "mmn": {
            "TeamName": "Minnesota",
            "TeamCode": "MIN"
        },
        "mmn2": {
            "TeamName": "Minnesota Golden Gophers",
            "TeamCode": "MIN"
        },
        "mmo": {
            "TeamName": "Ole Miss",
            "TeamCode": "MIS"
        },
        "mmo2": {
            "TeamName": "Ole Miss Rebels",
            "TeamCode": "MIS"
        },
        "mmq": {
            "TeamName": "Mississippi State",
            "TeamCode": "MSST"
        },
        "mmq2": {
            "TeamName": "Mississippi State Bulldogs",
            "TeamCode": "MSST"
        },
        "mmq3": {
            "TeamName": "Mississippi Rebels",
            "TeamCode": "MSST"
        },
        "mmr": {
            "TeamName": "Mississippi Valley State",
            "TeamCode": "MVS"
        },
        "mms": {
            "TeamName": "Missouri",
            "TeamCode": "MIZ"
        },
        "mms2": {
            "TeamName": "Missouri Tigers",
            "TeamCode": "MIZ"
        },
        "mmu": {
            "TeamName": "Montana",
            "TeamCode": "MONT"
        },
        "mmv": {
            "TeamName": "Montana State",
            "TeamCode": "MOS"
        },
        "nad": {
            "TeamName": "Charlotte",
            "TeamCode": "CHA"
        },
        "nna": {
            "TeamName": "Navy",
            "TeamCode": "NAV"
        },
        "nnb": {
            "TeamName": "Louisiana-Monroe",
            "TeamCode": "ULM"
        },
        "nnd": {
            "TeamName": "Nebraska",
            "TeamCode": "NEB"
        },
        "nnd2": {
            "TeamName": "Nebraska Cornhuskers",
            "TeamCode": "NEB"
        },
        "nne": {
            "TeamName": "UNLV",
            "TeamCode": "UNLV"
        },
        "nnf": {
            "TeamName": "Nevada",
            "TeamCode": "NEV"
        },
        "nnf2": {
            "TeamName": "Nevada Wolf Pack",
            "TeamCode": "NEV"
        },
        "nng": {
            "TeamName": "New Hampshire",
            "TeamCode": "NH"
        },
        "nnh": {
            "TeamName": "New Mexico",
            "TeamCode": "NM"
        },
        "nni": {
            "TeamName": "New Mexico State",
            "TeamCode": "NMS"
        },
        "nnl": {
            "TeamName": "North Carolina",
            "TeamCode": "NC"
        },
        "nnl2": {
            "TeamName": "North Carolina Tar Heels",
            "TeamCode": "NC"
        },
        "nnm": {
            "TeamName": "North Carolina A&T",
            "TeamCode": "NAT"
        },
        "nnn": {
            "TeamName": "North Carolina State",
            "TeamCode": "NCST"
        },
        "nno": {
            "TeamName": "North Dakota",
            "TeamCode": "UND"
        },
        "nnp": {
            "TeamName": "North Texas",
            "TeamCode": "NTX"
        },
        "nnr": {
            "TeamName": "Northern Arizona",
            "TeamCode": "NAZ"
        },
        "nns": {
            "TeamName": "Northern Illinois",
            "TeamCode": "NIL"
        },
        "nnv": {
            "TeamName": "Northwestern",
            "TeamCode": "NW"
        },
        "nnv2": {
            "TeamName": "Northwestern Wildcats",
            "TeamCode": "NW"
        },
        "nnx": {
            "TeamName": "Notre Dame",
            "TeamCode": "ND"
        },
        "nnx2": {
            "TeamName": "Notre Dame Fighting Irish",
            "TeamCode": "ND"
        },
        "nnz": {
            "TeamName": "Northern Colorado",
            "TeamCode": "NOCO"
        },
        "oah": {
            "TeamName": "Old Dominion",
            "TeamCode": "ODU"
        },
        "ooa": {
            "TeamName": "Ohio",
            "TeamCode": "OHI"
        },
        "oob": {
            "TeamName": "Ohio State",
            "TeamCode": "OSU"
        },
        "oob2": {
            "TeamName": "Ohio State Buckeyes",
            "TeamCode": "OSU"
        },
        "ooc": {
            "TeamName": "Oklahoma",
            "TeamCode": "OKL"
        },
        "ooc2": {
            "TeamName": "Oklahoma Sooners",
            "TeamCode": "OKL"
        },
        "ood": {
            "TeamName": "Oklahoma State",
            "TeamCode": "OKS"
        },
        "ood2": {
            "TeamName": "Oklahoma State Cowboys",
            "TeamCode": "OKS"
        },
        "ooe": {
            "TeamName": "Oregon",
            "TeamCode": "ORE"
        },
        "ooe2": {
            "TeamName": "Oregon Ducks",
            "TeamCode": "ORE"
        },
        "oof": {
            "TeamName": "Oregon State",
            "TeamCode": "ORS"
        },
        "oof2": {
            "TeamName": "Oregon State Beavers",
            "TeamCode": "ORS"
        },
        "ppb": {
            "TeamName": "Penn State",
            "TeamCode": "PSU"
        },
        "ppb2": {
            "TeamName": "Penn State Nittany Llions",
            "TeamCode": "PSU"
        },
        "ppb3": {
            "TeamName": "Penn State Nittany Lions",
            "TeamCode": "PSU"
        },
        "ppd": {
            "TeamName": "Pittsburgh",
            "TeamCode": "PIT"
        },
        "ppd2": {
            "TeamName": "Pittsburgh Panthers",
            "TeamCode": "PIT"
        },
        "ppe": {
            "TeamName": "Portland State",
            "TeamCode": "PRST"
        },
        "ppg": {
            "TeamName": "Presbyterian",
            "TeamCode": "PRES"
        },
        "pph": {
            "TeamName": "Princeton",
            "TeamCode": "PRI"
        },
        "ppj": {
            "TeamName": "Purdue",
            "TeamCode": "PUR"
        },
        "ppj2": {
            "TeamName": "Purdue Boilermakers",
            "TeamCode": "PUR"
        },
        "rra": {
            "TeamName": "Rhode Island",
            "TeamCode": "RIL"
        },
        "rrb": {
            "TeamName": "Rice",
            "TeamCode": "RICE"
        },
        "rrc": {
            "TeamName": "Richmond",
            "TeamCode": "RCH"
        },
        "rrd": {
            "TeamName": "Rutgers",
            "TeamCode": "RUT"
        },
        "rrd2": {
            "TeamName": "Rutgers Scarlet Knights",
            "TeamCode": "RUT"
        },
        "sal": {
            "TeamName": "South Alabama",
            "TeamCode": "BAMA"
        },
        "sbc": {
            "TeamName": "San Diego",
            "TeamCode": "SDG"
        },
        "sbf": {
            "TeamName": "Stony Brook",
            "TeamCode": "SBK"
        },
        "sbn": {
            "TeamName": "South Florida",
            "TeamCode": "USF"
        },
        "ses": {
            "TeamName": "Sacramento State",
            "TeamCode": "CSUS"
        },
        "ssb": {
            "TeamName": "San Diego State",
            "TeamCode": "SDSU"
        },
        "ssc": {
            "TeamName": "San Jose State",
            "TeamCode": "SJS"
        },
        "sse": {
            "TeamName": "Southeastern Louisiana",
            "TeamCode": "SEL"
        },
        "ssf": {
            "TeamName": "Southeast Missouri State",
            "TeamCode": "SEM"
        },
        "ssh": {
            "TeamName": "SMU",
            "TeamCode": "SMU"
        },
        "ssi": {
            "TeamName": "South Carolina",
            "TeamCode": "SC"
        },
        "ssi2": {
            "TeamName": "South Carolina Gamecocks",
            "TeamCode": "SC"
        },
        "sso": {
            "TeamName": "Southern Miss",
            "TeamCode": "USM"
        },
        "sso2": {
            "TeamName": "Southern Miss Golden Eagles",
            "TeamCode": "USM"
        },
        "sso3": {
            "TeamName": "Marquette Golden Eagles",
            "TeamCode": "USM"
        },
        "ssp": {
            "TeamName": "Southern Utah",
            "TeamCode": "SUT"
        },
        "sss": {
            "TeamName": "Stanford",
            "TeamCode": "STA"
        },
        "sss2": {
            "TeamName": "Stanford Cardinal",
            "TeamCode": "STA"
        },
        "ssu": {
            "TeamName": "Missouri State",
            "TeamCode": "MIZST"
        },
        "ssv": {
            "TeamName": "Texas State",
            "TeamCode": "TXST"
        },
        "ssv2": {
            "TeamName": "Texas Tech Red Raiders",
            "TeamCode": "TT"
        },
        "tcu": {
            "TeamName": "TCU Horned Frogs",
            "TeamCode": "TCU"
        },
        "tcu2": {
            "TeamName": "Tcu Horned Frogs",
            "TeamCode": "TCU"
        },
        "ssw": {
            "TeamName": "Syracuse",
            "TeamCode": "SYR"
        },
        "ssw2": {
            "TeamName": "Syracuse Orange",
            "TeamCode": "SYR"
        },
        "ssx": {
            "TeamName": "Savannah State",
            "TeamCode": "SVS"
        },
        "stetson": {
            "TeamName": "Stetson",
            "TeamCode": "STU"
        },
        "tsa": {
            "TeamName": "UTSA",
            "TeamCode": "UTSA"
        },
        "tta": {
            "TeamName": "TCU",
            "TeamCode": "TCU"
        },
        "ttb": {
            "TeamName": "Temple",
            "TeamCode": "TEM"
        },
        "ttd": {
            "TeamName": "Tennessee",
            "TeamCode": "TEN"
        },
        "ttd2": {
            "TeamName": "Tennessee Volunteers",
            "TeamCode": "TEN"
        },
        "tth": {
            "TeamName": "Texas",
            "TeamCode": "TEX"
        },
        "tth2": {
            "TeamName": "Texas Longhorns",
            "TeamCode": "TEX"
        },
        "ttj": {
            "TeamName": "Texas A&M",
            "TeamCode": "TXAM"
        },
        "ttj2": {
            "TeamName": "Texas A&M Aggies",
            "TeamCode": "TXAM"
        },
        "ttl": {
            "TeamName": "UTEP",
            "TeamCode": "TEP"
        },
        "tto": {
            "TeamName": "Texas Tech",
            "TeamCode": "TT"
        },
        "ttp": {
            "TeamName": "Toledo",
            "TeamCode": "TOL"
        },
        "ttq": {
            "TeamName": "Towson",
            "TeamCode": "TWN"
        },
        "tts": {
            "TeamName": "Tulane",
            "TeamCode": "TUL"
        },
        "tts2": {
            "TeamName": "Tulane Green Wave",
            "TeamCode": "TUL"
        },
        "ttt": {
            "TeamName": "Tulsa",
            "TeamCode": "TSA"
        },
        "ttv": {
            "TeamName": "Troy",
            "TeamCode": "TRY"
        },
        "ttv2": {
            "TeamName": "Troy State Trojans",
            "TeamCode": "TRY"
        },
        "uua": {
            "TeamName": "UCLA",
            "TeamCode": "UCLA"
        },
        "uua2": {
            "TeamName": "UCLA Bruins",
            "TeamCode": "UCLA"
        },
        "uua3": {
            "TeamName": "Ucla Bruins",
            "TeamCode": "UCLA"
        },
        "uub": {
            "TeamName": "USC",
            "TeamCode": "USC"
        },
        "uub2": {
            "TeamName": "USC Trojans",
            "TeamCode": "USC"
        },
        "uub3": {
            "TeamName": "Usc Trojans",
            "TeamCode": "USC"
        },
        "uuc": {
            "TeamName": "Utah",
            "TeamCode": "UTH"
        },
        "uuc2": {
            "TeamName": "Utah Utes",
            "TeamCode": "UTH"
        },
        "uuc3": {
            "TeamName": "UConn Huskies",
            "TeamCode": "UCH"
        },
        "uuc4": {
            "TeamName": "UNC Charlotte 49ers",
            "TeamCode": "UNC"
        },
        "uud": {
            "TeamName": "Utah State",
            "TeamCode": "UTS"
        },
        "vva": {
            "TeamName": "Vanderbilt",
            "TeamCode": "VAN"
        },
        "vva2": {
            "TeamName": "Vanderbilt Commodores",
            "TeamCode": "VAN"
        },
        "vvb": {
            "TeamName": "Virginia",
            "TeamCode": "UVA"
        },
        "vvb2": {
            "TeamName": "Virginia Cavaliers",
            "TeamCode": "UVA"
        },
        "vvd": {
            "TeamName": "Virginia Tech",
            "TeamCode": "VT"
        },
        "vvd2": {
            "TeamName": "Virginia Tech Hokies",
            "TeamCode": "VT"
        },
        "vvh": {
            "TeamName": "Villanova",
            "TeamCode": "VIL"
        },
        "vvh2": {
            "TeamName": "Villanova Wildcats",
            "TeamCode": "VIL"
        },
        "vvi": {
            "TeamName": "Valparaiso",
            "TeamCode": "VAL"
        },
        "waa": {
            "TeamName": "Wagner",
            "TeamCode": "WAG"
        },
        "wwa": {
            "TeamName": "Wake Forest",
            "TeamCode": "WF"
        },
        "wwa2": {
            "TeamName": "Wake Forest Demon Deacons",
            "TeamCode": "WF"
        },
        "wwb": {
            "TeamName": "Washington",
            "TeamCode": "WAS"
        },
        "wwb2": {
            "TeamName": "Washington Huskies",
            "TeamCode": "WAS"
        },
        "wwc": {
            "TeamName": "Washington State",
            "TeamCode": "WST"
        },
        "wwc2": {
            "TeamName": "Washington State Cougars",
            "TeamCode": "WST"
        },
        "wwe": {
            "TeamName": "Weber State",
            "TeamCode": "WBS"
        },
        "wwh": {
            "TeamName": "West Virginia",
            "TeamCode": "WVU"
        },
        "wwh2": {
            "TeamName": "West Virginia Mountaineers",
            "TeamCode": "WVU"
        },
        "wwi": {
            "TeamName": "Western Carolina",
            "TeamCode": "WC"
        },
        "wwk": {
            "TeamName": "Western Kentucky",
            "TeamCode": "WKY"
        },
        "wwl": {
            "TeamName": "Western Michigan",
            "TeamCode": "WMC"
        },
        "wwn": {
            "TeamName": "William & Mary",
            "TeamCode": "WM"
        },
        "wwo": {
            "TeamName": "Wisconsin",
            "TeamCode": "WIS"
        },
        "wwo2": {
            "TeamName": "Wisconsin Badgers",
            "TeamCode": "WIS"
        },
        "wwq": {
            "TeamName": "Wyoming",
            "TeamCode": "WYO"
        },
        "yya": {
            "TeamName": "Yale",
            "TeamCode": "YAL"
        }
    }

    NHL = {
        "ana": {
            "TeamName": "Anaheim Ducks",
            "TeamCode": "441862de-0f24-11e2-8525-18a905767e44"
        },
        "ari": {
            "TeamName": "Arizona Coyotes",
            "TeamCode": "44153da1-0f24-11e2-8525-18a905767e44"
        },
        "bos": {
            "TeamName": "Boston Bruins",
            "TeamCode": "4416ba1a-0f24-11e2-8525-18a905767e44"
        },
        "buf": {
            "TeamName": "Buffalo Sabres",
            "TeamCode": "4416d559-0f24-11e2-8525-18a905767e44"
        },
        "cgy": {
            "TeamName": "Calgary Flames",
            "TeamCode": "44159241-0f24-11e2-8525-18a905767e44"
        },
        "car": {
            "TeamName": "Carolina Hurricanes",
            "TeamCode": "44182a9d-0f24-11e2-8525-18a905767e44"
        },
        "chi": {
            "TeamName": "Chicago Blackhawks",
            "TeamCode": "4416272f-0f24-11e2-8525-18a905767e44"
        },
        "col": {
            "TeamName": "Colorado Avalanche",
            "TeamCode": "4415ce44-0f24-11e2-8525-18a905767e44"
        },
        "cob": {
            "TeamName": "Columbus Blue Jackets",
            "TeamCode": "44167db4-0f24-11e2-8525-18a905767e44"
        },
        "dal": {
            "TeamName": "Dallas Stars",
            "TeamCode": "44157522-0f24-11e2-8525-18a905767e44"
        },
        "det": {
            "TeamName": "Detroit Red Wings",
            "TeamCode": "44169bb9-0f24-11e2-8525-18a905767e44"
        },
        "edm": {
            "TeamName": "Edmonton Oilers",
            "TeamCode": "4415ea6c-0f24-11e2-8525-18a905767e44"
        },
        "fla": {
            "TeamName": "Florida Panthers",
            "TeamCode": "4418464d-0f24-11e2-8525-18a905767e44"
        },
        "los": {
            "TeamName": "Los Angeles Kings",
            "TeamCode": "44151f7a-0f24-11e2-8525-18a905767e44"
        },
        "min": {
            "TeamName": "Minnesota Wild",
            "TeamCode": "4416091c-0f24-11e2-8525-18a905767e44"
        },
        "mon": {
            "TeamName": "Montreal Canadiens",
            "TeamCode": "441713b7-0f24-11e2-8525-18a905767e44"
        },
        "nas": {
            "TeamName": "Nashville Predators",
            "TeamCode": "441643b7-0f24-11e2-8525-18a905767e44"
        },
        "njd": {
            "TeamName": "New Jersey Devils",
            "TeamCode": "44174b0c-0f24-11e2-8525-18a905767e44"
        },
        "nyi": {
            "TeamName": "New York Islanders",
            "TeamCode": "441766b9-0f24-11e2-8525-18a905767e44"
        },
        "nyr": {
            "TeamName": "New York Rangers",
            "TeamCode": "441781b9-0f24-11e2-8525-18a905767e44"
        },
        "ott": {
            "TeamName": "Ottawa Senators",
            "TeamCode": "4416f5e2-0f24-11e2-8525-18a905767e44"
        },
        "phi": {
            "TeamName": "Philadelphia Flyers",
            "TeamCode": "44179d47-0f24-11e2-8525-18a905767e44"
        },
        "pit": {
            "TeamName": "Pittsburgh Penguins",
            "TeamCode": "4417b7d7-0f24-11e2-8525-18a905767e44"
        },
        "san": {
            "TeamName": "San Jose Sharks",
            "TeamCode": "44155909-0f24-11e2-8525-18a905767e44"
        },
        "stl": {
            "TeamName": "St. Louis Blues",
            "TeamCode": "441660ea-0f24-11e2-8525-18a905767e44"
        },
        "stl2": {
            "TeamName": "St Louis Blues",
            "TeamCode": "441660ea-0f24-11e2-8525-18a905767e44"
        },
        "tam": {
            "TeamName": "Tampa Bay Lightning",
            "TeamCode": "4417d3cb-0f24-11e2-8525-18a905767e44"
        },
        "tor": {
            "TeamName": "Toronto Maple Leafs",
            "TeamCode": "441730a9-0f24-11e2-8525-18a905767e44"
        },
        "van": {
            "TeamName": "Vancouver Canucks",
            "TeamCode": "4415b0a7-0f24-11e2-8525-18a905767e44"
        },
        "was": {
            "TeamName": "Washington Capitals",
            "TeamCode": "4417eede-0f24-11e2-8525-18a905767e44"
        },
        "wpg": {
            "TeamName": "Winnipeg Jets",
            "TeamCode": "44180e55-0f24-11e2-8525-18a905767e44"
        },
        "lvgk": {
            "TeamName": "Las Vegas Golden Knights",
            "TeamCode": "42376e1c-6da8-461e-9443-cfcf0a9fcc4d"
        }
    }

    FIFA = {
        "Argentina": {
            "TeamName": "Argentina",
            "TeamCode": "ARG"
        },
        "Australia": {
            "TeamName": "Australia",
            "TeamCode": "AUS"
        },
        "Belgium": {
            "TeamName": "Belgium",
            "TeamCode": "BEL"
        },
        "Brazil": {
            "TeamName": "Brazil",
            "TeamCode": "BRA"
        },
        "Colombia": {
            "TeamName": "Colombia",
            "TeamCode": "COL"
        },
        "Costa Rica": {
            "TeamName": "Costa Rica",
            "TeamCode": "CRC"
        },
        "Croatia": {
            "TeamName": "Croatia",
            "TeamCode": "CRO"
        },
        "Danmark": {
            "TeamName": "Danmark",
            "TeamCode": "DEN"
        },
        "Denmark": {
            "TeamName": "Denmark",
            "TeamCode": "DEN"
        },
        "Egypt": {
            "TeamName": "Egypt",
            "TeamCode": "EGY"
        },
        "Australia": {
            "TeamName": "Australia",
            "TeamCode": "AUS"
        },
        "England": {
            "TeamName": "England",
            "TeamCode": "ENG"
        },
        "France": {
            "TeamName": "France",
            "TeamCode": "FRA"
        },
        "Germany": {
            "TeamName": "Germany",
            "TeamCode": "GER"
        },
        "Iceland": {
            "TeamName": "Iceland",
            "TeamCode": "ISL"
        },
        "IR Iran": {
            "TeamName": "IR Iran",
            "TeamCode": "IRN"
        },
        "Iran": {
            "TeamName": "Iran",
            "TeamCode": "IRN"
        },
        "Japan": {
            "TeamName": "Japan",
            "TeamCode": "JPN"
        },
        "Korea Republic": {
            "TeamName": "Korea Republic",
            "TeamCode": "KOR"
        },
        "South Korea": {
            "TeamName": "South Korea",
            "TeamCode": "KOR"
        },
        "Mexico": {
            "TeamName": "Mexico",
            "TeamCode": "MEX"
        },
        "Morocco": {
            "TeamName": "Morocco",
            "TeamCode": "MAR"
        },
        "Nigeria": {
            "TeamName": "Nigeria",
            "TeamCode": "NGA"
        },
        "Panama": {
            "TeamName": "Panama",
            "TeamCode": "PAN"
        },
        "Peru": {
            "TeamName": "Peru",
            "TeamCode": "PER"
        },
        "Poland": {
            "TeamName": "Poland",
            "TeamCode": "POL"
        },
        "Portugal": {
            "TeamName": "Portugal",
            "TeamCode": "POR"
        },
        "Russia": {
            "TeamName": "Russia",
            "TeamCode": "RUS"
        },
        "Saudi Arabia": {
            "TeamName": "Saudi Arabia",
            "TeamCode": "KSA"
        },
        "Senegal": {
            "TeamName": "Senegal",
            "TeamCode": "SEN"
        },
        "Serbia": {
            "TeamName": "Serbia",
            "TeamCode": "SRB"
        },
        "Spain": {
            "TeamName": "Spain",
            "TeamCode": "ESP"
        },
        "Sweden": {
            "TeamName": "Sweden",
            "TeamCode": "SWE"
        },
        "Switcerland": {
            "TeamName": "Switzerland",
            "TeamCode": "MAR"
        },
        "Switzerland": {
            "TeamName": "Switzerland",
            "TeamCode": "SUI",
        },
        "Tunisia": {
            "TeamName": "Tunisia",
            "TeamCode": "TUN"
        },
        "Uruguay": {
            "TeamName": "Uruguay",
            "TeamCode": "URU"
        }
    }

    DELREY = {
        "Albacete": {
            "TeamName": "Albacete",
            "TeamCode": "Alba"
        },
        "Alcorcón": {
            "TeamName": "Alcorcón",
            "TeamCode": "Alco"
        },
        "Alcoyano": {
            "TeamName": "Alcoyano",
            "TeamCode": "Alcy"
        },
        "Almería": {
            "TeamName": "Almería",
            "TeamCode": "Alme"
        },
        "Antequera": {
            "TeamName": "Antequera",
            "TeamCode": "Ante"
        },
        "Arcos": {
            "TeamName": "Arcos",
            "TeamCode": "Arco"
        },
        "Athletic Club": {
            "TeamName": "Athletic Club",
            "TeamCode": "ABI"
        },
        "Atlético Baleares": {
            "TeamName": "Atlético Baleares",
            "TeamCode": "Bale"
        },
        "Atlético Madrid": {
            "TeamName": "Atlético Madrid",
            "TeamCode": "AMA"
        },
        "Badalona": {
            "TeamName": "Badalona",
            "TeamCode": "Bada"
        },
        "Barcelona": {
            "TeamName": "Barcelona",
            "TeamCode": "Barc"
        },
        "Cacereño": {
            "TeamName": "Cacereño",
            "TeamCode": "Cace"
        },
        "Cádiz": {
            "TeamName": "Cádiz",
            "TeamCode": "Cadi"
        },
        "CD Calahorra": {
            "TeamName": "CD Calahorra",
            "TeamCode": "Cala"
        },
        "Celta de Vigo": {
            "TeamName": "Celta de Vigo",
            "TeamCode": "CVI"
        },
        "Córdoba": {
            "TeamName": "Córdoba",
            "TeamCode": "Cord"
        },
        "Cultural Leonesa": {
            "TeamName": "Cultural Leonesa",
            "TeamCode": "Leon"
        },
        "Deportivo Alavés": {
            "TeamName": "Deportivo Alavés",
            "TeamCode": "ALA"
        },
        "Deportivo La Coruña": {
            "TeamName": "Deportivo La Coruña",
            "TeamCode": "Laco"
        },
        "Durango": {
            "TeamName": "Durango",
            "TeamCode": "Dura"
        },
        "Eibar": {
            "TeamName": "Eibar",
            "TeamCode": "Eiba"
        },
        "Elche": {
            "TeamName": "Elche",
            "TeamCode": "Elch"
        },
        "Espanyol": {
            "TeamName": "Espanyol",
            "TeamCode": "Espa"
        },
        "FC Cartagena": {
            "TeamName": "FC Cartagena",
            "TeamCode": "Cart"
        },
        "Formentera": {
            "TeamName": "Formentera",
            "TeamCode": "From"
        },
        "Fuenlabrada": {
            "TeamName": "Fuenlabrada",
            "TeamCode": "Fuen"
        },
        "Getafe": {
            "TeamName": "Getafe",
            "TeamCode": "Get"
        },
        "Gimnàstic Tarragona": {
            "TeamName": "Gimnàstic Tarragona",
            "TeamCode": "Gimn"
        },
        "Gimnástica Segoviana": {
            "TeamName": "Gimnástica Segoviana",
            "TeamCode": "Sego"
        },
        "Gimnástica Torrelavega": {
            "TeamName": "Gimnástica Torrelavega",
            "TeamCode": "Torr"
        },
        "Girona": {
            "TeamName": "Girona",
            "TeamCode": "Giro"
        },
        "Granada": {
            "TeamName": "Granada",
            "TeamCode": "Gran"
        },
        "Hércules": {
            "TeamName": "Hércules",
            "TeamCode": "Herc"
        },
        "Huesca": {
            "TeamName": "Huesca",
            "TeamCode": "Hues"
        },
        "Las Palmas": {
            "TeamName": "Las Palmas",
            "TeamCode": "Palm"
        },
        "Leganés": {
            "TeamName": "Leganés",
            "TeamCode": "Lega"
        },
        "Leioa": {
            "TeamName": "Leioa",
            "TeamCode": "Leio"
        },
        "Levante": {
            "TeamName": "Levante",
            "TeamCode": "Leva"
        },
        "Lleida Esportiu": {
            "TeamName": "Lleida Esportiu",
            "TeamCode": "Llei"
        },
        "Lorca": {
            "TeamName": "Lorca",
            "TeamCode": "Lora"
        },
        "Lorca Deportiva": {
            "TeamName": "Lorca Deportiva",
            "TeamCode": "Lorc"
        },
        "Lugo": {
            "TeamName": "Lugo",
            "TeamCode": "Lugo"
        },
        "Málaga": {
            "TeamName": "Málaga",
            "TeamCode": "Mala"
        },
        "Mallorca": {
            "TeamName": "Mallorca",
            "TeamCode": "Mall"
        },
        "Marbella": {
            "TeamName": "Marbella",
            "TeamCode": "Marb"
        },
        "Melilla": {
            "TeamName": "Melilla",
            "TeamCode": "Meli"
        },
        "Mérida AD": {
            "TeamName": "Mérida AD",
            "TeamCode": "Meri"
        },
        "Mirandés": {
            "TeamName": "Mirandés",
            "TeamCode": "Mira"
        },
        "Numancia": {
            "TeamName": "Numancia",
            "TeamCode": "Numa"
        },
        "Olímpic de Xàtiva": {
            "TeamName": "Olímpic de Xàtiva",
            "TeamCode": "Olim"
        },
        "Olot": {
            "TeamName": "Olot",
            "TeamCode": "Olot"
        },
        "Osasuna": {
            "TeamName": "Osasuna",
            "TeamCode": "Osas"
        },
        "Peña Sport": {
            "TeamName": "Peña Sport",
            "TeamCode": "Spor"
        },
        "Ponferradina": {
            "TeamName": "Ponferradina",
            "TeamCode": "Ponf"
        },
        "Pontevedra": {
            "TeamName": "Pontevedra",
            "TeamCode": "Pont"
        },
        "Racing Ferrol": {
            "TeamName": "Racing Ferrol",
            "TeamCode": "Raci"
        },
        "Racing Santander": {
            "TeamName": "Racing Santander",
            "TeamCode": "Sant"
        },
        "Rápido Bouzas": {
            "TeamName": "Rápido Bouzas",
            "TeamCode": "Bouz"
        },
        "Rayo Majadahonda": {
            "TeamName": "Rayo Majadahonda",
            "TeamCode": "Maja"
        },
        "Rayo Vallecano": {
            "TeamName": "Rayo Vallecano",
            "TeamCode": "Rayo"
        },
        "Real Avilés": {
            "TeamName": "Real Avilés",
            "TeamCode": "Avil"
        },
        "Real Betis": {
            "TeamName": "Real Betis",
            "TeamCode": "BET"
        },
        "Real Madrid": {
            "TeamName": "Real Madrid",
            "TeamCode": "RMA"
        },
        "Real Murcia": {
            "TeamName": "Real Murcia",
            "TeamCode": "Rmur"
        },
        "Real Oviedo": {
            "TeamName": "Real Oviedo",
            "TeamCode": "Rovie"
        },
        "Real Sociedad": {
            "TeamName": "Real Sociedad",
            "TeamCode": "Soci"
        },
        "Real Unión": {
            "TeamName": "Real Unión",
            "TeamCode": "Unio"
        },
        "Real Valladolid": {
            "TeamName": "Real Valladolid",
            "TeamCode": "Vall"
        },
        "Valladolid": {
            "TeamName": "Real Valladolid",
            "TeamCode": "Vall"
        },
        "Real Zaragoza": {
            "TeamName": "Real Zaragoza",
            "TeamCode": "Zara"
        },
        "Reus Deportiu": {
            "TeamName": "Reus Deportiu",
            "TeamCode": "Depo"
        },
        "Sevilla": {
            "TeamName": "Sevilla",
            "TeamCode": "Sevi"
        },
        "Sporting Gijón": {
            "TeamName": "Sporting Gijón",
            "TeamCode": "Gion"
        },
        "Talavera CF": {
            "TeamName": "Talavera CF",
            "TeamCode": "Tala"
        },
        "Tarazona": {
            "TeamName": "Tarazona",
            "TeamCode": "Tara"
        },
        "Tenerife": {
            "TeamName": "Tenerife",
            "TeamCode": "Tene"
        },
        "Toledo": {
            "TeamName": "Toledo",
            "TeamCode": "Tole"
        },
        "UCAM Murcia": {
            "TeamName": "UCAM Murcia",
            "TeamCode": "Murc"
        },
        "UD Logroñés": {
            "TeamName": "UD Logroñés",
            "TeamCode": "Log"
        },
        "UD San Fernando": {
            "TeamName": "UD San Fernando",
            "TeamCode": "Fern"
        },
        "Unión Adarve": {
            "TeamName": "Unión Adarve",
            "TeamCode": "Adar"
        },
        "Valencia": {
            "TeamName": "Valencia",
            "TeamCode": "Vale"
        },
        "Villanovense": {
            "TeamName": "Villanovense",
            "TeamCode": "Vila"
        },
        "Villarreal": {
            "TeamName": "Villarreal",
            "TeamCode": "Vill"
        },
        "Dejion": {
            "TeamName": "Dejion",
            "TeamCode": "Deji"
        }

    }

    FACUP = {
        "Accrington Stanley": {
            "TeamName": "Accrington Stanley",
            "TeamCode": "Accr"
        },
        "AFC Bournemouth": {
            "TeamName": "AFC Bournemouth",
            "TeamCode": "Bour"
        },
        "AFC Wimbledon": {
            "TeamName": "AFC Wimbledon",
            "TeamCode": "Wimb"
        },
        "Arsenal": {
            "TeamName": "Arsenal",
            "TeamCode": "Ars"
        },
        "Aston Villa": {
            "TeamName": "Aston Villa",
            "TeamCode": "Asto"
        },
        "Bamber Bridge": {
            "TeamName": "Bamber Bridge",
            "TeamCode": "Bamb"
        },
        "Barnet": {
            "TeamName": "Barnet",
            "TeamCode": "Barn"
        },
        "Barnsley": {
            "TeamName": "Barnsley",
            "TeamCode": "Bars"
        },
        "Barwell": {
            "TeamName": "Barwell",
            "TeamCode": "Barw"
        },
        "Birmingham City": {
            "TeamName": "Birmingham City",
            "TeamCode": "Birm"
        },
        "Blackburn Rovers": {
            "TeamName": "Blackburn Rovers",
            "TeamCode": "Blac"
        },
        "Blackpool": {
            "TeamName": "Blackpool",
            "TeamCode": "Blap"
        },
        "Bolton Wanderers": {
            "TeamName": "Bolton Wanderers",
            "TeamCode": "Bolt"
        },
        "Boston United": {
            "TeamName": "Boston United",
            "TeamCode": "Bost"
        },
        "Bournemouth FC": {
            "TeamName": "Bournemouth FC",
            "TeamCode": "Bour"
        },
        "Bradford City": {
            "TeamName": "Bradford City",
            "TeamCode": "Brad"
        },
        "Brentford": {
            "TeamName": "Brentford",
            "TeamCode": "Bren"
        },
        "Brighton & Hove Albion": {
            "TeamName": "Brighton & Hove Albion",
            "TeamCode": "Brig"
        },
        "Bristol City": {
            "TeamName": "Bristol City",
            "TeamCode": "Bris"
        },
        "Bristol Manor Farm": {
            "TeamName": "Bristol Manor Farm",
            "TeamCode": "Mano"
        },
        "Bristol Rovers": {
            "TeamName": "Bristol Rovers",
            "TeamCode": "Rove"
        },
        "Burnley": {
            "TeamName": "Burnley",
            "TeamCode": "Burn"
        },
        "Burton Albion": {
            "TeamName": "Burton Albion",
            "TeamCode": "Burt"
        },
        "Bury": {
            "TeamName": "Bury",
            "TeamCode": "Bury"
        },
        "Cambridge United": {
            "TeamName": "Cambridge United",
            "TeamCode": "Camu"
        },
        "Cardiff City": {
            "TeamName": "Cardiff City",
            "TeamCode": "CAR"
        },
        "Carlisle United": {
            "TeamName": "Carlisle United",
            "TeamCode": "Carl"
        },
        "Charlton Athletic": {
            "TeamName": "Charlton Athletic",
            "TeamCode": "Char"
        },
        "Chelsea": {
            "TeamName": "Chelsea",
            "TeamCode": "Chel"
        },
        "Cheltenham Town": {
            "TeamName": "Cheltenham Town",
            "TeamCode": "Chet"
        },
        "Chesterfield": {
            "TeamName": "Chesterfield",
            "TeamCode": "Ches"
        },
        "Colchester United": {
            "TeamName": "Colchester United",
            "TeamCode": "Colc"
        },
        "Coventry City": {
            "TeamName": "Coventry City",
            "TeamCode": "Cove"
        },
        "Crawley Town": {
            "TeamName": "Crawley Town",
            "TeamCode": "Crat"
        },
        "Crewe Alexandra": {
            "TeamName": "Crewe Alexandra",
            "TeamCode": "Crew"
        },
        "Crystal Palace": {
            "TeamName": "Crystal Palace",
            "TeamCode": "Crys"
        },
        "Derby County": {
            "TeamName": "Derby County",
            "TeamCode": "Derb"
        },
        "Doncaster Rovers": {
            "TeamName": "Doncaster Rovers",
            "TeamCode": "Donc"
        },
        "Ebbsfleet United": {
            "TeamName": "Ebbsfleet United",
            "TeamCode": "Ebbs"
        },
        "Everton": {
            "TeamName": "Everton",
            "TeamCode": "Ever"
        },
        "Exeter City": {
            "TeamName": "Exeter City",
            "TeamCode": "Exet"
        },
        "Fleetwood Town": {
            "TeamName": "Fleetwood Town",
            "TeamCode": "Flee"
        },
        "Forest Green Rovers": {
            "TeamName": "Forest Green Rovers",
            "TeamCode": "Fore"
        },
        "Fulham": {
            "TeamName": "Fulham",
            "TeamCode": "Fulh"
        },
        "Fylde": {
            "TeamName": "Fylde",
            "TeamCode": "Flyd"
        },
        "Gillingham": {
            "TeamName": "Gillingham",
            "TeamCode": "Gill"
        },
        "Grimsby Town": {
            "TeamName": "Grimsby Town",
            "TeamCode": "Grit"
        },
        "Hartlepool United": {
            "TeamName": "Hartlepool United",
            "TeamCode": "Hart"
        },
        "Huddersfield Town": {
            "TeamName": "Huddersfield Town",
            "TeamCode": "Hudd"
        },
        "Hull City": {
            "TeamName": "Hull City",
            "TeamCode": "Hull"
        },
        "Ipswich Town": {
            "TeamName": "Ipswich Town",
            "TeamCode": "Ipsw"
        },
        "Kingstonian": {
            "TeamName": "Kingstonian",
            "TeamCode": "King"
        },
        "Leatherhead": {
            "TeamName": "Leatherhead",
            "TeamCode": "Leat"
        },
        "Leeds United": {
            "TeamName": "Leeds United",
            "TeamCode": "Leed"
        },
        "Leicester City": {
            "TeamName": "Leicester City",
            "TeamCode": "Leic"
        },
        "Liverpool": {
            "TeamName": "Liverpool",
            "TeamCode": "Liv"
        },
        "Luton Town": {
            "TeamName": "Luton Town",
            "TeamCode": "Luto"
        },
        "Maidstone United": {
            "TeamName": "Maidstone United",
            "TeamCode": "Maid"
        },
        "Manchester City": {
            "TeamName": "Manchester City",
            "TeamCode": "Mci"
        },
        "Manchester United": {
            "TeamName": "Manchester United",
            "TeamCode": "Manu"
        },
        "Mansfield Town": {
            "TeamName": "Mansfield Town",
            "TeamCode": "Mans"
        },
        "Middlesbrough": {
            "TeamName": "Middlesbrough",
            "TeamCode": "Midd"
        },
        "Millwall": {
            "TeamName": "Millwall",
            "TeamCode": "Mill"
        },
        "Milton Keynes Dons": {
            "TeamName": "Milton Keynes Dons",
            "TeamCode": "Mkdo"
        },
        "Morecambe": {
            "TeamName": "Morecambe",
            "TeamCode": "More"
        },
        "Newcastle United": {
            "TeamName": "Newcastle United",
            "TeamCode": "Newu"
        },
        "Newport County": {
            "TeamName": "Newport County",
            "TeamCode": "Newp"
        },
        "Norwich City": {
            "TeamName": "Norwich City",
            "TeamCode": "Norw"
        },
        "Nottingham Forest": {
            "TeamName": "Nottingham Forest",
            "TeamCode": "Notf"
        },
        "Notts County": {
            "TeamName": "Notts County",
            "TeamCode": "Notc"
        },
        "Oldham Athletic": {
            "TeamName": "Oldham Athletic",
            "TeamCode": "Oldh"
        },
        "Oxford City": {
            "TeamName": "Oxford City",
            "TeamCode": "Oxf"
        },
        "Peterborough United": {
            "TeamName": "Peterborough United",
            "TeamCode": "Pete"
        },
        "Plymouth Argyle": {
            "TeamName": "Plymouth Argyle",
            "TeamCode": "Plym"
        },
        "Port Vale": {
            "TeamName": "Port Vale",
            "TeamCode": "Porv"
        },
        "Portsmouth": {
            "TeamName": "Portsmouth",
            "TeamCode": "Port"
        },
        "Preston North End": {
            "TeamName": "Preston North End",
            "TeamCode": "Pres"
        },
        "Queens Park Rangers": {
            "TeamName": "Queens Park Rangers",
            "TeamCode": "Quee"
        },
        "Reading": {
            "TeamName": "Reading",
            "TeamCode": "Read"
        },
        "Rochdale": {
            "TeamName": "Rochdale",
            "TeamCode": "Roch"
        },
        "Rotherham United": {
            "TeamName": "Rotherham United",
            "TeamCode": "Roth"
        },
        "Salford City": {
            "TeamName": "Salford City",
            "TeamCode": "Salt"
        },
        "Scunthorpe United": {
            "TeamName": "Scunthorpe United",
            "TeamCode": "Scun"
        },
        "Sheffield United": {
            "TeamName": "Sheffield United",
            "TeamCode": "Sheu"
        },
        "Sheffield Wednesday": {
            "TeamName": "Sheffield Wednesday",
            "TeamCode": "Wedn"
        },
        "Shrewsbury Town": {
            "TeamName": "Shrewsbury Town",
            "TeamCode": "Shre"
        },
        "Slough Town": {
            "TeamName": "Slough Town",
            "TeamCode": "Slou"
        },
        "Solihull Moors": {
            "TeamName": "Solihull Moors",
            "TeamCode": "Soli"
        },
        "Southampton": {
            "TeamName": "Southampton",
            "TeamCode": "Sout"
        },
        "Southend United": {
            "TeamName": "Southend United",
            "TeamCode": "Suni"
        },
        "St Albans City": {
            "TeamName": "St Albans City",
            "TeamCode": "Alba"
        },
        "Stevenage": {
            "TeamName": "Stevenage",
            "TeamCode": "Stev"
        },
        "Stoke City": {
            "TeamName": "Stoke City",
            "TeamCode": "Stok"
        },
        "Sunderland": {
            "TeamName": "Sunderland",
            "TeamCode": "Sund"
        },
        "Sutton United": {
            "TeamName": "Sutton United",
            "TeamCode": "Sutu"
        },
        "Swansea City": {
            "TeamName": "Swansea City",
            "TeamCode": "Swan"
        },
        "Swindon Town": {
            "TeamName": "Swindon Town",
            "TeamCode": "Swin"
        },
        "Tamworth": {
            "TeamName": "Tamworth",
            "TeamCode": "Tamw"
        },
        "Torquay United": {
            "TeamName": "Torquay United",
            "TeamCode": "Torq"
        },
        "Tottenham Hotspur": {
            "TeamName": "Tottenham Hotspur",
            "TeamCode": "Tott"
        },
        "Tranmere Rovers": {
            "TeamName": "Tranmere Rovers",
            "TeamCode": "Tran"
        },
        "Truro City": {
            "TeamName": "Truro City",
            "TeamCode": "Turo"
        },
        "Walsall": {
            "TeamName": "Walsall",
            "TeamCode": "Wals"
        },
        "Watford": {
            "TeamName": "Watford",
            "TeamCode": "Watf"
        },
        "Wealdstone": {
            "TeamName": "Wealdstone",
            "TeamCode": "Wea"
        },
        "West Bromwich Albion": {
            "TeamName": "West Bromwich Albion",
            "TeamCode": "Brom"
        },
        "West Ham United": {
            "TeamName": "West Ham United",
            "TeamCode": "Wesu"
        },
        "Whitehawk": {
            "TeamName": "Whitehawk",
            "TeamCode": "Whit"
        },
        "Wigan Athletic": {
            "TeamName": "Wigan Athletic",
            "TeamCode": "Wiga"
        },
        "Woking": {
            "TeamName": "Woking",
            "TeamCode": "Wok"
        },
        "Wolverhampton Wanderers": {
            "TeamName": "Wolverhampton Wanderers",
            "TeamCode": "WOL"
        },
        "Wycombe Wanderers": {
            "TeamName": "Wycombe Wanderers",
            "TeamCode": "Wyco"
        },
        "Yeovil Town": {
            "TeamName": "Yeovil Town",
            "TeamCode": "Yeov"
        },
        "York City": {
            "TeamName": "York City",
            "TeamCode": "York"
        }
    }




