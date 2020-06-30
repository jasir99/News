import scrapy
from datetime import datetime
import hashlib
from dateparser import parse
from ..models import News
from ..database import session
from ..utils.NewsUtils import getCrawlerStats, updateCrawlerStats
from ..sources.sources import BING_NEWS


SOCCER_LEAGUES = ['EPL', 'LALIGA', 'UEFA', 'BUND', 'SerieA',
                  'LIGUE', 'ERED', 'MLS', 'PRIME', 'Argent',
                  'Brazil', 'Mexico', 'EFL', 'FACUP', 'TURKEY',
                  'EUROL', 'ENGL1', 'PREMIER','UEFA']

OTHER_LEAGUES = ['NFL', 'NBA', 'MLB', 'NHL', 'NCAAMB']

NCAAFB = ['NCAAFB']


'''
    scrapy crawl BingNews -a sport=<sport>
    
    sport: - SOCCER
           - NCAAFB
           - OTHER

'''

class BingNews(scrapy.Spider):
    name = "BingNews"
    base_urls = ['https://www.bing.com']

    def __init__(self, sport):
        self.start_urls = [BING_NEWS[0]["link2"]]
        if sport == 'SOCCER':
            self.SPORT = SOCCER_LEAGUES
        elif sport == 'NCAAFB':
            self.SPORT = NCAAFB
        elif sport == 'OTHER':
            self.SPORT = OTHER_LEAGUES
        else:
            self.SPORT = SOCCER_LEAGUES + OTHER_LEAGUES + NCAAFB

        self.crawlerStats = getCrawlerStats(self.name, session)


    def parse(self, response):
        for team in BING_NEWS:
            if team["league"] in self.SPORT:
                request = scrapy.Request(team["link2"] + '/', callback=self.parseTeam, dont_filter=True)
                request.meta['team'] = team
                yield request


    def parseTeam(self, response):
        print("PARSING TEAM")
        team = response.meta['team']
        news_section_list = response.xpath("//div[@class='news-card newsitem cardcommon b_cards2']")
        i = 1
        for ne in news_section_list:
            print("YES")
            title = ne.xpath(".//a[@class='title']/text()").extract_first()
            image = ne.xpath(".//a[@class='imagelink']//img/@src").extract_first(default="NA")
            link = ne.xpath(".//a[@class='title']/@href").extract_first()
            date = ne.xpath(".//div[@class='source']/span[2]/text()").extract_first()

            if image != "NA":
                image = self.base_urls[0] + image

            try:
                now = datetime.now()
                if "m" in date and "mon" not in date:
                    date=date.replace("m","minutes")
                date = parse(date)
                diff = now - date
                hours = diff.seconds / 3600
                if 24 >= hours >= -24:
                    date = str(date)
                else:
                    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            except:
                date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            article = News(title=title, published_at=date, image=image,
                           description="",
                           link=link, source=team["link2"], league=team["league"], crawled_time=datetime.now(),
                           team=team["team"],
                           team_code=team["team_code"], sport=self.SPORT,
                           hash=hashlib.sha224(link + team["team"].encode("utf-8")).hexdigest(),
                           isExternal=True)

            a = session.query(News).filter(News.hash == article.hash).first()

            if a is None:
                session.save(article)
                updateCrawlerStats(self.crawlerStats, session)
            i += 1
