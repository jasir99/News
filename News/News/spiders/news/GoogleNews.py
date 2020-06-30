import scrapy
from datetime import datetime
import hashlib

from ..models import News

from ..database import session
from dateparser import parse

from ..utils.NewsUtils import getCrawlerStats, updateCrawlerStats
from ..sources.sources import GOOGLE_NEWS

'''
    scrapy crawl GoogleNews --set="ROBOTSTXT_OBEY=False"

'''

class GoogleNews(scrapy.Spider):
    name = "GoogleNews"
    base_urls = ['http://news.google.com']

    def __init__(self):
        self.start_urls = [GOOGLE_NEWS[0]["link"]]
        self.pushData = []
        self.crawlerStats = getCrawlerStats(self.name, session)


    def parse(self, response):
        for team in GOOGLE_NEWS:
            request = scrapy.Request(team["link"] + '/', callback=self.parseTeam, dont_filter=True)
            request.meta['team'] = team
            yield request

    def parseTeam(self, response):
        team = response.meta['team']

        #news_section_list = response.xpath("//div/div/main/c-wiz/div//div")
        news_section_list = response.xpath("//div/div/main/c-wiz/div/div/main/div[1]/div")

        i = 1
        for ne in news_section_list:
            news_list = ne.xpath(".//article")
            for n in news_list:
                if n.xpath(".//h4/a//text()").extract_first() is not None:
                    title = n.xpath(".//h4/a//text()").extract_first()
                    published_at = n.xpath(".//time/text()").extract_first(default="")
                    try:
                        date = str(parse(published_at))
                    except:
                        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    description = ""
                    link = "{}{}".format(self.base_urls[0], n.xpath(".//h4/a/@href").extract_first()[1:])
                    if "http" in link:
                        link = link.replace("http", "https")
                        
                    source = team["link"]
                    league = team["league"]
                    team_code = team["team_code"]
                    team_name = team["team"]

                    image = n.xpath(".//img/@src").extract_first()
                    if image is None:
                        image = ne.xpath(".//figure/img/@src").extract_first()
                        if image is None:
                            image = ne.xpath("//*[ancestor::figure/img/@src]/@src".format(i)).extract_first(default="NA")

                    if "=w32" in image:
                        image = "NA"

                    if i < team['newsCount']:
                        article = News(title=title, published_at=date, image=image,
                                       description=description,
                                       link=link, source=source, league=league, crawled_time=datetime.now(),
                                       team=team_name,
                                       team_code=team_code,
                                       hash=hashlib.sha224(link + team["team"].encode("utf-8")).hexdigest(),
                                       isExternal=True)

                        a = session.query(News).filter(News.hash == article.hash).first()

                        if a is None:
                            session.save(article)
                            updateCrawlerStats(self.crawlerStats, session)

                        i+=1
