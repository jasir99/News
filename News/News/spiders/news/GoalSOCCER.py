import scrapy
import hashlib

from ..models import News, TeamCodes

from ..database import session
from dateutil.parser import parse

from ..utils.NewsUtils import *
from ..utils.GetTeamCode import getTeamCode

GOAL_SOURCES = {
    "EPL": "https://www.goal.com/en/news/1862/premier-league?ICID=OP_TN_3_4",
    "LALIGA": "https://www.goal.com/en/primera-divisi%C3%B3n/34pl8szyvrbwcmfkuocjm3r6t",
    "SerieA": "https://www.goal.com/en/serie-a/1r097lpxe0xn03ihb7wi98kao",
    "Bund": "https://www.goal.com/en/bundesliga/6by3h89i2eykc341oz7lv1ddd"
}

'''
    scrapy crawl GoalSOCCER -a url=<url1> -a league=<league1>
    
'''

class GoalSOCCERSpider(scrapy.Spider):
    name = "GoalSOCCER"
    base_urls = ['https://www.goal.com']
    data = {}

    def __init__(self, url, league):
        self.start_urls = [url]
        self.URL = url
        self.LEAGUE = league
        self.pushData = []
        self.crawlerStats = getCrawlerStats(self.name, session)


    def start_requests(self):
        url = self.start_urls[0]
        request = scrapy.Request(url, self.parse)
        yield request


    def parse(self, response):
        i = 1
        for link in response.selector.xpath("//section[@class='widget-list-of-teams']/div[@class='group clearfix']/div[@class='team']/a/@href"):
            ilink = link.extract()
            ilink = self.base_urls[0]+ilink
            print ("TEAM: " + response.selector.xpath("//div[@class='group clearfix']/div[@class='team'][{}]/a/span[@class='team-name']/text()".format(i)).extract_first().encode("utf-8"))
            request = scrapy.Request(ilink + '/', callback=self.parseTeamNews, dont_filter=True)
            request.meta['team'] = response.selector.xpath("//div[@class='group clearfix']/div[@class='team'][{}]/a/span[@class='team-name']/text()".format(i)).extract_first().encode("utf-8")
            i += 1
            yield request


    def parseTeamNews(self, response):
        for link in response.selector.xpath("//article/a/@href"):
            try:
                ilink = link.extract()
                ilink = self.base_urls[0] + ilink
                request = scrapy.Request(ilink + '/', callback=self.parseNews, dont_filter=True)
                request.meta['team'] = response.meta['team']
                yield request
            except:
                print ("Failed to parse Level 2: {}".format(link))


    def parseNews(self, response):
        team = response.meta['team']

        if team not in self.data:
            self.data[team] = []

        title = response.selector.xpath("//h1[@class='article-headline']/text()").extract_first()
        published_at = response.selector.xpath("//div[@class='actions-bar']/time/text()").extract_first()
        image=""
        try:
            image = response.selector.xpath("//article/div[1]/div[5]/div[2]/noscript").extract_first().split("\"")[3]
        except:
            pass
        description = ""
        for p in response.selector.xpath("//div[@class='article-container  clearfix']/div/p/text()"):
            description += p.extract()
        link = response.url
        self.data[team].append({
            'title': title,
            'publishedAt': published_at,
            'image': image,
            'description': description,
            'link': link,
            'team': team,
            'league': self.LEAGUE,
            'source': response.url
        })

        team_code = getTeamCode(TeamCodes, self.LEAGUE, team)
        try:
            date = str(parse(published_at, fuzzy=True))
        except:
            date = str(datetime.now())

        if self.LEAGUE != "UEFA" or (self.LEAGUE == "UEFA" and team_code != "NA"):
            isExternal = checkDescription(description)
            article = News(title=title, published_at=date, image=image or '', description=description,
                           link=link, source=self.URL, league=self.LEAGUE, crawled_time=datetime.now(),
                           team=team, team_code=team_code, sport='SOCCER',
                           hash=hashlib.sha224(link.encode() + team.encode("utf-8")).hexdigest(),
                           isExternal=isExternal)

            a = session.query(News).filter(News.hash == article.hash).first()

            if a is None:
                session.save(article)
                updateCrawlerStats(self.crawlerStats, session)
