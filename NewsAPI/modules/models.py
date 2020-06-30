from modules.app import db
from dateparser import parse

SOCCER_LEAGUES = ['EPL', 'LALIGA', 'UEFA', 'Bund', 'SerieA',
                  'LIGUE', 'ERED', 'MLS', 'PRIME', 'Argent',
                  'Brazil', 'Mexico', 'EFL', 'FACUP', 'Turkey',
                  'EuroL', 'SERIEA', 'BUND']


class News(db.Document):
    title = db.StringField()
    description = db.StringField()
    link = db.StringField()
    image = db.StringField()
    sport = db.StringField(default="")
    team = db.StringField()
    league = db.StringField()
    source = db.StringField()
    published_at = db.StringField()
    crawled_time = db.DateTimeField()
    team_code = db.StringField()
    hash = db.StringField()
    isExternal = db.BoolField(default=False)


    def serialize(self):
        sport = ''
        if self.league in SOCCER_LEAGUES:
            sport = 'SOCCER'

        if self.description == "":
            self.isExternal = True

        if "CopaDelRey" in self.league:
            self.league = "DELREY"

        # if "SerieA" in self.league:
        #     self.league = "SERIEA"
        #
        # if "Bund" in self.league:
        #     self.league = "BUND"

        self.fixDate()

        return {
            'title': self.title,
            'description': self.description,
            'link': self.link,
            'image': self.image,
            'team': self.team,
            'league': self.league,
            'source': self.source,
            'published_at': self.published_at,
            'crawled_time': self.crawled_time,
            'team_code': self.team_code,
            'hash': self.hash,
            'sport': sport,
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

